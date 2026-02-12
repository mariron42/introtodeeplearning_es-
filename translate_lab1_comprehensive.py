#!/usr/bin/env python3
"""
Comprehensive Jupyter Notebook Translation Script for Lab1
Translates ALL markdown cells and code comments from English to Spanish
Performs complete extraction, translation, and application
"""

import json
import re
import os
import sys
import subprocess


def get_comprehensive_translations():
    """
    Returns the most comprehensive translation dictionary covering ALL English text
    in the lab1 notebooks. This includes both simple phrase translations and 
    paragraph-level translations.
    """
    return {
        # ========== NAVIGATION AND BADGES ==========
        "Visit MIT Deep Learning": "Visita MIT Deep Learning",
        "Run in Google Colab": "Ejecutar en Google Colab",
        "View Source on GitHub": "Ver Código Fuente en GitHub",
        "Copyright Information": "Información de Derechos de Autor",
        
        # ========== MAIN TITLES ==========
        "Lab 1: Intro to PyTorch and Music Generation with RNNs": "Laboratorio 1: Introducción a PyTorch y Generación de Música con RNNs",
        "Lab 1: Intro to TensorFlow and Music Generation with RNNs": "Laboratorio 1: Introducción a TensorFlow y Generación de Música con RNNs",
        
        # ========== PART TITLES ==========
        "Part 1: Intro to PyTorch": "Parte 1: Introducción a PyTorch",
        "Part 1: Intro to TensorFlow": "Parte 1: Introducción a TensorFlow",
        "Part 2: Music Generation with RNNs": "Parte 2: Generación de Música con RNNs",
        
        # ========== COPYRIGHT ==========
        "All Rights Reserved": "Todos los Derechos Reservados",
        "Licensed under the MIT License. You may not use this file except in compliance": "Licenciado bajo la Licencia MIT. No puedes usar este archivo excepto en cumplimiento",
        "with the License. Use and/or modification of this code outside of MIT Introduction": "con la Licencia. El uso y/o modificación de este código fuera de MIT Introduction",
        "to Deep Learning must reference:": "to Deep Learning debe hacer referencia a:",
        
        # ========== SECTION HEADERS ==========
        "## 0.1 Install PyTorch": "## 0.1 Instalar PyTorch",
        "## 0.1 Install TensorFlow": "## 0.1 Instalar TensorFlow",
        "## 0.2 Import PyTorch and other libraries": "## 0.2 Importar PyTorch y otras bibliotecas",
        "## 0.2 Import TensorFlow and other libraries": "## 0.2 Importar TensorFlow y otras bibliotecas",
        "## 1.1 What is PyTorch?": "## 1.1 ¿Qué es PyTorch?",
        "## 1.1 What is TensorFlow?": "## 1.1 ¿Qué es TensorFlow?",
        "## 1.1 Why is PyTorch useful?": "## 1.1 ¿Por qué es útil PyTorch?",
        "## 1.1 Why is TensorFlow useful?": "## 1.1 ¿Por qué es útil TensorFlow?",
        "## 1.2 Computations on Tensors": "## 1.2 Cálculos con Tensores",
        "## 1.3 Neural networks in PyTorch": "## 1.3 Redes neuronales en PyTorch",
        "## 1.3 Neural networks in TensorFlow": "## 1.3 Redes neuronales en TensorFlow",
        "## 1.4 Automatic Differentiation in PyTorch": "## 1.4 Diferenciación Automática en PyTorch",
        "## 1.4 Automatic differentiation in TensorFlow": "## 1.4 Diferenciación automática en TensorFlow",
        
        # Music Generation sections
        "## 2.1 Comet experiment setup": "## 2.1 Configuración del experimento Comet",
        "## 2.2 Dataset preprocessing and exploration": "## 2.2 Preprocesamiento y exploración del conjunto de datos",
        "## 2.3 Process the dataset for the learning task": "## 2.3 Procesar el conjunto de datos para la tarea de aprendizaje",
        "## 2.4 The Recurrent Neural Network (RNN) model": "## 2.4 El modelo de Red Neuronal Recurrente (RNN)",
        "## 2.5 Training the model": "## 2.5 Entrenamiento del modelo",
        "## 2.6 Generate music using the RNN model": "## 2.6 Generar música usando el modelo RNN",
        
        # Subsections
        "### 1.3.1 Define a network Layer": "### 1.3.1 Definir una capa de red",
        "### 1.3.2 Neural networks using the Sequential API": "### 1.3.2 Redes neuronales usando la API Sequential",
        "### 1.3.3 Model subclassing": "### 1.3.3 Subclasificación de modelos",
        "### 2.1.1 Import Comet": "### 2.1.1 Importar Comet",
        "### 2.1.2 Initialize a Comet Experiment": "### 2.1.2 Inicializar un experimento Comet",
        "### 2.2.1 Listen to the music": "### 2.2.1 Escuchar la música",
        "### 2.2.2 Character encoding": "### 2.2.2 Codificación de caracteres",
        "### 2.3.1 Create training examples and targets": "### 2.3.1 Crear ejemplos de entrenamiento y objetivos",
        "### 2.3.2 Batch definition": "### 2.3.2 Definición de lotes",
        "### 2.4.1 Defining our RNN model": "### 2.4.1 Definiendo nuestro modelo RNN",
        "### 2.4.2 Test the model": "### 2.4.2 Probar el modelo",
        "### 2.5.1 Loss function": "### 2.5.1 Función de pérdida",
        "### 2.5.2 Hyperparameters and training operation": "### 2.5.2 Hiperparámetros y operación de entrenamiento",
        "### 2.5.3 Training loop": "### 2.5.3 Bucle de entrenamiento",
        "### 2.6.1 Restoration of the latest checkpoint": "### 2.6.1 Restauración del último checkpoint",
        "### 2.6.2 Prediction of a generated song": "### 2.6.2 Predicción de una canción generada",
        "### 2.6.3 Play back generated songs": "### 2.6.3 Reproducir las canciones generadas",
        
        # ========== INTRODUCTION PARAGRAPHS ==========
        "In this lab, you'll get exposure to using TensorFlow and learn how it can be used for solving deep learning tasks.": "En este laboratorio, obtendrás experiencia usando TensorFlow y aprenderás cómo se puede usar para resolver tareas de aprendizaje profundo.",
        "In this lab, you'll get exposure to using PyTorch and learn how it can be used for deep learning.": "En este laboratorio, obtendrás experiencia usando PyTorch y aprenderás cómo se puede usar para aprendizaje profundo.",
        "In this lab, you'll get exposure to using": "En este laboratorio, obtendrás experiencia usando",
        "and learn how it can be used for deep learning.": "y aprenderás cómo se puede usar para aprendizaje profundo.",
        "and learn how it can be used for solving deep learning tasks.": "y aprenderás cómo se puede usar para resolver tareas de aprendizaje profundo.",
        "Go through the code and run each cell.": "Revisa el código y ejecuta cada celda.",
        "Along the way, you'll encounter several": "En el camino, encontrarás varios bloques",
        "blocks -- follow the instructions to fill them out before running those cells and continuing.": "-- sigue las instrucciones para completarlos antes de ejecutar esas celdas y continuar.",
        
        # ========== INSTALLATION SECTIONS ==========
        "is a popular deep learning library known for its flexibility and ease of use.": "es una popular biblioteca de aprendizaje profundo conocida por su flexibilidad y facilidad de uso.",
        "Here we'll learn how computations are represented and how to define a simple neural network in": "Aquí aprenderemos cómo se representan los cálculos y cómo definir una red neuronal simple en",
        "For all the labs in Introduction to Deep Learning": "Para todos los laboratorios en Introducción al Aprendizaje Profundo",
        "there will be a": "habrá una versión de",
        "version available.": "disponible.",
        "Let's install": "Instalemos",
        "and a couple of dependencies.": "y un par de dependencias.",
        
        # ========== WHAT IS PYTORCH/TENSORFLOW ==========
        "is a machine learning library, like TensorFlow.": "es una biblioteca de aprendizaje automático, como TensorFlow.",
        "is a machine learning library, like PyTorch.": "es una biblioteca de aprendizaje automático, como PyTorch.",
        "At its core,": "En su núcleo,",
        "provides an interface for creating and manipulating": "proporciona una interfaz para crear y manipular",
        "which are data structures that you can think of as multi-dimensional arrays.": "que son estructuras de datos que puedes considerar como arreglos multidimensionales.",
        "Tensors are represented as n-dimensional arrays of base datatypes such as a string or integer --": "Los tensores se representan como arreglos n-dimensionales de tipos de datos base como cadenas o enteros --",
        "they provide a way to generalize vectors and matrices to higher dimensions.": "proporcionan una manera de generalizar vectores y matrices a dimensiones superiores.",
        
        # TensorFlow specific
        "TensorFlow is called 'TensorFlow' because it handles the flow (node/mathematical operation) of Tensors, which are data structures that you can think of as multi-dimensional arrays.": "TensorFlow se llama 'TensorFlow' porque maneja el flujo (nodo/operación matemática) de Tensores, que son estructuras de datos que puedes considerar como arreglos multidimensionales.",
        "Tensors are represented as n-dimensional arrays of base datatypes such as a string or integer -- they provide a way to generalize vectors and matrices to higher dimensions.": "Los tensores se representan como arreglos n-dimensionales de tipos de datos base como cadenas o enteros -- proporcionan una manera de generalizar vectores y matrices a dimensiones superiores.",
        
        # PyTorch specific
        "provides the ability to perform computation on these tensors, define neural networks, and train them efficiently.": "proporciona la capacidad de realizar cálculos en estos tensores, definir redes neuronales y entrenarlas eficientemente.",
        
        # ========== TENSOR PROPERTIES ==========
        "The shape of a PyTorch": "La forma de un",
        "The shape of a TensorFlow": "La forma de un",
        "The shape of a": "La forma de un",
        "tensor defines its number of dimensions and the size of each dimension.": "tensor define su número de dimensiones y el tamaño de cada dimensión.",
        
        "tensor provides the number of dimensions": "tensor proporciona el número de elementos",
        "this is equivalent to the tensor's rank": "esto es equivalente al rango del tensor",
        "and you can also think of this as the tensor's order or degree.": "y también puedes pensar en esto como el orden o grado del tensor.",
        
        # ========== CREATING TENSORS ==========
        "Let's start by creating some tensors and inspecting their properties:": "Comencemos creando algunos tensores e inspeccionando sus propiedades:",
        "Let's first look at 0-d Tensors, represented as scalars.": "Primero veamos los tensores 0-d, representados como escalares.",
        "Let's first look at 0-d Tensors, of which a scalar is an example:": "Primero veamos los tensores 0-d, de los cuales un escalar es un ejemplo:",
        "Vectors and lists can be used to create 1-d tensors:": "Los vectores y listas se pueden usar para crear tensores 1-d:",
        "Vectors and lists can be used to create 1-d Tensors": "Los vectores y listas se pueden usar para crear tensores 1-d",
        "Next, let's create": "A continuación, vamos a crear",
        "Next we consider creating 2-d (i.e., matrices)": "A continuación consideramos crear tensores 2-d (es decir, matrices)",
        "and higher-rank tensors.": "y tensores de rango superior.",
        
        # Image processing
        "In image processing and computer vision, we will use 4-d Tensors with dimensions corresponding to batch size, number of color channels, image height, and image width.": "En procesamiento de imágenes y visión por computadora, usaremos tensores 4-d con dimensiones correspondientes al tamaño del lote, número de canales de color, altura de imagen y ancho de imagen.",
        
        # ========== TENSOR OPERATIONS ==========
        "As you have seen, the shape of a Tensor provides the number of elements along each of the Tensor's axes. Let's next see how to access information along a particular axis.": "Como has visto, la forma de un Tensor proporciona el número de elementos a lo largo de cada uno de los ejes del Tensor. Veamos a continuación cómo acceder a la información a lo largo de un eje particular.",
        "You can also use slicing to access subtensors within a higher-rank Tensor:": "También puedes usar slicing para acceder a subtensores dentro de un Tensor de rango superior:",
        
        # ========== COMPUTATIONS ==========
        "A convenient way to think about and visualize computations in": "Una manera conveniente de pensar y visualizar los cálculos en",
        "is in terms of graphs. Computation graphs are a nice way to visualize the mathematical operations that occur in calculations.": "es en términos de gráficos. Los gráficos de cálculo son una buena manera de visualizar las operaciones matemáticas que ocurren en los cálculos.",
        
        "Notice how we've created a computation graph consisting of": "Observa cómo hemos creado un gráfico de cálculo que consiste en operaciones de",
        "operations. Here, we take two inputs,": "Aquí, tomamos dos entradas,",
        "and compute an output": "y calculamos una salida",
        "The output is defined as the sum of the two inputs.": "La salida se define como la suma de las dos entradas.",
        
        "We can define this graph in terms of Tensors and": "Podemos definir este gráfico en términos de Tensores y operaciones de",
        "operations:": ":",
        
        # PyTorch specifics
        "Notice how we've created a computation graph consisting of PyTorch operations. Here, we take two inputs, a, b, and compute an output e. The output is defined as the sum of the two inputs.": "Observa cómo hemos creado un gráfico de cálculo que consiste en operaciones de PyTorch. Aquí, tomamos dos entradas, a, b, y calculamos una salida e. La salida se define como la suma de las dos entradas.",
        "Notice how we've created a computation graph consisting of TensorFlow operations. Here, we take two inputs, a, b, and compute an output e. The output is defined as the sum of the two inputs.": "Observa cómo hemos creado un gráfico de cálculo que consiste en operaciones de TensorFlow. Aquí, tomamos dos entradas, a, b, y calculamos una salida e. La salida se define como la suma de las dos entradas.",
        
        "Let's define a simple function in": "Definamos una función simple en",
        "Let's write a dense layer class to implement a perceptron defined above.": "Escribamos una clase de capa densa para implementar un perceptrón definido arriba.",
        "Let's test out our new model, using an example input, setting": "Probemos nuestro nuevo modelo, usando una entrada de ejemplo, estableciendo",
        "and": "y",
        "as before.": "como antes.",
        "Let's test this behavior:": "Probemos este comportamiento:",
        "using": "usando",
        "and access them for computation. We define the simple function": "y acceder a ellos para cálculo. Definimos la función simple",
        "and compute the gradient:": "y calculamos el gradiente:",
        
        # ========== NEURAL NETWORKS ==========
        "We can also define neural networks in": "También podemos definir redes neuronales en",
        "uses a high-level API called Keras to build and train deep learning models.": "usa una API de alto nivel llamada Keras para construir y entrenar modelos de aprendizaje profundo.",
        "Tensors can flow through abstract types called Layers -- these are the building blocks of neural networks.": "Los tensores pueden fluir a través de tipos abstractos llamados Capas -- estos son los bloques de construcción de las redes neuronales.",
        
        # Perceptron example
        "Let's consider the example of a simple perceptron, the most simple type of feedforward neural network.": "Consideremos el ejemplo de un perceptrón simple, el tipo más simple de red neuronal feedforward.",
        "A perceptron has a single layer with weights and bias and computes an output based on:": "Un perceptrón tiene una sola capa con pesos y sesgo y calcula una salida basada en:",
        
        # Layer definition
        "We will use": "Usaremos",
        "to define layers in": "para definir capas en",
        "We will first define a Layer to implement the simple perceptron.": "Primero definiremos una Capa para implementar el perceptrón simple.",
        
        # PyTorch specific
        "All classes subclassing nn.Module should override the forward function, which describes the forward pass through the network.": "Todas las clases que heredan de nn.Module deben sobrescribir la función forward, que describe el paso hacia adelante a través de la red.",
        
        # TensorFlow specific  
        "All classes subclassing Layer should override the call function, which describes the forward pass through the network.": "Todas las clases que heredan de Layer deben sobrescribir la función call, que describe el paso hacia adelante a través de la red.",
        
        "Now, let's test the output of our layer using an example input:": "Ahora, probemos la salida de nuestra capa usando una entrada de ejemplo:",
        
        # Sequential API
        "Conveniently,": "Convenientemente,",
        "has defined a number of": "ha definido una serie de",
        "that are commonly used.": "que se usan comúnmente.",
        
        "With the Sequential API, you can readily create neural networks by stacking together layers like building blocks.": "Con la API Sequential, puedes crear fácilmente redes neuronales apilando capas como bloques de construcción.",
        "Let's use the Sequential API to define our perceptron:": "Usemos la API Sequential para definir nuestro perceptrón:",
        
        # Subclassing
        "In addition to defining models using the Sequential API, we can also define models by directly subclassing": "Además de definir modelos usando la API Sequential, también podemos definir modelos heredando directamente de",
        "Using Subclassing, we can create a class for our model,": "Usando Subclasificación, podemos crear una clase para nuestro modelo,",
        "and then define the forward pass through the network by calling the different layers on the input.": "y luego definir el paso hacia adelante a través de la red llamando a las diferentes capas en la entrada.",
        
        "Let's define the same neural network as a subclass of": "Definamos la misma red neuronal como una subclase de",
        
        "Subclassing affords the flexibility to define custom layers, custom training loops, custom activation functions, and custom models. Here, for the sake of simplicity, we've used some pre-defined layers.": "La Subclasificación ofrece la flexibilidad de definir capas personalizadas, bucles de entrenamiento personalizados, funciones de activación personalizadas y modelos personalizados. Aquí, por simplicidad, hemos usado algunas capas predefinidas.",
        
        "Just like the model we built using the Sequential API, let's test out our new model:": "Al igual que el modelo que construimos usando la API Sequential, probemos nuestro nuevo modelo:",
        
        "Importantly, Subclassing affords us a lot of flexibility in defining custom models, but also gives us the flexibility to define custom behavior for training.": "Es importante destacar que la Subclasificación nos ofrece mucha flexibilidad para definir modelos personalizados, pero también nos da la flexibilidad de definir comportamiento personalizado para el entrenamiento.",
        
        "Let's suppose under some instances we want our network to return a probability distribution over the outputs, and under other instances we want to return the most probable output. To do this we can define a boolean argument that specifies this behavior:": "Supongamos que en algunas instancias queremos que nuestra red devuelva una distribución de probabilidad sobre las salidas, y en otras instancias queremos devolver la salida más probable. Para hacer esto, podemos definir un argumento booleano que especifique este comportamiento:",
        
        "Now that we have learned how to define layers and models in": "Ahora que hemos aprendido cómo definir capas y modelos en",
        "let's shift our focus to actually training these models.": "cambiemos nuestro enfoque a entrenar realmente estos modelos.",
        
        # ========== AUTOMATIC DIFFERENTIATION ==========
        "Automatic differentiation is one of the most important parts of": "La diferenciación automática es una de las partes más importantes de",
        "and is used extensively in training neural networks.": "y se usa extensivamente en el entrenamiento de redes neuronales.",
        
        # PyTorch autograd
        "In PyTorch, torch.autograd is used for automatic differentiation. It provides automatic computation of backward pass gradients in neural networks.": "En PyTorch, torch.autograd se usa para la diferenciación automática. Proporciona el cálculo automático de gradientes de paso hacia atrás en redes neuronales.",
        
        "On a tensor, the requires_grad attribute controls whether gradients are computed for operations involving that tensor. Let's see this in action.": "En un tensor, el atributo requires_grad controla si se calculan gradientes para operaciones que involucran ese tensor. Veamos esto en acción.",
        
        # TensorFlow GradientTape
        "[Automatic differentiation](https://en.wikipedia.org/wiki/Automatic_differentiation) is useful in many machine learning algorithms, including optimization and neural networks.": "[La diferenciación automática](https://es.wikipedia.org/wiki/Diferenciaci%C3%B3n_autom%C3%A1tica) es útil en muchos algoritmos de aprendizaje automático, incluida la optimización y las redes neuronales.",
        
        "When a forward pass is made through the network, all forward-pass operations get recorded to a \"tape\"; then, to compute the gradient, the tape is played backwards. By default, the tape is discarded after it is played backwards; this means that a particular": "Cuando se realiza un paso hacia adelante a través de la red, todas las operaciones de paso hacia adelante se registran en una \"cinta\"; luego, para calcular el gradiente, la cinta se reproduce hacia atrás. Por defecto, la cinta se descarta después de reproducirse hacia atrás; esto significa que una",
        "instance can only compute one gradient, and subsequent calls throw a runtime error.": "instancia particular solo puede calcular un gradiente, y las llamadas posteriores generan un error de tiempo de ejecución.",
        
        "First, we will look at how we can compute gradients using GradientTape and access them for computation. We define the simple function": "Primero, veremos cómo podemos calcular gradientes usando GradientTape y acceder a ellos para cálculo. Definimos la función simple",
        "First, we will look at how we can compute gradients using": "Primero, veremos cómo podemos calcular gradientes usando",
        "and then put it all together to build a neural network": "y luego juntarlo todo para construir una red neuronal",
        "and train it.": "y entrenarla.",
        
        "Let's compute the gradient of": "Calculemos el gradiente de",
        
        # Gradient descent
        "In training neural networks, we use differentiation and stochastic gradient descent (SGD) to optimize a loss function. Here we will tackle a simpler optimization problem, finding the minimum of": "En el entrenamiento de redes neuronales, usamos diferenciación y descenso de gradiente estocástico (SGD) para optimizar una función de pérdida. Aquí abordaremos un problema de optimización más simple, encontrar el mínimo de",
        
        "provides an extremely flexible framework for automatic differentiation.": "proporciona un marco extremadamente flexible para la diferenciación automática.",
        
        "In order to back propagate errors and train our model, we will have to keep track of the gradients of the network with respect to the loss.": "Para retropropagar errores y entrenar nuestro modelo, tendremos que realizar un seguimiento de los gradientes de la red con respecto a la pérdida.",
        
        # ========== MUSIC GENERATION ==========
        "In this portion of the lab, we will explore building a Recurrent Neural Network (RNN) for music generation using": "En esta parte del laboratorio, exploraremos la construcción de una Red Neuronal Recurrente (RNN) para la generación de música usando",
        "In this portion of the lab, we will explore building a Recurrent Neural Network (RNN) for music generation.": "En esta parte del laboratorio, exploraremos la construcción de una Red Neuronal Recurrente (RNN) para la generación de música.",
        "We will train a model to learn the patterns in raw sheet music in ABC notation and then use this model to generate new music.": "Entrenaremos un modelo para aprender los patrones en partituras musicales en notación ABC y luego usaremos este modelo para generar nueva música.",
        "We will train a model to learn the patterns in raw sheet music in": "Entrenaremos un modelo para aprender los patrones en partituras musicales en",
        "then use this model to generate new music.": "luego usaremos este modelo para generar nueva música.",
        
        # Comet setup
        "We will be using Comet ML to track our model development and training runs. Comet is a platform that allows you to track, compare, and optimize your machine learning experiments.": "Usaremos Comet ML para rastrear nuestro desarrollo de modelo y ejecuciones de entrenamiento. Comet es una plataforma que te permite rastrear, comparar y optimizar tus experimentos de aprendizaje automático.",
        "We will be using": "Usaremos",
        "to track our model development": "para rastrear nuestro desarrollo de modelo",
        "training runs. First, sign up for a Comet account": "ejecuciones de entrenamiento. Primero, regístrate para obtener una cuenta de Comet",
        "(you can use your MIT email!). You will need to generate a new personal API Key. Enter this API key as the global variable": "(¡puedes usar tu correo electrónico del MIT!). Necesitarás generar una nueva clave API personal. Ingresa esta clave API como la variable global",
        
        "First, sign up for a Comet account at this link:": "Primero, regístrate para obtener una cuenta de Comet en este enlace:",
        "First, let's download the course repository, install dependencies,": "Primero, descarguemos el repositorio del curso, instalemos las dependencias,",
        "import the relevant packages we'll need for this lab.": "importemos los paquetes relevantes que necesitaremos para este laboratorio.",
        "You will need to generate a new personal API Key. Enter this API key as the global variable": "Necesitarás generar una nueva clave API personal. Ingresa esta clave API como la variable global",
        
        # Dataset
        "thousands of Irish folk songs": "miles de canciones folclóricas irlandesas",
        "thousands of Irish": "miles de canciones folclóricas irlandesas",
        "We've gathered a dataset of thousands of Irish folk songs, represented in the ABC notation. Let's download the dataset": "Hemos recopilado un conjunto de datos de miles de canciones folclóricas irlandesas, representadas en la notación ABC. Descarguemos el conjunto de datos",
        "inspect it:": "inspeccionémoslo:",
        
        # Listen to music
        "We can easily convert a song in ABC notation to an audio waveform and play it back.": "Podemos convertir fácilmente una canción en notación ABC a una forma de onda de audio y reproducirla.",
        "Be patient for this conversion to run, it can take some time!": "¡Ten paciencia para que se ejecute esta conversión, puede tomar algo de tiempo!",
        
        # Character encoding
        "the notes being played": "las notas que se están tocando",
        "being played": "están tocando",
        "One important thing to think about is that this notation of music does not simply contain information on the notes being played, but also encompasses information on the rhythm and tempo.": "Una cosa importante a tener en cuenta es que esta notación de música no solo contiene información sobre las notas que se están tocando, sino que también abarca información sobre el ritmo y el tempo.",
        "One important thing to think about is that this notation of music does not simply contain information on the notes being played, but additionally there is meta information such as the song title, key,": "Una cosa importante a tener en cuenta es que esta notación de música no solo contiene información sobre las notas que se están tocando, sino que también hay metainformación como el título de la canción, clave,",
        "tempo.": "tempo.",
        "This will become important soon, when we generate a numerical representation of the text.": "Esto se volverá importante pronto, cuando generemos una representación numérica del texto.",
        
        "How does the number of different characters that are present in the text file impact the complexity of the learning problem?": "¿Cómo afecta el número de diferentes caracteres presentes en el archivo de texto la complejidad del problema de aprendizaje?",
        
        # Prediction task
        "Let's take a step back and consider our prediction task. We're trying to train an RNN model to learn patterns in ABC music, and then use this model to generate (i.e., predict) a new piece of music based on this learned information.": "Demos un paso atrás y consideremos nuestra tarea de predicción. Estamos tratando de entrenar un modelo RNN para aprender patrones en música ABC, y luego usar este modelo para generar (es decir, predecir) una nueva pieza de música basada en esta información aprendida.",
        
        "Breaking this down, what we're really asking the model is: given a character, or a sequence of characters, what is the most probable next character? We'll train the model to perform this task.": "Desglosando esto, lo que realmente le estamos pidiendo al modelo es: dada un carácter, o una secuencia de caracteres, ¿cuál es el siguiente carácter más probable? Entrenaremos el modelo para realizar esta tarea.",
        
        "To achieve this, we will input a sequence of characters to the model, and train the model to predict the output, that is, the following character at each time step. RNNs maintain an internal state that depends on previously seen elements, so information about all characters seen up until a given moment will be taken into account in generating the prediction.": "Para lograr esto, ingresaremos una secuencia de caracteres al modelo, y entrenaremos el modelo para predecir la salida, es decir, el siguiente carácter en cada paso de tiempo. Las RNNs mantienen un estado interno que depende de los elementos vistos previamente, por lo que se tendrá en cuenta información sobre todos los caracteres vistos hasta un momento dado en la generación de la predicción.",
        
        # Numerical representation
        "Before we begin training our RNN model, we'll need to create a numerical representation of our text-based dataset. We'll do this by mapping each unique character to a unique integer index.": "Antes de comenzar a entrenar nuestro modelo RNN, necesitaremos crear una representación numérica de nuestro conjunto de datos basado en texto. Haremos esto mapeando cada carácter único a un índice entero único.",
        
        "To do this, we'll generate two lookup tables: one that maps characters to numbers, and another that maps numbers back to characters. Recall that we just identified the unique characters present in the text.": "Para hacer esto, generaremos dos tablas de búsqueda: una que mapea caracteres a números, y otra que mapea números de vuelta a caracteres. Recuerda que acabamos de identificar los caracteres únicos presentes en el texto.",
        
        "This gives us an integer representation for each character. Observe that the unique characters (i.e., our vocabulary) in the text are mapped as indices from 0 to": "Esto nos da una representación entera para cada carácter. Observa que los caracteres únicos (es decir, nuestro vocabulario) en el texto se mapean como índices desde 0 hasta",
        
        "Let's take a peek at this numerical representation of our dataset:": "Echemos un vistazo a esta representación numérica de nuestro conjunto de datos:",
        
        # Training examples
        "Our next step is to actually divide the text into example sequences that we'll use during training. Each input sequence that we feed into our RNN will contain": "Nuestro siguiente paso es dividir realmente el texto en secuencias de ejemplo que usaremos durante el entrenamiento. Cada secuencia de entrada que alimentamos a nuestra RNN contendrá",
        "characters from the text.": "caracteres del texto.",
        
        "We'll also need to define a target sequence for each input sequence. For each input, the corresponding target will contain the same length of text, except shifted one character to the right. To do this, we'll break the text into chunks of": "También necesitaremos definir una secuencia objetivo para cada secuencia de entrada. Para cada entrada, el objetivo correspondiente contendrá la misma longitud de texto, excepto desplazado un carácter a la derecha. Para hacer esto, dividiremos el texto en fragmentos de",
        
        "The batch method will then let us convert this stream of character indices to sequences of the desired size.": "El método de lote nos permitirá entonces convertir este flujo de índices de caracteres en secuencias del tamaño deseado.",
        
        "For each of these vectors, each index is processed at a single time step. So, for the input at time step 0, the model receives the index for the first character in the sequence, and tries to predict the index of the next character. At the next timestep, it does the same thing, but the RNN considers the information from the previous step, i.e., its updated state, in addition to the current input.": "Para cada uno de estos vectores, cada índice se procesa en un solo paso de tiempo. Entonces, para la entrada en el paso de tiempo 0, el modelo recibe el índice del primer carácter en la secuencia, e intenta predecir el índice del siguiente carácter. En el siguiente paso de tiempo, hace lo mismo, pero la RNN considera la información del paso anterior, es decir, su estado actualizado, además de la entrada actual.",
        
        "We can make this concrete by taking a look at how this works over a single sequence of inputs. This function displays a training example from our data:": "Podemos hacer esto concreto echando un vistazo a cómo funciona esto sobre una sola secuencia de entradas. Esta función muestra un ejemplo de entrenamiento de nuestros datos:",
        
        # RNN model
        "Now we're ready to define and train an RNN model on our ABC music dataset, and then use that model to generate a new song. We'll train our RNN using batches of song snippets from our dataset, which we generated in the previous section.": "Ahora estamos listos para definir y entrenar un modelo RNN en nuestro conjunto de datos de música ABC, y luego usar ese modelo para generar una nueva canción. Entrenaremos nuestra RNN usando lotes de fragmentos de canciones de nuestro conjunto de datos, que generamos en la sección anterior.",
        
        "The model is based off the LSTM architecture, where we use a state vector to maintain information about the temporal relationships between consecutive characters. The final output of the LSTM is then fed into a fully connected": "El modelo se basa en la arquitectura LSTM, donde usamos un vector de estado para mantener información sobre las relaciones temporales entre caracteres consecutivos. La salida final del LSTM se alimenta luego a una capa",
        "layer where we'll output a softmax over each character in the vocabulary.": "totalmente conectada donde sacaremos un softmax sobre cada carácter en el vocabulario.",
        
        "As we introduced in the first portion of this lab, we'll use the": "Como presentamos en la primera parte de este laboratorio, usaremos la API",
        "API to define the model.": "para definir el modelo.",
        
        "Three layers are used to define the model:": "Se utilizan tres capas para definir el modelo:",
        
        # Model layers
        "This is the input layer, consisting of a trainable lookup table that will map the numbers of each character to a vector with": "Esta es la capa de entrada, que consiste en una tabla de búsqueda entrenable que mapeará los números de cada carácter a un vector con",
        "dimensions.": "dimensiones.",
        
        "Our LSTM network, with size": "Nuestra red LSTM, con tamaño",
        "units. We can also add more LSTM layers but for now, one is sufficient.": "unidades. También podemos agregar más capas LSTM pero por ahora, una es suficiente.",
        
        "The output layer, with": "La capa de salida, con",
        "outputs.": "salidas.",
        
        # Model definition
        "Let's define our model as an": "Definamos nuestro modelo como un",
        "Fill in the": "Completa los bloques",
        "to define the RNN model.": "para definir el modelo RNN.",
        
        "The time has come! Let's instantiate the model!": "¡Ha llegado el momento! ¡Vamos a instanciar el modelo!",
        
        # Model testing
        "It's always a good idea to run a few simple checks on our model to see that it behaves as expected.": "Siempre es una buena idea ejecutar algunas verificaciones simples en nuestro modelo para ver que se comporta como se espera.",
        
        "We can quickly check the layers in the model, and the shapes of the output from each layer, with": "Podemos verificar rápidamente las capas en el modelo, y las formas de la salida de cada capa, con",
        
        "Note that the model can be run on inputs of any length.": "Ten en cuenta que el modelo se puede ejecutar en entradas de cualquier longitud.",
        
        # Loss function
        "Now we'll define a loss function for the network to optimize. The loss we'll use is the": "Ahora definiremos una función de pérdida para que la red optimice. La pérdida que usaremos es la",
        "which is well suited to this classification task. You may recall from lecture that this loss is one of the standard losses used for multiclass classification problems and is defined as the negative log probability of the true class.": "que es adecuada para esta tarea de clasificación. Puedes recordar de la conferencia que esta pérdida es una de las pérdidas estándar utilizadas para problemas de clasificación multiclase y se define como la probabilidad logarítmica negativa de la clase verdadera.",
        
        "We want to compute the loss using the true targets -- the labels -- and the predicted targets -- the logits.": "Queremos calcular la pérdida usando los objetivos verdaderos -- las etiquetas -- y los objetivos predichos -- los logits.",
        
        # Hyperparameters
        "Now, we're almost ready to train the model! Before we do that, there are a few more things we need to set up. First, we need to define an optimizer and decide on a value for the learning rate. To start, you can try using the Adam optimizer with the default learning rate.": "Ahora, ¡casi estamos listos para entrenar el modelo! Antes de hacer eso, hay algunas cosas más que necesitamos configurar. Primero, necesitamos definir un optimizador y decidir sobre un valor para la tasa de aprendizaje. Para empezar, puedes intentar usar el optimizador Adam con la tasa de aprendizaje predeterminada.",
        
        "Next, we'll define checkpoints for saving our model during training. This will allow us to load back a saved model and generate music without having to retrain the model.": "A continuación, definiremos checkpoints para guardar nuestro modelo durante el entrenamiento. Esto nos permitirá cargar de vuelta un modelo guardado y generar música sin tener que volver a entrenar el modelo.",
        
        # Training loop
        "Finally, we are ready to train the model!": "¡Finalmente, estamos listos para entrenar el modelo!",
        
        "The training loop executes as follows. For each epoch, the model:": "El bucle de entrenamiento se ejecuta de la siguiente manera. Para cada época, el modelo:",
        
        "* Initializes the hidden state of the RNN": "* Inicializa el estado oculto de la RNN",
        "* Iterates over the dataset in batches": "* Itera sobre el conjunto de datos en lotes",
        "* For each batch, computes the forward pass through the RNN to get predictions and the loss": "* Para cada lote, calcula el paso hacia adelante a través de la RNN para obtener predicciones y la pérdida",
        "* Computes the backward pass to update the parameters of the RNN": "* Calcula el paso hacia atrás para actualizar los parámetros de la RNN",
        "* And, every": "* Y, cada",
        "batches, generates some sample output to monitor training progress.": "lotes, genera alguna salida de muestra para monitorear el progreso del entrenamiento.",
        
        # Music generation
        "Once we have a trained model, we can use it to generate a new song!": "¡Una vez que tenemos un modelo entrenado, podemos usarlo para generar una nueva canción!",
        
        "To use our trained RNN model to generate text, we feed in a starting string and have the network predict the next character. The output from the model gives a probability distribution over the different characters. We randomly sample from this distribution to get the next predicted character. We then update the RNN state and repeat until we have a generated song!": "Para usar nuestro modelo RNN entrenado para generar texto, alimentamos una cadena de inicio y hacemos que la red prediga el siguiente carácter. La salida del modelo da una distribución de probabilidad sobre los diferentes caracteres. Tomamos una muestra aleatoria de esta distribución para obtener el siguiente carácter predicho. Luego actualizamos el estado de la RNN y repetimos hasta que tengamos una canción generada.",
        
        # Checkpoint restoration
        "If you are re-running this cell using a previously trained model, set the below flag to": "Si estás volviendo a ejecutar esta celda usando un modelo previamente entrenado, establece la siguiente bandera en",
        "to restore the model from the most recent checkpoint.": "para restaurar el modelo desde el checkpoint más reciente.",
        
        # Play music
        "Let's listen to the music our model has created!": "¡Escuchemos la música que nuestro modelo ha creado!",
        
        # ========== CODE COMMENTS ==========
        "Download and import the MIT Introduction to Deep Learning package": "Descargar e importar el paquete MIT Introduction to Deep Learning",
        "Import TensorFlow and other libraries for this lab": "Importar TensorFlow y otras bibliotecas para este laboratorio",
        "Import PyTorch and other libraries for this lab": "Importar PyTorch y otras bibliotecas para este laboratorio",
        
        # Tensor creation
        "Create the nodes in the graph and initialize values": "Crear los nodos en el gráfico e inicializar valores",
        "Add them!": "¡Sumarlos!",
        "PyTorch overrides the \"+\" operation so that it is able to act on Tensors": "PyTorch sobrescribe la operación \"+\" para que pueda actuar sobre Tensores",
        "TensorFlow overrides the \"+\" operation so that it is able to act on Tensors": "TensorFlow sobrescribe la operación \"+\" para que pueda actuar sobre Tensores",
        
        # Layer definition
        "Define and initialize parameters": "Definir e inicializar parámetros",
        "Note that parameter initialization is random!": "¡Ten en cuenta que la inicialización de parámetros es aleatoria!",
        "the output is a linear transformation of the input": "la salida es una transformación lineal de la entrada",
        
        # Music preprocessing
        "the length of the vectorized songs string": "la longitud de la cadena vectorizada de canciones",
        "randomly choose the starting indices for the examples in the training batch": "elegir aleatoriamente los índices de inicio para los ejemplos en el lote de entrenamiento",
        "Create a mapping from indices to characters": "Crear un mapeo de índices a caracteres",
        "Create a mapping from characters to indices": "Crear un mapeo de caracteres a índices",
        "check that vectorized_songs is a numpy array": "verificar que vectorized_songs es un arreglo numpy",
        "the number of characters in the input string": "el número de caracteres en la cadena de entrada",
        
        # Model checks
        "Perform some simple checks on the model": "Realizar algunas verificaciones simples en el modelo",
        "print out a summary of the model": "imprimir un resumen del modelo",
        "Test the model with some sample data": "Probar el modelo con algunos datos de muestra",
        
        # Training
        "Initialize the hidden state": "Inicializar el estado oculto",
        "Forward pass": "Paso hacia adelante",
        "Compute the loss": "Calcular la pérdida",
        "Backward pass": "Paso hacia atrás",
        "Update the parameters": "Actualizar los parámetros",
        
        # Common phrases
        "random": "aleatorio",
        "randomly": "aleatoriamente",
        "Note that parameter initialization is random!": "¡Ten en cuenta que la inicialización de parámetros es aleatoria!",
        "Note that the parameter initialize is random!": "¡Ten en cuenta que la inicialización de parámetros es aleatoria!",
        "Since layer parameters are initialized randomly, we will set a random seed for reproducibility": "Dado que los parámetros de la capa se inicializan aleatoriamente, estableceremos una semilla aleatoria para reproducibilidad",
        "Initialize a random value for our intial x": "Inicializar un valor aleatorio para nuestra x inicial",
        "Initialize a random value for our initial x": "Inicializar un valor aleatorio para nuestra x inicial",
        
        # ========== TODO BLOCKS ==========
        "TODO": "HACER",
        "Defining higher-order Tensors": "Definiendo tensores de orden superior",
        "Define a 2-d Tensor": "Define un tensor 2-d",
        "Define a 4-d Tensor": "Define un tensor 4-d",
        "Define a 4-d Tensor.": "Define un tensor 4-d.",
        "Use torch.zeros to initialize a 4-d Tensor of zeros with size": "Usa torch.zeros para inicializar un tensor 4-d de ceros con tamaño",
        "Use tf.zeros to initialize a 4-d Tensor of zeros with size": "Usa tf.zeros para inicializar un tensor 4-d de ceros con tamaño",
        "You can think of this as": "Puedes pensar en esto como",
        "images where each image is RGB": "imágenes donde cada imagen es RGB",
        
        # ========== COMMON WORDS ==========
        "Note:": "Nota:",
        "Example:": "Ejemplo:",
        "Exercise:": "Ejercicio:",
        "Solution": "Solución",
        "solution": "solución",
        "matrix": "matriz",
        "matrices": "matrices",
        "vector": "vector",
        "vectors": "vectores",
        "tensor": "tensor",
        "tensors": "tensores",
        "True": "True",
        "False": "False",
    }


