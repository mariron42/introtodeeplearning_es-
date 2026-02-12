#!/usr/bin/env python3
"""
Comprehensive Translation Script for Lab2 PyTorch Notebooks
Translates ALL markdown cells and code comments from English to Spanish
Preserves JSON structure, code, URLs, technical terms
"""

import json
import re
import os
import sys


def get_comprehensive_translations():
    """
    Returns comprehensive translation dictionary for Lab2 PyTorch notebooks
    """
    return {
        # ========== HEADERS AND TITLES ==========
        "Copyright Information": "Información de Derechos de Autor",
        "Laboratory 2: Computer Vision": "Laboratorio 2: Visión por Computadora",
        "Part 1: MNIST Digit Classification": "Parte 1: Clasificación de Dígitos MNIST",
        "Part 2: Debiasing Facial Detection Systems": "Parte 2: Eliminación de Sesgos en Sistemas de Detección Facial",
        
        # ========== COPYRIGHT TEXT ==========
        "Copyright 2026 MIT Introduction to Deep Learning. All Rights Reserved.": "Copyright 2026 MIT Introduction to Deep Learning. Todos los Derechos Reservados.",
        "All Rights Reserved": "Todos los Derechos Reservados",
        "Licensed under the MIT License. You may not use this file except in compliance": "Licenciado bajo la Licencia MIT. No puedes usar este archivo excepto en cumplimiento",
        "with the License. Use and/or modification of this code outside of MIT Introduction": "con la Licencia. El uso y/o modificación de este código fuera de MIT Introduction",
        "to Deep Learning must reference:": "to Deep Learning debe hacer referencia a:",
        "© MIT Introduction to Deep Learning": "© MIT Introduction to Deep Learning",
        
        # ========== BADGES ==========
        "Visit MIT Deep Learning": "Visita MIT Deep Learning",
        "Run in Google Colab": "Ejecutar en Google Colab",
        "View Source on GitHub": "Ver Código Fuente en GitHub",
        
        # ========== SECTION HEADERS - PART 1 ==========
        "# Part 1: MNIST": "# Parte 1: MNIST",
        "## 0.1 Install Dependencies": "## 0.1 Instalar Dependencias",
        "## 0.2 Import Packages": "## 0.2 Importar Paquetes",
        "## 1.1 MNIST Dataset": "## 1.1 Conjunto de Datos MNIST",
        "## 1.2 Neural Network for Handwritten Digit Classification": "## 1.2 Red Neuronal para Clasificación de Dígitos Escritos a Mano",
        "## 1.3 Training": "## 1.3 Entrenamiento",
        "## 1.4 Convolutional Neural Network (CNN)": "## 1.4 Red Neuronal Convolucional (CNN)",
        "## 1.5 Training the CNN": "## 1.5 Entrenamiento de la CNN",
        
        # ========== SECTION HEADERS - PART 2 ==========
        "# Part 2: Debiasing": "# Parte 2: Eliminación de Sesgos",
        "## 0.1 Comet Setup": "## 0.1 Configuración de Comet",
        "## 1.1 Download and Explore the CelebA Dataset": "## 1.1 Descargar y Explorar el Conjunto de Datos CelebA",
        "## 1.2 Exploring Bias in CelebA": "## 1.2 Exploración de Sesgos en CelebA",
        "## 2.1 Datasets": "## 2.1 Conjuntos de Datos",
        "## 2.2 CNN for facial detection": "## 2.2 CNN para detección facial",
        "## 2.1 Variational Autoencoder (VAE)": "## 2.1 Autocodificador Variacional (VAE)",
        "## 2.2 Debiasing Variational Autoencoder (DB-VAE)": "## 2.2 Autocodificador Variacional sin Sesgos (DB-VAE)",
        "## 2.3 Training the DB-VAE": "## 2.3 Entrenamiento del DB-VAE",
        "## 3.1 Evaluate Facial Detection Classifier": "## 3.1 Evaluar Clasificador de Detección Facial",
        "### Thinking about bias": "### Pensando sobre el sesgo",
        "### Define and train the CNN model": "### Definir y entrenar el modelo CNN",
        
        # ========== COMMON PHRASES ==========
        "In the first portion of this lab, we will build and train a convolutional neural network (CNN) for classification of handwritten digits from the famous": "En la primera parte de este laboratorio, construiremos y entrenaremos una red neuronal convolucional (CNN) para la clasificación de dígitos escritos a mano del famoso conjunto de datos",
        "dataset. The MNIST dataset consists of 60,000 training images and 10,000 test images. Our classes are the digits 0-9.": "El conjunto de datos MNIST consiste de 60,000 imágenes de entrenamiento y 10,000 imágenes de prueba. Nuestras clases son los dígitos 0-9.",
        "First, let's download the course repository, install dependencies, and import the relevant packages we'll need for this lab.": "Primero, descarguemos el repositorio del curso, instalemos las dependencias e importemos los paquetes relevantes que necesitaremos para este laboratorio.",
        "First, we'll download the course repository, install dependencies, and import relevant packages.": "Primero, descargaremos el repositorio del curso, instalaremos las dependencias e importaremos los paquetes relevantes.",
        "We'll also install Comet. If you followed the instructions from Lab 1, you should have your Comet account set up. Enter your API key below.": "También instalaremos Comet. Si seguiste las instrucciones del Laboratorio 1, deberías tener tu cuenta de Comet configurada. Ingresa tu clave API a continuación.",
        "In this lab, we will continue using Comet to track our experiments.": "En este laboratorio, continuaremos usando Comet para rastrear nuestros experimentos.",
        "Now let's import the relevant packages.": "Ahora importemos los paquetes relevantes.",
        "Let's start by looking at some examples from the MNIST dataset.": "Comencemos observando algunos ejemplos del conjunto de datos MNIST.",
        "Let's download and load the dataset and display a few random samples from it:": "Descarguemos y carguemos el conjunto de datos y mostremos algunas muestras aleatorias de él:",
        "Now we'll define our neural network architecture.": "Ahora definiremos la arquitectura de nuestra red neuronal.",
        "Let's train our model!": "¡Entrenemos nuestro modelo!",
        "Now let's visualize the results.": "Ahora visualicemos los resultados.",
        "We can improve performance by using convolutional layers.": "Podemos mejorar el rendimiento usando capas convolucionales.",
        "Let's define a CNN architecture.": "Definamos una arquitectura CNN.",
        "The MNIST dataset object in PyTorch is not a simple tensor or array. It's an iterable dataset that loads samples (image-label pairs) one at a time or in batches. In a later section of this lab, we will define a handy DataLoader to process the data in batches.": "El objeto del conjunto de datos MNIST en PyTorch no es un tensor o arreglo simple. Es un conjunto de datos iterable que carga muestras (pares imagen-etiqueta) de una en una o en lotes. En una sección posterior de este laboratorio, definiremos un DataLoader útil para procesar los datos en lotes.",
        
        # Part 2 specific phrases
        "In the second portion of the lab, we'll explore two prominent aspects of applied deep learning: facial detection and algorithmic bias.": "En la segunda parte del laboratorio, exploraremos dos aspectos prominentes del aprendizaje profundo aplicado: detección facial y sesgo algorítmico.",
        "Deploying fair, unbiased AI systems is critical to their long-term acceptance. Consider the task of facial detection: given an image, is it an image of a face?  This seemingly simple, but extremely important, task is subject to significant amounts of algorithmic bias among select demographics.": "Implementar sistemas de IA justos y sin sesgos es crítico para su aceptación a largo plazo. Considera la tarea de detección facial: dada una imagen, ¿es una imagen de un rostro? Esta tarea aparentemente simple, pero extremadamente importante, está sujeta a cantidades significativas de sesgo algorítmico entre ciertas demografías.",
        "Let's get started by installing the relevant dependencies.": "Comencemos instalando las dependencias relevantes.",
        "We will be using Comet ML to track our model development and training runs.": "Usaremos Comet ML para rastrear nuestro desarrollo de modelos y ejecuciones de entrenamiento.",
        "We can look at the size of the training dataset and grab a batch of size 100:": "Podemos ver el tamaño del conjunto de datos de entrenamiento y tomar un lote de tamaño 100:",
        "Play around with displaying images to get a sense of what the training data actually looks like!": "¡Juega con la visualización de imágenes para tener una idea de cómo se ve realmente el conjunto de datos de entrenamiento!",
        "Remember we'll be training our facial detection classifiers on the large, well-curated CelebA dataset (and ImageNet), and then evaluating their accuracy by testing them on an independent test dataset. Our goal is to build a model that trains on CelebA *and* achieves high classification accuracy on the the test dataset across all demographics, and to thus show that this model does not suffer from any hidden bias.": "Recuerda que entrenaremos nuestros clasificadores de detección facial en el gran conjunto de datos bien curado CelebA (e ImageNet), y luego evaluaremos su precisión probándolos en un conjunto de datos de prueba independiente. Nuestro objetivo es construir un modelo que se entrene en CelebA *y* logre alta precisión de clasificación en el conjunto de datos de prueba en todas las demografías, y así mostrar que este modelo no sufre de ningún sesgo oculto.",
        "What exactly do we mean when we say a classifier is biased": "¿Qué queremos decir exactamente cuando decimos que un clasificador está sesgado",
        "First, we'll define and train a CNN on the facial classification task, and evaluate its accuracy. Later, we'll evaluate the performance of our debiased models against this baseline CNN. The CNN model has a relatively standard architecture consisting of a series of convolutional layers with batch normalization followed by two fully connected layers to flatten the convolution output and generate a class prediction.": "Primero, definiremos y entrenaremos una CNN en la tarea de clasificación facial, y evaluaremos su precisión. Más tarde, evaluaremos el rendimiento de nuestros modelos sin sesgos contra esta CNN base. El modelo CNN tiene una arquitectura relativamente estándar que consiste en una serie de capas convolucionales con normalización por lotes seguidas de dos capas completamente conectadas para aplanar la salida de convolución y generar una predicción de clase.",
        
        # More comprehensive phrases from notebooks
        "Our training set is made up of 28x28 grayscale images of handwritten digits.": "Nuestro conjunto de entrenamiento está compuesto de imágenes en escala de grises de 28x28 de dígitos escritos a mano.",
        "Let's visualize what some of these images and their corresponding training labels look like.": "Visualicemos cómo se ven algunas de estas imágenes y sus etiquetas de entrenamiento correspondientes.",
        "We'll first build a simple neural network consisting of two fully connected layers and train this model to classify the images.": "Primero construiremos una red neuronal simple que consiste en dos capas completamente conectadas y entrenaremos este modelo para clasificar las imágenes.",
        "To define the architecture of this first fully connected neural network, we'll once again use the the PyTorch API and define the network as a subclass of": "Para definir la arquitectura de esta primera red neuronal completamente conectada, usaremos nuevamente la API de PyTorch y definiremos la red como una subclase de",
        "As we progress through this next portion, you may find that you'll want to make changes to the architecture defined above.": "A medida que avances en esta siguiente parte, puede que quieras hacer cambios a la arquitectura definida arriba.",
        "Note that in order to update the model later on, you'll need to re-run the cell": "Nota que para actualizar el modelo más adelante, necesitarás volver a ejecutar la celda",
        "Let's take a step back and think about the network we've just created.": "Demos un paso atrás y pensemos sobre la red que acabamos de crear.",
        "The first layer in this network": "La primera capa en esta red",
        "transforms the format of the images from a 2d-array": "transforma el formato de las imágenes de un arreglo 2d",
        "Recall that in Lab 1, we explored creating more flexible models by subclassing": "Recuerda que en el Laboratorio 1, exploramos la creación de modelos más flexibles mediante subclases de",
        "This technique of defining models is more common in PyTorch than using the Sequential API.": "Esta técnica de definir modelos es más común en PyTorch que usar la API Sequential.",
        
        # Training and evaluation phrases  
        "Before training the model, we need to define components that govern its performance and guide its learning process.": "Antes de entrenar el modelo, necesitamos definir componentes que rigen su rendimiento y guían su proceso de aprendizaje.",
        "We're now ready to train our model, which will involve feeding the training data": "Ahora estamos listos para entrenar nuestro modelo, lo cual implicará alimentar los datos de entrenamiento",
        "into the model, and then asking the model to learn to associate images and labels.": "al modelo, y luego pedirle al modelo que aprenda a asociar imágenes y etiquetas.",
        "As the model trains, the loss and accuracy metrics are displayed.": "Mientras el modelo se entrena, se muestran las métricas de pérdida y precisión.",
        "With five epochs and a learning rate of 0.01, this fully connected model should achieve": "Con cinco épocas y una tasa de aprendizaje de 0.01, este modelo completamente conectado debería alcanzar",
        "Now that we've trained the model, we can ask it to make predictions about a test set that it hasn't seen before.": "Ahora que hemos entrenado el modelo, podemos pedirle que haga predicciones sobre un conjunto de prueba que no ha visto antes.",
        "You may observe that the accuracy on the test dataset is a little lower than the accuracy on the training dataset.": "Puedes observar que la precisión en el conjunto de datos de prueba es un poco menor que la precisión en el conjunto de datos de entrenamiento.",
        "This gap between training accuracy and test accuracy is an example of": "Esta brecha entre precisión de entrenamiento y precisión de prueba es un ejemplo de",
        "overfitting": "sobreajuste",
        
        # CNN specific
        "As we saw in lecture, convolutional neural networks (CNNs) are particularly well-suited for a variety of tasks in computer vision": "Como vimos en la conferencia, las redes neuronales convolucionales (CNN) son particularmente adecuadas para una variedad de tareas en visión por computadora",
        "and have achieved near-perfect accuracies on the MNIST dataset.": "y han logrado precisiones casi perfectas en el conjunto de datos MNIST.",
        "We'll use the same training and test datasets as before, and proceed similarly as our fully connected network to define and train the model.": "Usaremos los mismos conjuntos de datos de entrenamiento y prueba que antes, y procederemos de manera similar a nuestra red completamente conectada para definir y entrenar el modelo.",
        "Earlier in the lab, we defined a": "Antes en el laboratorio, definimos una",
        "function. The body of the function is quite useful because it allows us to train both types of models": "función. El cuerpo de la función es bastante útil porque nos permite entrenar ambos tipos de modelos",
        "Now that we've trained the model, let's evaluate it on the test dataset.": "Ahora que hemos entrenado el modelo, evaluémoslo en el conjunto de datos de prueba.",
        "What is the highest accuracy you're able to achieve using the CNN model": "¿Cuál es la precisión más alta que puedes lograr usando el modelo CNN",
        "and how does the accuracy of the CNN model compare to the accuracy of the simple fully connected network?": "y cómo se compara la precisión del modelo CNN con la precisión de la red simple completamente conectada?",
        "What optimizers and learning rates did you use to train the model?": "¿Qué optimizadores y tasas de aprendizaje usaste para entrenar el modelo?",
        
        # Predictions
        "With the model trained, we can use it to make predictions about some images.": "Con el modelo entrenado, podemos usarlo para hacer predicciones sobre algunas imágenes.",
        "With this function call, the model has predicted the label of the first image in the testing set.": "Con esta llamada de función, el modelo ha predicho la etiqueta de la primera imagen en el conjunto de prueba.",
        "Let's take a look at the prediction:": "Veamos la predicción:",
        "As you can see, a prediction is an array of 10 numbers.": "Como puedes ver, una predicción es un arreglo de 10 números.",
        "Recall that the output of our model is a  distribution over the 10 digit classes.": "Recuerda que la salida de nuestro modelo es una distribución sobre las 10 clases de dígitos.",
        "Thus, these numbers describe the model's predicted likelihood": "Por lo tanto, estos números describen la probabilidad predicha del modelo",
        "So, the model is most confident that this image is a": "Entonces, el modelo está más confiado de que esta imagen es un",
        "We can check the test label (remember, this is the true identity of the digit) to see if this prediction is correct:": "Podemos verificar la etiqueta de prueba (recuerda, esta es la identidad verdadera del dígito) para ver si esta predicción es correcta:",
        "It is!": "¡Lo es!",
        "Let's visualize the classification results on the MNIST dataset.": "Visualicemos los resultados de clasificación en el conjunto de datos MNIST.",
        "We will plot images from the test dataset along with their predicted label": "Grafiquemos imágenes del conjunto de datos de prueba junto con su etiqueta predicha",
        "We can also plot several images along with their predictions": "También podemos graficar varias imágenes junto con sus predicciones",
        "where correct prediction labels are blue and incorrect prediction labels are grey.": "donde las etiquetas de predicción correctas son azules y las etiquetas de predicción incorrectas son grises.",
        "The number in the title of each image is the predicted label.": "El número en el título de cada imagen es la etiqueta predicha.",
        
        # Conclusion
        "In this part of the lab, you had the chance to play with different MNIST classifiers with different architectures": "En esta parte del laboratorio, tuviste la oportunidad de jugar con diferentes clasificadores MNIST con diferentes arquitecturas",
        "This technique of defining models is more commonly used in PyTorch.": "Esta técnica de definir modelos es más comúnmente usada en PyTorch.",
        "We will practice using this approach of subclassing to define our models for the rest of the lab.": "Practicaremos usando este enfoque de subclases para definir nuestros modelos para el resto del laboratorio.",
        "into the model, and then asking it to learn the associations between images and labels.": "al modelo, y luego pedirle que aprenda las asociaciones entre imágenes y etiquetas.",
        "We'll also need to define the batch size and the number of epochs, or iterations over the MNIST dataset, to use during training.": "También necesitaremos definir el tamaño del lote y el número de épocas, o iteraciones sobre el conjunto de datos MNIST, para usar durante el entrenamiento.",
        "This dataset consists of a (image, label) tuples that we will iteratively access in batches.": "Este conjunto de datos consiste en tuplas (imagen, etiqueta) que accederemos iterativamente en lotes.",
        "an accuracy of approximatley 0.97 (or 97%) on the training data.": "una precisión de aproximadamente 0.97 (o 97%) en los datos de entrenamiento.",
        "and train our new CNN model": "y entrenar nuestro nuevo modelo CNN",
        "that the image corresponds to each of the 10 different digits.": "de que la imagen corresponde a cada uno de los 10 dígitos diferentes.",
        "look at the digit that has the highest likelihood": "ver el dígito que tiene la mayor probabilidad",
        "The number gives the percent confidence (out of 100) for the predicted label": "El número da el porcentaje de confianza (de 100) para la etiqueta predicha",
        "as well as a histogram that provides the prediction probabilities for each of the digits.": "así como un histograma que proporciona las probabilidades de predicción para cada uno de los dígitos.",
        "Recuerda that in PyTorch": "Recuerda que en PyTorch",
        "You are free to implement the following parts with or without the train and evaluate functions we defined above": "Eres libre de implementar las siguientes partes con o sin las funciones de entrenamiento y evaluación que definimos arriba",
        "By appending the predictions, test labels, and test images from each batch, we will first gradually accumulate all the data needed for visualization into singular variables to observe our model's predictions.": "Al agregar las predicciones, etiquetas de prueba e imágenes de prueba de cada lote, primero acumularemos gradualmente todos los datos necesarios para la visualización en variables singulares para observar las predicciones de nuestro modelo.",
        "Our network will ultimately output a probability distribution over the 10 digit classes (0-9)": "Nuestra red finalmente producirá una distribución de probabilidad sobre las 10 clases de dígitos (0-9)",
        "In this section, we will define a function to train the model using": "En esta sección, definiremos una función para entrenar el modelo usando",
        "to automatically update our model parameters (weights and biases) as we saw in Lab 1.": "para actualizar automáticamente nuestros parámetros del modelo (pesos y sesgos) como vimos en el Laboratorio 1.",
        "You can think of this layer as unstacking rows of pixels in the image and lining them up": "Puedes pensar en esta capa como desapilar filas de píxeles en la imagen y alinearlas",
        "And to evaluate accuracy, we can check to see if the model's predictions match the labels from this loader.": "Y para evaluar la precisión, podemos verificar si las predicciones del modelo coinciden con las etiquetas de este cargador.",
        "Since we have now trained the mode, we will use the eval state of the model on the test data.": "Como ahora hemos entrenado el modelo, usaremos el estado de evaluación del modelo en los datos de prueba.",
        "Nota the model can be very confident in an incorrect prediction!": "Nota que el modelo puede estar muy confiado en una predicción incorrecta!",
        "We will now build a CNN composed of two convolutional layers and pooling layers, followed by two fully connected layers, and ultimately output a probability distribution over the 10 digit classes (0-9)": "Ahora construiremos una CNN compuesta de dos capas convolucionales y capas de pooling, seguidas de dos capas completamente conectadas, y finalmente producir una distribución de probabilidad sobre las 10 clases de dígitos (0-9)",
        "In this example, we'll define and take a look at the *accuracy*, the fraction of the images that are correctly classified.": "En este ejemplo, definiremos y veremos la *precisión*, la fracción de las imágenes que están correctamente clasificadas.",
        "We'll start out by using a stochastic gradient descent (SGD) optimizer initialized with a learning rate": "Comenzaremos usando un optimizador de descenso de gradiente estocástico (SGD) inicializado con una tasa de aprendizaje",
        "In this example, iterating over the": "En este ejemplo, iterar sobre el",
        "allows us to access our test images and test labels": "nos permite acceder a nuestras imágenes de prueba y etiquetas de prueba",
        "These include the loss function, optimizer, and evaluation metrics:": "Estos incluyen la función de pérdida, optimizador y métricas de evaluación:",
        "This defines how we measure how accurate the model is during training": "Esto define cómo medimos qué tan preciso es el modelo durante el entrenamiento",
        'As was covered in lecture, during training we want to minimize this function, which will "steer" the model in the right direction.': 'Como se cubrió en la conferencia, durante el entrenamiento queremos minimizar esta función, que "dirigirá" al modelo en la dirección correcta.',
        "This defines how the model is updated based on the data it sees and its loss function.": "Esto define cómo se actualiza el modelo basándose en los datos que ve y su función de pérdida.",
        "What is most important is understanding how to manipulate the bodies of those functions to train and test models.": "Lo más importante es entender cómo manipular los cuerpos de esas funciones para entrenar y probar modelos.",
        "As we've done above, we can define the loss function, optimizer, and calculate the accuracy": "Como hemos hecho arriba, podemos definir la función de pérdida, optimizador y calcular la precisión",
        "The next part of the lab explores another application of CNNs, facial detection, and some drawbacks of AI systems in real world applications, like issues of bias.": "La siguiente parte del laboratorio explora otra aplicación de las CNN, detección facial, y algunas desventajas de los sistemas de IA en aplicaciones del mundo real, como problemas de sesgo.",
        "Each node contains a score that indicates the probability that the current image belongs to one of the handwritten digit classes.": "Cada nodo contiene una puntuación que indica la probabilidad de que la imagen actual pertenezca a una de las clases de dígitos escritos a mano.",
        "That defines our fully connected model!": "¡Eso define nuestro modelo completamente conectado!",
        "Aquí, we will define a PyTorch": "Aquí, definiremos un PyTorch",
        "that will enable us to do that.": "que nos permitirá hacer eso.",
        "Usar the parameters shown in the network architecture above to define these layers and build the CNN model": "Usa los parámetros mostrados en la arquitectura de red arriba para definir estas capas y construir el modelo CNN",
        "To do this we will explore two layers we have not encountered before: you can use": "Para hacer esto exploraremos dos capas que no hemos encontrado antes: puedes usar",
        "to define convolutional layers and": "para definir capas convolucionales y",
        "Since we are performing a categorical classification task, we'll want to use the": "Como estamos realizando una tarea de clasificación categórica, querremos usar la",
        "cross entropy loss": "pérdida de entropía cruzada",
        "You'll want to experiment with the learning rate and optimizer to try to achieve high accuracy!": "¡Querrás experimentar con la tasa de aprendizaje y el optimizador para tratar de lograr alta precisión!",
        "Nota how we first use a": "Nota cómo primero usamos un",
        "layer, which flattens the input so that it can be fed into the model.": "capa, que aplana la entrada para que pueda ser alimentada al modelo.",
        "In this next block, you'll define the architecture of the fully connected network.": "En este siguiente bloque, definirás la arquitectura de la red completamente conectada.",
        
        # Additional phrases found
        "when a machine learning model performs worse on new data than on its training data.": "cuando un modelo de aprendizaje automático se desempeña peor en datos nuevos que en sus datos de entrenamiento.",
        "What is the highest accuracy you can achieve with this first fully connected network?": "¿Cuál es la precisión más alta que puedes lograr con esta primera red completamente conectada?",
        "In Lab 1, we saw how we can use the": "En el Laboratorio 1, vimos cómo podemos usar el",
        "method on the train dataset object  to shuffle the data and batch it efficiently.": "método en el objeto del conjunto de datos de entrenamiento para barajar los datos y agruparlos eficientemente.",
        "Aquí, we will define a": "Aquí, definiremos un",
        "that will feed the data to the model in batches.": "que alimentará los datos al modelo en lotes.",
        "to define pooling layers.": "para definir capas de pooling.",
        "Recall from class that pooling is a technique to downsample the input data": "Recuerda de la clase que el pooling es una técnica para submuestrear los datos de entrada",
        "In this next block, you'll define the architecture of the CNN.": "En este siguiente bloque, definirás la arquitectura de la CNN.",
        "In PyTorch, with a defined model, we simply call": "En PyTorch, con un modelo definido, simplemente llamamos",
        "on the model object to output the predictions for a batch of images.": "en el objeto del modelo para producir las predicciones para un lote de imágenes.",
        "Since we're working with PyTorch, we need to bring our data onto the":  "Como estamos trabajando con PyTorch, necesitamos traer nuestros datos al",
        "before we can pass them to our model.": "antes de que podamos pasarlos a nuestro modelo.",
        "In earlier versions of PyTorch, we": "En versiones anteriores de PyTorch, nosotros",
        "Now however, we can": "Ahora sin embargo, podemos",
        "to place our data onto the correct device, whether that's a": "para colocar nuestros datos en el dispositivo correcto, ya sea una",
        "from a 2d-array (of 28 by 28 pixels), to a 1d-array of 784 pixels.": "de un arreglo 2d (de 28 por 28 píxeles), a un arreglo 1d de 784 píxeles.",
        "This layer does not have any parameters to learn.": "Esta capa no tiene parámetros para aprender.",
        "The final layer is a densely-connected layer with 10 output nodes.": "La capa final es una capa densamente conectada con 10 nodos de salida.",
        
        # ========== CODE COMMENTS - SETUP ==========
        "Import PyTorch and other relevant libraries": "Importar PyTorch y otras bibliotecas relevantes",
        "MIT introduction to deep learning package": "Paquete de introducción a deep learning del MIT",
        "other packages": "otros paquetes",
        "Download the repository": "Descargar el repositorio",
        "Install dependencies": "Instalar dependencias",
        "Import packages": "Importar paquetes",
        "Import TensorFlow": "Importar TensorFlow",
        "Import PyTorch": "Importar PyTorch",
        
        # ========== CODE COMMENTS - COMET ==========
        "ENTER YOUR API KEY HERE": "INGRESA TU CLAVE API AQUÍ",
        "Check that we are using a GPU, if not switch runtimes": "Verificar que estemos usando una GPU, si no cambiar el entorno de ejecución",
        "using Runtime > Change Runtime Type > GPU": "usando Runtime > Change Runtime Type > GPU",
        "Set GPU for computation": "Configurar GPU para cómputo",
        "start a first comet experiment for the first part of the lab": "iniciar un primer experimento comet para la primera parte del laboratorio",
        "start a second comet experiment for the second part of the lab": "iniciar un segundo experimento comet para la segunda parte del laboratorio",
        "Create a new Comet experiment": "Crear un nuevo experimento Comet",
        "Log parameters to Comet": "Registrar parámetros en Comet",
        "Log metrics to Comet": "Registrar métricas en Comet",
        
        # ========== CODE COMMENTS - DATA LOADING ==========
        "Load the MNIST dataset": "Cargar el conjunto de datos MNIST",
        "Download and load the data": "Descargar y cargar los datos",
        "Normalize the data": "Normalizar los datos",
        "Transform to tensor and normalize": "Transformar a tensor y normalizar",
        "Create data loaders": "Crear cargadores de datos",
        "Split into training and test sets": "Dividir en conjuntos de entrenamiento y prueba",
        "Visualize some examples": "Visualizar algunos ejemplos",
        "Plot the images": "Graficar las imágenes",
        "Display sample images": "Mostrar imágenes de muestra",
        
        # ========== CODE COMMENTS - MODEL DEFINITION ==========
        "Define the model architecture": "Definir la arquitectura del modelo",
        "Define the neural network": "Definir la red neuronal",
        "Build the model": "Construir el modelo",
        "Define fully connected layers": "Definir capas completamente conectadas",
        "Define convolutional layers": "Definir capas convolucionales",
        "Define pooling layers": "Definir capas de pooling",
        "Add dropout for regularization": "Agregar dropout para regularización",
        "Define the forward pass": "Definir el paso hacia adelante",
        "Forward pass": "Paso hacia adelante",
        "Flatten the input": "Aplanar la entrada",
        "Apply activation function": "Aplicar función de activación",
        "Return output": "Retornar salida",
        
        # ========== CODE COMMENTS - TRAINING ==========
        "Define loss function and optimizer": "Definir función de pérdida y optimizador",
        "Define loss function": "Definir función de pérdida",
        "Define optimizer": "Definir optimizador",
        "Set up training loop": "Configurar bucle de entrenamiento",
        "Training loop": "Bucle de entrenamiento",
        "Train the model": "Entrenar el modelo",
        "Iterate through epochs": "Iterar a través de épocas",
        "Iterate through batches": "Iterar a través de lotes",
        "Zero the gradients": "Poner a cero los gradientes",
        "Forward pass through the network": "Paso hacia adelante a través de la red",
        "Calculate the loss": "Calcular la pérdida",
        "Backward pass": "Paso hacia atrás",
        "Backpropagation": "Retropropagación",
        "Compute gradients": "Calcular gradientes",
        "Update the weights": "Actualizar los pesos",
        "Update model parameters": "Actualizar parámetros del modelo",
        "Print training progress": "Imprimir progreso del entrenamiento",
        "Log to Comet": "Registrar en Comet",
        
        # ========== CODE COMMENTS - EVALUATION ==========
        "Evaluate the model": "Evaluar el modelo",
        "Test the model": "Probar el modelo",
        "Evaluate on test set": "Evaluar en conjunto de prueba",
        "Calculate accuracy": "Calcular precisión",
        "Compute accuracy": "Calcular precisión",
        "Make predictions": "Hacer predicciones",
        "Get model predictions": "Obtener predicciones del modelo",
        "Visualize predictions": "Visualizar predicciones",
        "Plot results": "Graficar resultados",
        "Display results": "Mostrar resultados",
        
        # ========== CODE COMMENTS - CNN SPECIFIC ==========
        "Define CNN architecture": "Definir arquitectura CNN",
        "Convolutional layer": "Capa convolucional",
        "Max pooling layer": "Capa de max pooling",
        "Batch normalization": "Normalización por lotes",
        "Fully connected layer": "Capa completamente conectada",
        "Apply convolution": "Aplicar convolución",
        "Apply pooling": "Aplicar pooling",
        "Apply ReLU activation": "Aplicar activación ReLU",
        
        # ========== CODE COMMENTS - CELEBA/DEBIASING ==========
        "Download CelebA dataset": "Descargar conjunto de datos CelebA",
        "Load CelebA data": "Cargar datos de CelebA",
        "Explore the dataset": "Explorar el conjunto de datos",
        "Visualize face images": "Visualizar imágenes de rostros",
        "Check for bias in the data": "Verificar sesgos en los datos",
        "Analyze class distribution": "Analizar distribución de clases",
        "Define VAE architecture": "Definir arquitectura VAE",
        "Define encoder": "Definir codificador",
        "Define decoder": "Definir decodificador",
        "Encode the input": "Codificar la entrada",
        "Decode the latent representation": "Decodificar la representación latente",
        "Sample from latent space": "Muestrear del espacio latente",
        "Reparameterization trick": "Truco de reparametrización",
        "Calculate reconstruction loss": "Calcular pérdida de reconstrucción",
        "Calculate KL divergence": "Calcular divergencia KL",
        "Compute VAE loss": "Calcular pérdida VAE",
        "Train the VAE": "Entrenar el VAE",
        "Train the DB-VAE": "Entrenar el DB-VAE",
        "Reconstruct images": "Reconstruir imágenes",
        "Generate new faces": "Generar nuevos rostros",
        "Evaluate fairness": "Evaluar equidad",
        "Compare standard VAE and DB-VAE": "Comparar VAE estándar y DB-VAE",
        
        # Part 2 markdown content
        "We will also evaluate our networks on an independent test dataset containing faces that were not seen during training.": "También evaluaremos nuestras redes en un conjunto de datos de prueba independiente que contiene rostros que no se vieron durante el entrenamiento.",
        "For the test data, we'll look at the classification accuracy across four different demographics": "Para los datos de prueba, veremos la precisión de clasificación a través de cuatro demografías diferentes",
        "Now, let's evaluate the probability of each of these face demographics being classified as a face using the standard CNN classifier we've just trained.": "Ahora, evaluemos la probabilidad de que cada una de estas demografías de rostros sea clasificada como un rostro usando el clasificador CNN estándar que acabamos de entrenar.",
        "Take a look at the accuracies for this first model across these four groups.": "Echa un vistazo a las precisiones para este primer modelo a través de estos cuatro grupos.",
        "What do you observe?": "¿Qué observas?",
        "Would you consider this model biased or unbiased?": "¿Considerarías este modelo sesgado o sin sesgos?",
        "What are some reasons why a trained model may have biases?": "¿Cuáles son algunas razones por las que un modelo entrenado puede tener sesgos?",
        
        # VAE section
        "Great! Now that we have a more concrete sense of how VAEs work": "¡Genial! Ahora que tenemos un sentido más concreto de cómo funcionan los VAE",
        "let's explore how we can leverage this network structure to train a": "exploremos cómo podemos aprovechar esta estructura de red para entrenar un",
        "debiased facial classifier": "clasificador facial sin sesgos",
        "Recall that we want to apply our DB-VAE to a": "Recuerda que queremos aplicar nuestro DB-VAE a un",
        "supervised classification problem": "problema de clasificación supervisada",
        "the facial detection task": "la tarea de detección facial",
        "Importantly, note how the encoder portion in the DB-VAE architecture also outputs a single": "Importante, nota cómo la porción codificadora en la arquitectura DB-VAE también produce una única",
        "class prediction": "predicción de clase",
        "First, we've defined a short helper function": "Primero, hemos definido una función auxiliar corta",
        "that returns the latent variable means returned by the encoder": "que devuelve las medias de variables latentes devueltas por el codificador",
        "after a batch of images is inputted to the network:": "después de que un lote de imágenes se ingresa a la red:",
        "Now, we will put this decoder together with the standard CNN classifier as our encoder to define the DB-VAE.": "Ahora, pondremos este decodificador junto con el clasificador CNN estándar como nuestro codificador para definir el DB-VAE.",
        "Note that at this point, there is nothing special about how we put the model together that would debias the facial classifer": "Nota que en este punto, no hay nada especial sobre cómo armamos el modelo que eliminaría el sesgo del clasificador facial",
        "that's next!": "¡eso es lo siguiente!",
        "As stated, the encoder architecture is identical to the CNN from earlier in this lab.": "Como se indicó, la arquitectura del codificador es idéntica a la CNN de antes en este laboratorio.",
        "Note the outputs of our constructed DB_VAE model in the": "Nota las salidas de nuestro modelo DB_VAE construido en la",
        "function:": "función:",
        
        # Subsections
        "### Fully connected neural network architecture": "### Arquitectura de red neuronal completamente conectada",
        "### Model Metrics and Training Parameters": "### Métricas del Modelo y Parámetros de Entrenamiento",
        "### Evaluate accuracy on the test dataset": "### Evaluar precisión en el conjunto de datos de prueba",
        "### Define the CNN model": "### Definir el modelo CNN",
        "### Train and test the CNN model": "### Entrenar y probar el modelo CNN",
        "### Evaluate the CNN Model": "### Evaluar el Modelo CNN",
        "### Hacer predicciones with the CNN model": "### Hacer predicciones con el modelo CNN",
        "## 1.5 Conclusion": "## 1.5 Conclusión",
        
        # ========== ADDITIONAL COMMON PHRASES ==========
        "Initialize the model": "Inicializar el modelo",
        "Set random seed": "Establecer semilla aleatoria",
        "Set device": "Establecer dispositivo",
        "Move to device": "Mover al dispositivo",
        "Save the model": "Guardar el modelo",
        "Load the model": "Cargar el modelo",
        "Print model summary": "Imprimir resumen del modelo",
        "Set model to training mode": "Establecer modelo en modo de entrenamiento",
        "Set model to evaluation mode": "Establecer modelo en modo de evaluación",
        "Disable gradient calculation": "Deshabilitar cálculo de gradientes",
        "Enable gradient calculation": "Habilitar cálculo de gradientes",
        
        # ========== HYPERPARAMETERS ==========
        "Set hyperparameters": "Establecer hiperparámetros",
        "Define hyperparameters": "Definir hiperparámetros",
        "Learning rate": "Tasa de aprendizaje",
        "Batch size": "Tamaño de lote",
        "Number of epochs": "Número de épocas",
        "Hidden size": "Tamaño oculto",
        "Latent dimension": "Dimensión latente",
        "Dropout rate": "Tasa de dropout",
        
        # ========== UTILITIES ==========
        "Helper function": "Función auxiliar",
        "Utility function": "Función de utilidad",
        "Define helper functions": "Definir funciones auxiliares",
        "Create directory if it doesn't exist": "Crear directorio si no existe",
        "Set up plotting": "Configurar gráficas",
        "Configure matplotlib": "Configurar matplotlib",
    }


