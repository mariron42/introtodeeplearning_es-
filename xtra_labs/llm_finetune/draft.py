"""
Borrador del flujo del laboratorio en formato de script usando PyTorch
"""
from datasets import load_dataset
import math
import numpy as np
import pandas as pd
import random
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import CrossEntropyLoss
from torch.optim import Adam
import transformers
from trl import SFTTrainer
from tqdm import tqdm

from utils import run_benchmark, make_spider_plot

# Parte 1

# TEXTO: descripción general del laboratorio de LLM
# Cargar LLM preentrenado (modelo de tamaño mediano)

# model_name = "facebook/opt-1.3b"
model_name = "facebook/opt-125m"
model = transformers.AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)

# TEXTO: explicar el tokenizador
# Incluir celda para inspección del tokenizador

# TEXTO: explicar cómo se entrenan los LLM para la predicción del siguiente token
# Escribir una función para predecir el siguiente token
def predict_next_token(probs, tokenizer):
    new_token = np.random.choice(len(probs), p=probs.numpy())
    print(tokenizer.decode(new_token), end='', flush=True)
    return new_token

# TEXTO: explicar que la predicción del siguiente token debe llamarse múltiples veces para la inferencia
# Llamar en bucle para inferencia autorregresiva
def generate(start_text, model, tokenizer, num_steps=20, temp=1.): 
    print(start_text, end="")
    x = tokenizer.encode(start_text)
    num_start = len(x)

    for i in range(num_steps):
        input_tensor = torch.tensor(x).view(1, -1).to("cuda")
        logits = model(input_tensor).logits
        probs = F.softmax(logits/temp, dim=-1)[0, -1, :].cpu().detach()

        new_token = predict_next_token(probs, tokenizer)
        x.append(new_token)
    
    output = tokenizer.decode(x[num_start:])
    return output

def generate_pt(model, tokenizer, text, num_steps=50, until=None, temp=1.): 
    device = model.device
    print(text, end='', flush=True)
    x = tokenizer.encode(text)
    enc_until = tokenizer.encode(until)[1:]
    num_start = len(x)

    decoded = tokenizer.decode(x)

    for step in range(num_steps): 
        with torch.no_grad():
            input_tensor = torch.reshape(torch.LongTensor(x), [1, -1]).to(device)
            logits = model(input_tensor).logits
            probs = F.softmax(logits/temp, dim=-1)[0, -1, :]
        probs = probs.detach().cpu().numpy()

        new_token = np.random.choice(len(probs), p=probs)
        x.append(new_token)

        new_decoded = tokenizer.decode(x)
        new_part = new_decoded[len(decoded):]
        decoded = new_decoded

        print(new_part, end='', flush=True)
        text += new_part

        if len(x) >= len(until) and text[-len(until):] == until:
            break 
        
    
    output = tokenizer.decode(x[num_start:])
    print("\n", flush=True)
    return output

# Probar la generación autorregresiva
# while True: 
#     print("\n\n\n\n\n")
#     input_text = input("Prompt: ")
#     output = generate(input_text, model, tokenizer)

# TEXTO: algo de contexto sobre la evaluación comparativa de LLM
# Cargar conjunto de datos de referencia y evaluar el modelo
benchmark_dataset = pd.read_csv("benchmark.csv")
# category_accs_1300m, avg_acc_1300m = run_benchmark(model, tokenizer, benchmark_dataset)

# TEXTO: pedirles que hagan una predicción sobre cómo la precisión se verá afectada por diferentes tamaños de modelo

# Evaluar modelo más pequeño
# model_name_350m = "facebook/opt-350m" 
# model_350m = transformers.AutoModelForCausalLM.from_pretrained(model_name_350m, device_map="auto")
# tokenizer_350m = transformers.AutoTokenizer.from_pretrained(model_name_350m)

# category_accs_350m, avg_acc_350m = run_benchmark(model_350m, tokenizer_350m, benchmark_dataset)

# Evaluar modelo más grande
# model_name_2700m = "facebook/opt-2.7b" 
# model_2700m = transformers.AutoModelForCausalLM.from_pretrained(model_name_2700m, device_map="auto")
# tokenizer_2700m = transformers.AutoTokenizer.from_pretrained(model_name_2700m)

# category_accs_2700m, avg_acc_2700m = run_benchmark(model_2700m, tokenizer_2700m, benchmark_dataset)

# Gráfico de araña

# benchmark_data = {"350M-Model": category_accs_350m, "1300M-Model": category_accs_1300m, "2700M-Model": category_accs_2700m}
# benchmark_data = {"350M-Model": category_accs_1300m}
# make_spider_plot(benchmark_data)

def print_lora_params(module, layer_type):
    summ = 0
    for name, child in module.named_children():
        if isinstance(child, layer_type):
            num_params = sum(p.numel() for p in child.parameters() if p.requires_grad)

            print(name, num_params, child.in_features, child.out_features, (child.in_features * 8 + child.out_features * 8 == num_params))
            
            summ += num_params
        else:
            summ += print_lora_params(child, layer_type)
    
    return summ

# Parte 2

# inspeccionar modelo actual
# print(model)

# summ = print_lora_params(model, nn.Linear)