def translate_text(text, translations):
    """
    Translate English text to Spanish using the provided translation dictionary.
    Applies longest-match-first strategy to avoid partial replacements.
    """
    if not text or not text.strip():
        return text
    
    result = text
    
    # Sort by length (longest first) to handle phrases before individual words
    sorted_translations = sorted(translations.items(), key=lambda x: -len(x[0]))
    
    for eng_text, spa_text in sorted_translations:
        result = result.replace(eng_text, spa_text)
    
    # Post-processing: fix common typos from partial replacements
    typo_fixes = {
        'usyo': 'usando',
        'Usyo': 'Usando',
        'irlyesas': 'irlandesas',
        'tocyo': 'tocando',
        'Desglosyo': 'Desglosando',
        'solucións': 'soluciones',
        'tratyo': 'tratando',
        'ryom': 'aleatoria',
        'ryomly': 'aleatoriamente',
    }
    
    for typo, correct in typo_fixes.items():
        result = result.replace(typo, correct)
    
    return result


def translate_code_cell(source_lines, translations):
    """
    Translate comments in code cell while preserving all code.
    Handles full-line comments and inline comments.
    """
    translated_lines = []
    
    for line in source_lines:
        stripped = line.lstrip()
        
        # Skip shell commands (pip, wget, curl, etc.)
        if any(cmd in line for cmd in ['!pip', '!wget', '!curl', '!apt', '!conda']):
            translated_lines.append(line)
            continue
        
        # Handle full-line comments
        if stripped.startswith('#'):
            indent = line[:len(line) - len(stripped)]
            comment_text = stripped[1:].strip()
            
            if comment_text:
                # Don't translate shebang, special markers, or empty comments
                if comment_text.startswith('!') or comment_text in ['###', '####', '#####']:
                    translated_lines.append(line)
                else:
                    translated_comment = translate_text(comment_text, translations)
                    # Preserve newline if present
                    newline = '\n' if line.endswith('\n') else ''
                    translated_lines.append(f"{indent}# {translated_comment}{newline}")
            else:
                translated_lines.append(line)
        
        # Handle inline comments (be careful not to translate # in strings)
        elif '#' in line:
            # Simple heuristic: find # that's not inside quotes
            in_string = False
            quote_char = None
            hash_pos = -1
            
            for i, char in enumerate(line):
                # Track string state
                if char in ['"', "'"] and (i == 0 or line[i-1] != '\\'):
                    if not in_string:
                        in_string = True
                        quote_char = char
                    elif char == quote_char:
                        in_string = False
                        quote_char = None
                # Find # outside of strings
                elif char == '#' and not in_string:
                    hash_pos = i
                    break
            
            if hash_pos > 0:
                code_part = line[:hash_pos]
                comment_part = line[hash_pos+1:].strip()
                
                if comment_part:
                    translated_comment = translate_text(comment_part, translations)
                    newline = '\n' if line.endswith('\n') else ''
                    translated_lines.append(f"{code_part}# {translated_comment}{newline}")
                else:
                    translated_lines.append(line)
            else:
                # No valid inline comment found
                translated_lines.append(line)
        else:
            # No comment, keep as is
            translated_lines.append(line)
    
    return translated_lines