def translate_text(text, translations, preserve_case=False):
    """
    Translate text using the translation dictionary
    Only translates complete phrases, not individual words, to avoid corrupting compound words
    
    Args:
        text: Text to translate
        translations: Dictionary of English to Spanish translations
        preserve_case: Whether to preserve case sensitivity
    
    Returns:
        Translated text
    """
    if not text or not text.strip():
        return text
    
    # Sort by length (longest first) to avoid partial replacements
    sorted_translations = sorted(translations.items(), key=lambda x: len(x[0]), reverse=True)
    
    translated = text
    for eng, esp in sorted_translations:
        # Skip if already translated
        if esp in translated:
            continue
        
        # Do simple replacement for phrases
        if preserve_case:
            translated = translated.replace(eng, esp)
        else:
            # Case-insensitive replacement
            pattern = re.compile(re.escape(eng), re.IGNORECASE)
            translated = pattern.sub(esp, translated)
    
    return translated


def translate_code_comments(code):
    """
    Translate comments in code cells while preserving code structure
    
    Args:
        code: Code string to translate
    
    Returns:
        Code with translated comments
    """
    translations = get_comprehensive_translations()
    lines = code.split('\n')
    translated_lines = []
    
    for line in lines:
        if '#' in line:
            # Find the position of the first #
            comment_start = line.find('#')
            code_part = line[:comment_start]
            comment_part = line[comment_start+1:]
            
            # Translate the comment
            translated_comment = translate_text(comment_part, translations, preserve_case=False)
            translated_lines.append(code_part + '#' + translated_comment)
        else:
            translated_lines.append(line)
    
    return '\n'.join(translated_lines)