# print("with function", summ)

# print("without function", sum(p.numel() for p in model.parameters() if p.requires_grad))

# # congelar todos los gradientes de parámetros
for param in model.parameters():
    param.requires_grad = False

# nueva clase de capa lineal LoRA
class LoRALinear(nn.Module):
    def __init__(
            self, 
            in_features: int,
            out_features: int,
            pretrained_weight: torch.Tensor,
            pretrained_bias: torch.Tensor,
            r: int = 8,
            lora_alpha: int = 8,
            lora_dropout: float = 0.1,
            **kwargs
    ):
        super(LoRALinear, self).__init__()

        self.r = r
        self.in_features = in_features
        self.out_features = out_features
        self.lora_alpha = lora_alpha

        self.weight = nn.Parameter(pretrained_weight)
        self.weight.requires_grad = False

        if pretrained_bias is not None:
            self.bias = nn.Parameter(pretrained_bias)
            self.bias.requires_grad = False
        else:
            self.bias = None

        # de https://github.com/microsoft/LoRA/blob/main/loralib/layers.py
        self.lora_A = nn.Parameter(self.weight.new_zeros((r, in_features)))
        self.lora_B = nn.Parameter(self.weight.new_zeros((out_features, r)))
        self.scaling = self.lora_alpha / self.r
        self.lora_dropout = nn.Dropout(p=lora_dropout)
        
    def forward(self, x: torch.Tensor):
        result = F.linear(x, self.weight, bias=self.bias)
        result += (self.lora_dropout(x) @ self.lora_A.transpose(0, 1) @ self.lora_B.transpose(0, 1)) * self.scaling
        return result

# reemplazar capas lineales en el modelo recursivamente
def replace_linear_with_lora(module):
    for name, child in module.named_children():
        if isinstance(child, nn.Linear):
            setattr(module, name, LoRALinear(child.in_features, child.out_features, child.weight, child.bias))
        else:
            replace_linear_with_lora(child)

replace_linear_with_lora(model)



# summ = print_lora_params(model, LoRALinear)

# print("with function", summ)

# print("without function", sum(p.numel() for p in model.parameters() if p.requires_grad))


# inspeccionar nuevo modelo
# print(model)

# cargar conjunto de datos de chat
dataset_name = "timdettmers/openassistant-guanaco"
ft_dataset = load_dataset(dataset_name, split="train")

# entrenar modelo (bucle básico)
context_length = 768
loss_fn = CrossEntropyLoss()

learning_rate = 1e-4
optimizer = Adam(model.parameters(), lr=learning_rate)
num_epochs = 5

model = model.to("cuda")

### Entrenar el modelo
# Definir algunos argumentos de entrenamiento
args = transformers.TrainingArguments("/home/dnori/introtodeeplearning/xtra_labs/llm_finetune/outputs", 
    per_device_train_batch_size=1, 
    logging_first_step=True,
    logging_steps=20,
    save_steps=100,
)

# Definir un callback para verificar el progreso con una pregunta de ejemplo
class PrinterCallback(transformers.TrainerCallback):
    def on_log(self, args, state, control, model, logs=None, **kwargs):
        start_text = "### Human: When the weather is sunny, what color is the sky?### Assistant:"
        generate_pt(model, tokenizer, start_text, num_steps=200, until="###")

# Entrenar el modelo realmente
trainer = SFTTrainer(
    model,
    args=args,
    train_dataset=ft_dataset,
    dataset_text_field="text",
    max_seq_length=context_length,
    callbacks=[PrinterCallback()]
)
trainer.train()


# for epoch in range(num_epochs):
#     total_loss = 0
#     num_batches = 0

#     for batch in tqdm(ft_dataset):
#         prompt = batch["text"]
        
#         # codificar con el tokenizador
#         x = tokenizer.encode(prompt)
#         x_tensor = torch.tensor(x).view(1, -1).to("cuda")
#         max_len = min(context_length, x_tensor.shape[1]-1)
#         selected_len = random.randint(1,max_len)

#         input_tensor = x_tensor[:,:selected_len]
#         target_tensor = x_tensor[0,1:selected_len+1]

#          # poner gradientes a cero
#         optimizer.zero_grad()

#         # pasar por el modelo
#         logits = model(input_tensor).logits[0]

#         # aplicar la pérdida
#         loss = loss_fn(logits, target_tensor)

#         # retropropagación
#         loss.backward()

#         # paso del optimizador
#         optimizer.step()

#         total_loss += loss.item()
#         num_batches += 1

#     # Imprimir la pérdida promedio de la época
#     average_loss = total_loss / num_batches
#     print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {average_loss}")

# # evaluar modelo ajustado en el benchmark
# category_accs_1300m_ft, avg_acc_1300m_ft = run_benchmark(model, tokenizer, benchmark_dataset)

# agregar al gráfico de araña
# benchmark_data = {"350M-Model": category_accs_350m, "1300M-Model": category_accs_1300m, "1300M-Model-Finetuned": category_accs_1300m_ft, "2700M-Model": category_accs_2700m}
# benchmark_data = {"350M-Model": category_accs_1300m, "350M-Model-Finetuned": category_accs_1300m_ft}
# make_spider_plot(benchmark_data)