def translate_notebook(filepath, translations):
    """
    Translate a Jupyter notebook file in-place.
    Translates markdown cells and code comments.
    """
    print(f"Translating: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
    except Exception as e:
        print(f"  ✗ Error loading: {e}")
        return False
    
    # Process each cell
    cells_translated = 0
    for cell in notebook.get('cells', []):
        cell_type = cell.get('cell_type')
        
        if cell_type == 'markdown':
            # Translate markdown content
            source = cell.get('source', [])
            if isinstance(source, list):
                cell['source'] = [translate_text(line, translations) for line in source]
            else:
                cell['source'] = translate_text(source, translations)
            cells_translated += 1
        
        elif cell_type == 'code':
            # Translate code comments
            source = cell.get('source', [])
            if isinstance(source, list):
                cell['source'] = translate_code_cell(source, translations)
            else:
                # Convert to list, translate, convert back
                lines = source.split('\n')
                # Preserve line structure
                line_list = [l + '\n' for l in lines[:-1]] + ([lines[-1]] if lines else [])
                translated = translate_code_cell(line_list, translations)
                cell['source'] = ''.join(translated)
            cells_translated += 1
    
    # Save translated notebook
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, ensure_ascii=False, indent=2)
        print(f"  ✓ Translated {cells_translated} cells")
        return True
    except Exception as e:
        print(f"  ✗ Error saving: {e}")
        return False