def translate_markdown(text):
    """
    Translate markdown text while preserving formatting
    
    Args:
        text: Markdown text to translate
    
    Returns:
        Translated markdown text
    """
    translations = get_comprehensive_translations()
    return translate_text(text, translations, preserve_case=True)


def translate_notebook(input_path):
    """
    Translate a Jupyter notebook in place
    
    Args:
        input_path: Path to the notebook to translate
    """
    print(f"\nTranslating: {input_path}")
    
    # Load notebook
    with open(input_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Track statistics
    markdown_cells = 0
    code_cells_with_comments = 0
    
    # Translate each cell
    for cell in notebook.get('cells', []):
        cell_type = cell.get('cell_type', '')
        source = cell.get('source', [])
        
        if cell_type == 'markdown':
            # Translate markdown cells
            markdown_cells += 1
            if isinstance(source, list):
                translated_source = []
                for line in source:
                    translated_source.append(translate_markdown(line))
                cell['source'] = translated_source
            else:
                cell['source'] = translate_markdown(source)
        
        elif cell_type == 'code':
            # Translate code comments
            if isinstance(source, list):
                code = ''.join(source)
            else:
                code = source
            
            # Check if there are comments
            if '#' in code:
                code_cells_with_comments += 1
                translated_code = translate_code_comments(code)
                
                # Preserve original line structure
                if isinstance(source, list):
                    # Split translated code back into lines, preserving newlines
                    translated_lines = translated_code.split('\n')
                    new_source = []
                    for i, line in enumerate(translated_lines):
                        if i < len(translated_lines) - 1:
                            new_source.append(line + '\n')
                        else:
                            # Last line - check if original had newline
                            if source and source[-1].endswith('\n'):
                                new_source.append(line + '\n')
                            else:
                                new_source.append(line)
                    cell['source'] = new_source
                else:
                    cell['source'] = translated_code
    
    # Save translated notebook (overwrite original)
    with open(input_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=1)
    
    print(f"  ✓ Translated {markdown_cells} markdown cells")
    print(f"  ✓ Translated {code_cells_with_comments} code cells with comments")


def main():
    """Main translation function"""
    print("=" * 70)
    print("Lab2 PyTorch Notebooks Translation Script")
    print("=" * 70)
    
    # Define notebook paths
    base_dir = '/home/runner/work/introtodeeplearning_es-/introtodeeplearning_es-/lab2'
    notebooks = [
        'PT_Part1_MNIST.ipynb',
        'PT_Part2_Debiasing.ipynb',
        'solutions/PT_Part1_MNIST_Solution.ipynb',
        'solutions/PT_Part2_Debiasing_Solution.ipynb'
    ]
    
    # Translate each notebook
    translated_count = 0
    for notebook in notebooks:
        notebook_path = os.path.join(base_dir, notebook)
        
        if os.path.exists(notebook_path):
            translate_notebook(notebook_path)
            translated_count += 1
        else:
            print(f"\n⚠ Warning: {notebook_path} not found, skipping...")
    
    print("\n" + "=" * 70)
    print(f"Translation complete! {translated_count}/{len(notebooks)} notebooks translated.")
    print("=" * 70)


if __name__ == '__main__':
    main()
