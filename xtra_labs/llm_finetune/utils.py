"""
Contiene funciones con las que los estudiantes no interactuarán
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
import torch
import torch.nn.functional as F
from tqdm import tqdm

def run_benchmark(model, tokenizer, dataset, few_shot=7, num_steps=500, verbose=False):
    device = model.device
    dataset["Correct"] = 0.0

    # Recorrer cada pregunta en el benchmark
    for step, row in tqdm(dataset.iterrows(), total=len(dataset)):
        question = row['Question']
        pre_text = f"### Human: {question}### Assistant:"
        len_prefix = len(tokenizer.encode(pre_text))
        
        # Ejecutar el modelo individualmente con cada una de las cuatro respuestas. 
        # Medir la logprob del modelo para generar cada una de las cuatro respuestas. 
        # Elegir la respuesta con la mayor logprob
        logprobs = []
        answers = []
        for choice in ["A", "B", "C", "D"]: 
            answer = row[f'Answer {choice}']
            text = f"{pre_text} {answer}"

            # Ejecutar el modelo 
            with torch.no_grad():
                x = tokenizer.encode(text, return_tensors="pt").to(device)
                logits = model(x).logits
                probs = F.softmax(logits, dim=-1)[0, :-1, :]  # shape: [seq_len-1, vocab_size]
                y = x[0, 1:]  # shape: [seq_len-1]

            # Calcular la probabilidad logarítmica de que aparezca esta respuesta (logprob promedio sobre los tokens de la respuesta)
            next_token_prob = np.array([probs[i, y[i]].item() for i in range(y.shape[0])])
            num_ans_tokens = x.shape[1] - len_prefix
            logprob = np.mean(np.log(next_token_prob[-num_ans_tokens:]))
            logprobs.append(logprob)
            answers.append(answer)
        
        # Verificar la respuesta correcta (siempre el índice cero, por definición)
        correct = np.argmax(logprobs) == 0

        # Registrar si el modelo respondió correctamente o no. 
        # Opcionalmente imprimir la pregunta -> predicción si verbose está activado
        dataset.at[step, "Correct"] = float(correct)
        if verbose: 
            print(f"[{correct}] {question} -> {answers[np.argmax(logprobs)]}")

    
    # Agrupar por categorías y calcular la precisión promedio
    accs = dataset.groupby("Category")["Correct"].mean()
    sorted_accs = accs.sort_values()
    print(sorted_accs)

    return accs, dataset["Correct"].mean()

def make_spider_plot(data):
    """
    Data es un diccionario donde las claves son diferentes entidades
    Los valores son Series de pd donde los índices de la serie son las etiquetas del gráfico y los valores de la serie muestran el rendimiento
    """
    colors = ['#1aaf6c', '#429bf4', '#d42cea']
    i = 0
    fig, ax = plt.subplots(figsize=(8,6), subplot_kw=dict(polar=True))
    for k,v in data.items():
        labels = v.index.tolist()
        values = v.values.tolist()
        
        num_vars = len(labels)
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        angles += angles[:1]
        values += values[:1]
        
        ax.plot(angles, values, color=colors[i], linewidth=1, label=k)
        ax.fill(angles, values, color=colors[i], alpha=0.25)

        i+=1

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    for label, angle in zip(ax.get_xticklabels(), angles):
        if angle in (0, np.pi):
            label.set_horizontalalignment('center')
        elif 0 < angle < np.pi:
            label.set_horizontalalignment('left')
        else:
            label.set_horizontalalignment('right')

    ax.set_ylim(0, 1)
    ax.set_rlabel_position(180 / num_vars)

    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

    plt.savefig("spider.png")


        