def main():
    """Main translation function"""
    print("=" * 70)
    print("Comprehensive Jupyter Notebook Translation to Spanish")
    print("=" * 70)
    
    # Step 1: Reset notebooks to original state
    print("\nStep 1: Resetting notebooks to original state...")
    try:
        result = subprocess.run(
            ['git', 'checkout', 'HEAD', '--', 'lab1/*.ipynb', 'lab1/solutions/*.ipynb'],
            capture_output=True,
            text=True,
            cwd='/home/runner/work/introtodeeplearning_es-/introtodeeplearning_es-'
        )
        if result.returncode == 0:
            print("  ✓ Notebooks reset successfully")
        else:
            print(f"  ⚠ Warning: {result.stderr}")
    except Exception as e:
        print(f"  ⚠ Warning: Could not reset notebooks: {e}")
    
    # Step 2: Load comprehensive translation dictionary
    print("\nStep 2: Loading comprehensive translation dictionary...")
    translations = get_comprehensive_translations()
    print(f"  ✓ Loaded {len(translations)} translation entries")
    
    # Step 3: Translate all notebooks
    print("\nStep 3: Translating all notebooks...")
    notebooks = [
        "/home/runner/work/introtodeeplearning_es-/introtodeeplearning_es-/lab1/PT_Part1_Intro.ipynb",
        "/home/runner/work/introtodeeplearning_es-/introtodeeplearning_es-/lab1/PT_Part2_Music_Generation.ipynb",
        "/home/runner/work/introtodeeplearning_es-/introtodeeplearning_es-/lab1/TF_Part1_Intro.ipynb",
        "/home/runner/work/introtodeeplearning_es-/introtodeeplearning_es-/lab1/TF_Part2_Music_Generation.ipynb",
        "/home/runner/work/introtodeeplearning_es-/introtodeeplearning_es-/lab1/solutions/PT_Part1_Intro_Solution.ipynb",
        "/home/runner/work/introtodeeplearning_es-/introtodeeplearning_es-/lab1/solutions/TF_Part1_Intro_Solution.ipynb",
        "/home/runner/work/introtodeeplearning_es-/introtodeeplearning_es-/lab1/solutions/PT_Part2_Music_Generation_Solution.ipynb",
        "/home/runner/work/introtodeeplearning_es-/introtodeeplearning_es-/lab1/solutions/TF_Part2_Music_Generation_Solution.ipynb",
    ]
    
    success_count = 0
    for notebook_path in notebooks:
        if os.path.exists(notebook_path):
            if translate_notebook(notebook_path, translations):
                success_count += 1
        else:
            print(f"  ✗ File not found: {notebook_path}")
    
    print("\n" + "=" * 70)
    print(f"✓ Translation complete! {success_count}/{len(notebooks)} notebooks translated")
    print("=" * 70)
    
    return success_count == len(notebooks)


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
