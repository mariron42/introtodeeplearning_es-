#!/usr/bin/env python3
"""
Add missing translations to the comprehensive script
"""

import re

# Read the current script
with open('translate_lab1_comprehensive.py', 'r') as f:
    script_content = f.read()

# Find the end of the current dictionary (before the closing })
dict_end_pattern = r'(\s+# ========== [A-Z\s]+ ==========.*?\n)(    }\n)'
match = re.search(r'(    # ========== .+ ==========.*?\n)(    }\n)', script_content, re.DOTALL)

if not match:
    print("Could not find dictionary end")
    exit(1)

# Additional comprehensive translations to add
additional_translations = '''        
        # ========== ADDITIONAL COMPREHENSIVE TRANSLATIONS ==========
        
        # Tensor shape and properties
        "As you have seen, the `shape` of a tensor provides the number of elements in each tensor dimension. The `shape` is quite useful, and we'll use it often. You can also use slicing to access subtensors within a higher-rank tensor:": "Como has visto, la `forma` de un tensor proporciona el número de elementos en cada dimensión del tensor. La `forma` es bastante útil, y la usaremos a menudo. También puedes usar slicing para acceder a subtensores dentro de un tensor de rango superior:",
        "As you have seen, the ```shape``` of a Tensor provides the number of elements in each Tensor dimension. The ```shape``` is quite useful, and we'll use it often. You can also use slicing to access subtensors within a higher-rank Tensor:": "Como has visto, la ```forma``` de un Tensor proporciona el número de elementos en cada dimensión del Tensor. La ```forma``` es bastante útil, y la usaremos a menudo. También puedes usar slicing para acceder a subtensors dentro de un Tensor de rango superior:",
        
        # Computations
        "A convenient way to think about and visualize computations in a machine learning framework like PyTorch is in terms of graphs. We can define this graph in terms of tensors, which hold data, and the mathematical operations that act on these tensors in some order. Let's look at a simple example, and define this computation using PyTorch:": "Una manera conveniente de pensar y visualizar los cálculos en un marco de aprendizaje automático como PyTorch es en términos de gráficos. Podemos definir este gráfico en términos de tensores, que contienen datos, y las operaciones matemáticas que actúan sobre estos tensores en algún orden. Veamos un ejemplo simple, y definamos este cálculo usando PyTorch:",
        "A convenient way to think about and visualize computations in a machine learning framework like TensorFlow is in terms of graphs. We can define this graph in terms of Tensors, which hold data, and the mathematical operations that act on these Tensors in some order. Let's look at a simple example, and define this computation using TensorFlow:": "Una manera conveniente de pensar y visualizar los cálculos en un marco de aprendizaje automático como TensorFlow es en términos de gráficos. Podemos definir este gráfico en términos de Tensores, que contienen datos, y las operaciones matemáticas que actúan sobre estos Tensores en algún orden. Veamos un ejemplo simple, y definamos este cálculo usando TensorFlow:",
        
        # Graph description
        "Here, we take two inputs, a, b, and compute an output e. Each node in the graph represents an operation that takes some input, does some computation, and passes its output to another node.": "Aquí, tomamos dos entradas, a, b, y calculamos una salida e. Cada nodo en el gráfico representa una operación que toma alguna entrada, realiza algún cálculo y pasa su salida a otro nodo.",
        
        # Notice patterns
        "Notice how we've created a computation graph consisting of PyTorch operations, and how the output is a tensor with value 76 -- we've just created a computation graph consisting of operations, and it's executed them and given us back the result.": "Observa cómo hemos creado un gráfico de cálculo que consiste en operaciones de PyTorch, y cómo la salida es un tensor con valor 76 -- acabamos de crear un gráfico de cálculo que consiste en operaciones, y las ha ejecutado y nos ha devuelto el resultado.",
        "Notice how we've created a computation graph consisting of TensorFlow operations, and how  the output is a Tensor with value 76 -- we've just created a computation graph consisting of operations, and it's executed them and given us back the result.": "Observa cómo hemos creado un gráfico de cálculo que consiste en operaciones de TensorFlow, y cómo la salida es un Tensor con valor 76 -- acabamos de crear un gráfico de cálculo que consiste en operaciones, y las ha ejecutado y nos ha devuelto el resultado.",
        
        # More complex example
        "Now let's consider a slightly more complicated example:": "Ahora consideremos un ejemplo un poco más complicado:",
        
        # Function definition
        "Let's define a simple function in PyTorch to construct this computation function:": "Definamos una función simple en PyTorch para construir esta función de cálculo:",
        "Let's define a simple function in TensorFlow to construct this computation function:": "Definamos una función simple en TensorFlow para construir esta función de cálculo:",
        
        # Calling the function
        "Now, we can call this function to execute the computation graph given some inputs `a,b`:": "Ahora, podemos llamar a esta función para ejecutar el gráfico de cálculo dadas algunas entradas `a,b`:",
        
        # Output description
        "Notice how our output is a tensor with value defined by the output of the computation, and that the output has no shape as it is a single scalar value.": "Observa cómo nuestra salida es un tensor con valor definido por la salida del cálculo, y que la salida no tiene forma ya que es un único valor escalar.",
        "Notice how our output is a Tensor with value defined by the output of the computation, and that the output has no shape as it is a single scalar value.": "Observa cómo nuestra salida es un Tensor con valor definido por la salida del cálculo, y que la salida no tiene forma ya que es un único valor escalar.",
        
        # Neural Networks section
        "We can also define neural networks in PyTorch. PyTorch uses ``torch.nn.Module``, which serves as a base class for all neural network modules in PyTorch. Layers and models in PyTorch inherit from this class.": "También podemos definir redes neuronales en PyTorch. PyTorch usa ``torch.nn.Module``, que sirve como clase base para todos los módulos de redes neuronales en PyTorch. Las capas y modelos en PyTorch heredan de esta clase.",
        "We can also define neural networks in TensorFlow. TensorFlow uses a high-level API called Keras that provides a powerful, intuitive framework for building and training deep learning models.": "También podemos definir redes neuronales en TensorFlow. TensorFlow usa una API de alto nivel llamada Keras que proporciona un marco poderoso e intuitivo para construir y entrenar modelos de aprendizaje profundo.",
        
        # Layers description
        "We will use `torch.nn.Module` to define layers -- the building blocks of neural networks. Layers implement common neural networks operations. In PyTorch, this class requires that you define a forward function, which describes the forward pass through the network.": "Usaremos `torch.nn.Module` para definir capas -- los bloques de construcción de las redes neuronales. Las capas implementan operaciones comunes de redes neuronales. En PyTorch, esta clase requiere que definas una función forward, que describe el paso hacia adelante a través de la red.",
        "Tensors can flow through abstract types called ```Layers``` -- the building blocks of neural networks. ```Layers``` implement common neural networks operations.": "Los tensores pueden fluir a través de tipos abstractos llamados ```Capas``` -- los bloques de construcción de las redes neuronales. Las ```Capas``` implementan operaciones comunes de redes neuronales.",
        
        # Perceptron
        "Let's consider the example of a simple perceptron defined by just one dense (aka fully-connected or linear) layer: $ y = \\sigma(Wx + b) $, where $W$ represents a matrix of weights, $b$ is a bias, $x$ is the input, and $\\sigma$ is a nonlinear activation function.": "Consideremos el ejemplo de un perceptrón simple definido por una sola capa densa (también conocida como totalmente conectada o lineal): $ y = \\sigma(Wx + b) $, donde $W$ representa una matriz de pesos, $b$ es un sesgo, $x$ es la entrada, y $\\sigma$ es una función de activación no lineal.",
        "Let's first consider the example of a simple perceptron defined by just one dense layer: $ y = \\sigma(Wx + b)$, where $W$ represents a matrix of weights, $b$ is a bias vector, $x$ is the input, and $\\sigma$ is a nonlinear activation function.": "Primero consideremos el ejemplo de un perceptrón simple definido por una sola capa densa: $ y = \\sigma(Wx + b)$, donde $W$ representa una matriz de pesos, $b$ es un vector de sesgo, $x$ es la entrada, y $\\sigma$ es una función de activación no lineal.",
        
        # Dense layer
        "We will use a \"dense\" ```Layer``` to illustrate this. The logic of this ```Layer``` will be identical to the ```OurDenseLayer``` we defined just now.": "Usaremos una ```Capa``` \"densa\" para ilustrar esto. La lógica de esta ```Capa``` será idéntica a la ```NuestraCapaDensa``` que acabamos de definir.",
        
        # Sequential API
        "Conveniently, PyTorch has defined a number of ```nn.Modules``` (or Layers) that are commonly used in neural networks, for example a ```nn.Linear``` layer. Now, instead of using a single ```Module``` to define our simple neural network, we'll use the  `nn.Sequential` module from PyTorch and a single `nn.Linear` layer to define our network.": "Convenientemente, PyTorch ha definido una serie de ```nn.Modules``` (o Capas) que se usan comúnmente en redes neuronales, por ejemplo una capa ```nn.Linear```. Ahora, en lugar de usar un solo ```Module``` para definir nuestra red neuronal simple, usaremos el módulo `nn.Sequential` de PyTorch y una sola capa `nn.Linear` para definir nuestra red.",
        "Convenientemente, TensorFlow has defined a number of ```Layers``` that are commonly used in neural networks, for example a ```Dense``` layer. Now, instead of using our ```OurDenseLayer```, we can use the ```Dense``` layer already provided from Keras:": "Convenientemente, TensorFlow ha definido una serie de ```Capas``` que se usan comúnmente en redes neuronales, por ejemplo una capa ```Dense```. Ahora, en lugar de usar nuestra ```NuestraCapaDensa```, podemos usar la capa ```Dense``` ya proporcionada por Keras:",
        
        # Sequential model
        "That's it! We've defined our model using the Sequential API. Now, we can test it out using an example input:": "¡Eso es todo! Hemos definido nuestro modelo usando la API Sequential. Ahora, podemos probarlo usando una entrada de ejemplo:",
        "Now, let's test the output of our layer using an example input:": "Ahora, probemos la salida de nuestra capa usando una entrada de ejemplo:",
        "Now, let's test the output of our layer.": "Ahora, probemos la salida de nuestra capa.",
        
        # Subclassing
        "In addition to defining models using the `Sequential` API, we can also define neural networks by directly subclassing the `Model` class, which groups layers together to enable model training and inference. The `Model` class has the same API as the `Layer` class. We'll actually use the `Model` class to define our model here because we have a single output.": "Además de definir modelos usando la API `Sequential`, también podemos definir redes neuronales heredando directamente de la clase `Model`, que agrupa capas para permitir el entrenamiento e inferencia del modelo. La clase `Model` tiene la misma API que la clase `Layer`. En realidad usaremos la clase `Model` para definir nuestro modelo aquí porque tenemos una sola salida.",
        "As we saw earlier with `OurDenseLayer`, we can subclass `nn.Module` to create a class for our model, and then define the forward pass through the network by calling the different layers on the input.": "Como vimos anteriormente con `NuestraCapaDensa`, podemos heredar de `nn.Module` para crear una clase para nuestro modelo, y luego definir el paso hacia adelante a través de la red llamando a las diferentes capas en la entrada.",
        
        # Test subclass model
        "Just like the model we built using the `Sequential` API, let's test out our `SubclassModel` using an example input.": "Al igual que el modelo que construimos usando la API `Sequential`, probemos nuestro `ModeloSubclasificado` usando una entrada de ejemplo.",
        
        # Custom behavior
        "Importantly, Subclassing affords us a lot of flexibility to define custom models. For example, we can use boolean arguments in the `call` function to specify different network behaviors, for example different behaviors during training and inference. Let's suppose under some instances we want our network to output a probability distribution over the outputs, and under other instances, we actually want to output the most probable output. We could achieve this as follows:": "Es importante destacar que la Subclasificación nos ofrece mucha flexibilidad para definir modelos personalizados. Por ejemplo, podemos usar argumentos booleanos en la función `call` para especificar diferentes comportamientos de red, por ejemplo diferentes comportamientos durante el entrenamiento y la inferencia. Supongamos que en algunas instancias queremos que nuestra red produzca una distribución de probabilidad sobre las salidas, y en otras instancias, realmente queremos producir la salida más probable. Podríamos lograr esto de la siguiente manera:",
        "Importantly, `nn.Module` affords us a lot of flexibility to define custom models. For example, we can use boolean arguments in the `forward` function to specify different network behaviors, for example different behaviors during training and inference. Let's suppose under some instances we want our network to return a probability distribution over the outputs, and under other instances we want to return the most probable output. To do this we can define a boolean argument that specifies this behavior:": "Es importante destacar que `nn.Module` nos ofrece mucha flexibilidad para definir modelos personalizados. Por ejemplo, podemos usar argumentos booleanos en la función `forward` para especificar diferentes comportamientos de red, por ejemplo diferentes comportamientos durante el entrenamiento y la inferencia. Supongamos que en algunas instancias queremos que nuestra red devuelva una distribución de probabilidad sobre las salidas, y en otras instancias queremos devolver la salida más probable. Para hacer esto podemos definir un argumento booleano que especifique este comportamiento:",
        
        # Ready for training
        "Now that we have learned how to define layers and models in PyTorch using both the Sequential API and subclassing `nn.Module`, we're ready to turn our attention to actually training these models!": "Ahora que hemos aprendido cómo definir capas y modelos en PyTorch usando tanto la API Sequential como heredando de `nn.Module`, ¡estamos listos para dirigir nuestra atención a entrenar realmente estos modelos!",
        "Now that we have learned how to define `Layers` as well as neural networks in TensorFlow using both the `Sequential` and Subclassing APIs, we're ready to shift our focus to actually training models!": "Ahora que hemos aprendido cómo definir `Capas` así como redes neuronales en TensorFlow usando tanto la API `Sequential` como de Subclasificación, ¡estamos listos para cambiar nuestro enfoque a entrenar realmente modelos!",
        
        # Automatic differentiation intro
        "In PyTorch, `torch.autograd` is used for automatic differentiation, which is critical for training deep learning models with backpropagation.": "En PyTorch, `torch.autograd` se usa para la diferenciación automática, que es crítica para entrenar modelos de aprendizaje profundo con retropropagación.",
        
        # Training overview
        "In training neural networks, we use differentiation and stochastic gradient descent (SGD) to optimize a loss function. Now that we have a sense of how PyTorch supports automatic differentiation, let's put everything together to train a neural network!": "En el entrenamiento de redes neuronales, usamos diferenciación y descenso de gradiente estocástico (SGD) para optimizar una función de pérdida. Ahora que tenemos una idea de cómo PyTorch soporta la diferenciación automática, ¡juntemos todo para entrenar una red neuronal!",
        "In training neural networks, we use differentiation and stochastic gradient descent (SGD) to optimize a loss function. Now that we have a sense of how `GradientTape` can be used to compute gradients, let's put everything together to train a neural network!": "En el entrenamiento de redes neuronales, usamos diferenciación y descenso de gradiente estocástico (SGD) para optimizar una función de pérdida. Ahora que tenemos una idea de cómo se puede usar `GradientTape` para calcular gradientes, ¡juntemos todo para entrenar una red neuronal!",
        
        # Final concepts
        "Now, we have covered the fundamental concepts of PyTorch -- tensors, operations, neural networks, and automatic differentiation. Fire!!": "Ahora, hemos cubierto los conceptos fundamentales de PyTorch -- tensores, operaciones, redes neuronales y diferenciación automática. ¡¡Fuego!!",
        "Now, we have covered the fundamental concepts of TensorFlow -- Tensors, computation graphs, neural networks, and automatic differentiation. Congrats!!": "Ahora, hemos cubierto los conceptos fundamentales de TensorFlow -- Tensores, gráficos de cálculo, redes neuronales y diferenciación automática. ¡¡Felicitaciones!!",
        
        # Miscellaneous phrases
        "and higher-rank Tensors. For examples, in future labs involving image processing and computer vision, we will use 4-d Tensors. Here the dimensions correspond to the number of example images in our batch, the image height, width, and color channel.": "y Tensores de rango superior. Por ejemplo, en futuros laboratorios que involucren procesamiento de imágenes y visión por computadora, usaremos Tensores 4-d. Aquí las dimensiones corresponden al número de imágenes de ejemplo en nuestro lote, la altura de la imagen, el ancho y el canal de color.",
        
        # Single words and short phrases (be careful with these)
        "and we'll use it often.": "y la usaremos a menudo.",
        "which hold data,": "que contienen datos,",
        "in some order.": "en algún orden.",
        "in terms of graphs.": "en términos de gráficos.",
        
'''

# Find where to insert (before the closing brace of the dictionary)
insertion_point = script_content.rfind('    }')

if insertion_point == -1:
    print("Could not find dictionary closing brace")
    exit(1)

# Insert the additional translations
new_script = script_content[:insertion_point] + additional_translations + script_content[insertion_point:]

# Write back
with open('translate_lab1_comprehensive.py', 'w') as f:
    f.write(new_script)

print("✓ Added comprehensive additional translations")
print(f"✓ Script now contains approximately {new_script.count('\":') + additional_translations.count('\":')} translations")

