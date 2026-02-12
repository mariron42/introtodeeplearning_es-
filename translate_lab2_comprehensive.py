#!/usr/bin/env python3
"""
Comprehensive Jupyter Notebook Translation Script for Lab2
Translates ALL markdown cells and code comments from English to Spanish
"""

import json
import re
import os
import sys


def get_comprehensive_translations():
    """
    Returns comprehensive translation dictionary for Lab2
    """
    return {
        # ========== NAVIGATION AND BADGES ==========
        "Visit MIT Deep Learning": "Visita MIT Deep Learning",
        "Run in Google Colab": "Ejecutar en Google Colab",
        "View Source on GitHub": "Ver Código Fuente en GitHub",
        "Copyright Information": "Información de Derechos de Autor",
        
        # ========== MAIN TITLES ==========
        "Laboratory 2: Computer Vision": "Laboratorio 2: Visión por Computadora",
        "Part 1: MNIST Digit Classification": "Parte 1: Clasificación de Dígitos MNIST",
        "Part 2: Debiasing Facial Detection Systems": "Parte 2: Eliminación de Sesgos en Sistemas de Detección Facial",
        
        # ========== COPYRIGHT ==========
        "All Rights Reserved": "Todos los Derechos Reservados",
        "Licensed under the MIT License. You may not use this file except in compliance": "Licenciado bajo la Licencia MIT. No puedes usar este archivo excepto en cumplimiento",
        "with the License. Use and/or modification of this code outside of MIT Introduction": "con la Licencia. El uso y/o modificación de este código fuera de MIT Introduction",
        "to Deep Learning must reference:": "to Deep Learning debe hacer referencia a:",
        
        # ========== SECTION HEADERS ==========
        "## 0.1 Setup and Imports": "## 0.1 Configuración e Importaciones",
        "## 0.2 MNIST Data": "## 0.2 Datos MNIST",
        "## 1.1 Fully Connected Neural Networks": "## 1.1 Redes Neuronales Completamente Conectadas",
        "## 1.2 Training the Model": "## 1.2 Entrenamiento del Modelo",
        "## 1.3 Results and Performance": "## 1.3 Resultados y Rendimiento",
        "## 2.1 Convolutional Neural Networks (CNNs)": "## 2.1 Redes Neuronales Convolucionales (CNN)",
        "## 2.2 Training the CNN": "## 2.2 Entrenamiento de la CNN",
        "## 2.3 CNN Results": "## 2.3 Resultados de la CNN",
        
        # Part 2 sections
        "## 0.1 Comet Setup": "## 0.1 Configuración de Comet",
        "## 0.2 Import Packages": "## 0.2 Importar Paquetes",
        "## 1.1 Setup and Imports": "## 1.1 Configuración e Importaciones",
        "## 1.2 CelebA Dataset": "## 1.2 Conjunto de Datos CelebA",
        "## 1.3 Exploring Bias in Data": "## 1.3 Exploración de Sesgos en los Datos",
        "## 2.1 Variational Autoencoder (VAE)": "## 2.1 Autocodificador Variacional (VAE)",
        "## 2.2 VAE Loss Function": "## 2.2 Función de Pérdida del VAE",
        "## 2.3 Training the VAE": "## 2.3 Entrenamiento del VAE",
        "## 3.1 DB-VAE for Debiasing": "## 3.1 DB-VAE para Eliminar Sesgos",
        "## 3.2 DB-VAE Loss Function": "## 3.2 Función de Pérdida del DB-VAE",
        "## 3.3 Training the DB-VAE": "## 3.3 Entrenamiento del DB-VAE",
        "## 4.1 Comparison": "## 4.1 Comparación",
        
        # ========== INTRODUCTION PARAGRAPHS ==========
        "In the first portion of this lab, we will build and train a convolutional neural network (CNN) for classification of handwritten digits from the famous": "En la primera parte de este laboratorio, construiremos y entrenaremos una red neuronal convolucional (CNN) para clasificación de dígitos escritos a mano del famoso conjunto de datos",
        "dataset. The MNIST dataset consists of 60,000 training images and 10,000 test images. Our classes are the digits 0-9.": "El conjunto de datos MNIST consiste de 60,000 imágenes de entrenamiento y 10,000 imágenes de prueba. Nuestras clases son los dígitos 0-9.",
        "First, let's download the course repository, install dependencies, and import the relevant packages we'll need for this lab.": "Primero, descarguemos el repositorio del curso, instalemos las dependencias e importemos los paquetes relevantes que necesitaremos para este laboratorio.",
        
        # ========== COMMON PHRASES ==========
        "Let's start by defining some functions that will be useful throughout this notebook.": "Comencemos definiendo algunas funciones que serán útiles a lo largo de este cuaderno.",
        "We'll begin by defining some hyperparameters for the model.": "Comenzaremos definiendo algunos hiperparámetros para el modelo.",
        "Now we can define our model architecture.": "Ahora podemos definir la arquitectura de nuestro modelo.",
        "Let's visualize some examples from the dataset.": "Visualicemos algunos ejemplos del conjunto de datos.",
        "We can now train the model.": "Ahora podemos entrenar el modelo.",
        "Let's evaluate the model on the test set.": "Evaluemos el modelo en el conjunto de prueba.",
        "Now let's look at the results.": "Ahora veamos los resultados.",
        
        # ========== CODE COMMENTS ==========
        # Setup and installation
        "Download the course repository": "Descargar el repositorio del curso",
        "Install dependencies": "Instalar dependencias",
        "Import packages": "Importar paquetes",
        "Import TensorFlow and other libraries": "Importar TensorFlow y otras bibliotecas",
        "Import PyTorch and other libraries": "Importar PyTorch y otras bibliotecas",
        
        # Data loading
        "Load and preprocess the MNIST dataset": "Cargar y preprocesar el conjunto de datos MNIST",
        "Load the data": "Cargar los datos",
        "Normalize the data": "Normalizar los datos",
        "Preprocess the data": "Preprocesar los datos",
        "Create data loaders": "Crear cargadores de datos",
        "Split into train and test sets": "Dividir en conjuntos de entrenamiento y prueba",
        
        # Model definition
        "Define the model": "Definir el modelo",
        "Define the neural network": "Definir la red neuronal",
        "Define fully connected layers": "Definir capas completamente conectadas",
        "Define convolutional layers": "Definir capas convolucionales",
        "Add dropout for regularization": "Agregar dropout para regularización",
        "Define forward pass": "Definir paso hacia adelante",
        
        # Training
        "Define loss function": "Definir función de pérdida",
        "Define optimizer": "Definir optimizador",
        "Training loop": "Bucle de entrenamiento",
        "Train the model": "Entrenar el modelo",
        "Forward pass": "Paso hacia adelante",
        "Backward pass": "Paso hacia atrás",
        "Update weights": "Actualizar pesos",
        "Calculate loss": "Calcular pérdida",
        "Compute gradients": "Calcular gradientes",
        
        # Evaluation
        "Evaluate on test set": "Evaluar en conjunto de prueba",
        "Calculate accuracy": "Calcular precisión",
        "Make predictions": "Hacer predicciones",
        "Visualize results": "Visualizar resultados",
        "Plot examples": "Graficar ejemplos",
        
        # Debiasing specific
        "Train the VAE": "Entrenar el VAE",
        "Train the DB-VAE": "Entrenar el DB-VAE",
        "Encode images": "Codificar imágenes",
        "Decode images": "Decodificar imágenes",
        "Reconstruct images": "Reconstruir imágenes",
        "Sample from latent space": "Muestrear del espacio latente",
        "Calculate reconstruction loss": "Calcular pérdida de reconstrucción",
        "Calculate KL divergence": "Calcular divergencia KL",
        
        # ========== FULL SENTENCES ==========
        "Define a simple fully connected neural network for MNIST classification.": "Definir una red neuronal completamente conectada simple para clasificación MNIST.",
        "Define a convolutional neural network for MNIST classification.": "Definir una red neuronal convolucional para clasificación MNIST.",
        "The model takes as input a 28x28 grayscale image and outputs a probability distribution over the 10 digit classes.": "El modelo toma como entrada una imagen en escala de grises de 28x28 y produce una distribución de probabilidad sobre las 10 clases de dígitos.",
        "We use cross-entropy loss for multi-class classification.": "Usamos pérdida de entropía cruzada para clasificación multi-clase.",
        "We use the Adam optimizer with a learning rate of 0.001.": "Usamos el optimizador Adam con una tasa de aprendizaje de 0.001.",
        
        # Dataset exploration
        "Let's explore the MNIST dataset by visualizing some samples.": "Exploremos el conjunto de datos MNIST visualizando algunas muestras.",
        "Each image is 28x28 pixels and represents a handwritten digit from 0-9.": "Cada imagen es de 28x28 píxeles y representa un dígito escrito a mano del 0-9.",
        "The dataset is already split into training and test sets.": "El conjunto de datos ya está dividido en conjuntos de entrenamiento y prueba.",
        
        # Training process
        "We train for a fixed number of epochs, monitoring the loss at each step.": "Entrenamos por un número fijo de épocas, monitoreando la pérdida en cada paso.",
        "During training, we perform forward and backward passes, updating the model weights using gradient descent.": "Durante el entrenamiento, realizamos pasos hacia adelante y hacia atrás, actualizando los pesos del modelo usando descenso de gradiente.",
        
        # Results
        "After training, we can evaluate the model's performance on the test set.": "Después del entrenamiento, podemos evaluar el rendimiento del modelo en el conjunto de prueba.",
        "The convolutional neural network should achieve higher accuracy than the fully connected network.": "La red neuronal convolucional debería lograr mayor precisión que la red completamente conectada.",
        
        # Debiasing
        "In this section, we will explore bias in facial detection systems and learn how to mitigate it.": "En esta sección, exploraremos el sesgo en sistemas de detección facial y aprenderemos cómo mitigarlo.",
        "We will use the CelebA dataset, which contains images of celebrity faces with various attributes.": "Usaremos el conjunto de datos CelebA, que contiene imágenes de rostros de celebridades con varios atributos.",
        "We will build a Variational Autoencoder (VAE) to learn a latent representation of faces.": "Construiremos un Autocodificador Variacional (VAE) para aprender una representación latente de rostros.",
        "Then, we will modify the VAE to create a debiased version (DB-VAE) that reduces bias in the learned representations.": "Luego, modificaremos el VAE para crear una versión sin sesgos (DB-VAE) que reduce el sesgo en las representaciones aprendidas.",
    }


def translate_code_comments(code):
    """Translate comments in code cells"""
    translations = get_comprehensive_translations()
    lines = code.split('\n')
    translated_lines = []
    
    for line in lines:
        # Check if line contains a comment
        if '#' in line:
            # Split at the first # to preserve code before comment
            parts = line.split('#', 1)
            if len(parts) == 2:
                code_part = parts[0]
                comment_part = parts[1]
                
                # Translate the comment part
                translated_comment = comment_part
                for eng, esp in translations.items():
                    # Use word boundaries for better matching
                    if eng.lower() in comment_part.lower():
                        # Case-insensitive replacement
                        pattern = re.compile(re.escape(eng), re.IGNORECASE)
                        translated_comment = pattern.sub(esp, translated_comment)
                
                translated_lines.append(code_part + '#' + translated_comment)
            else:
                translated_lines.append(line)
        else:
            translated_lines.append(line)
    
    return '\n'.join(translated_lines)


def translate_markdown(text):
    """Translate markdown text"""
    translations = get_comprehensive_translations()
    translated = text
    
    # Sort by length (longest first) to avoid partial replacements
    sorted_translations = sorted(translations.items(), key=lambda x: len(x[0]), reverse=True)
    
    for eng, esp in sorted_translations:
        # Skip if already contains Spanish translation
        if esp in translated:
            continue
        # Use case-sensitive replacement for markdown
        translated = translated.replace(eng, esp)
    
    return translated


def translate_notebook(input_path, output_path):
    """Translate a Jupyter notebook"""
    print(f"Translating {input_path}...")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Translate each cell
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            # Translate markdown cells
            if 'source' in cell:
                if isinstance(cell['source'], list):
                    cell['source'] = [translate_markdown(line) for line in cell['source']]
                else:
                    cell['source'] = translate_markdown(cell['source'])
        
        elif cell['cell_type'] == 'code':
            # Translate code comments
            if 'source' in cell:
                if isinstance(cell['source'], list):
                    code = ''.join(cell['source'])
                    translated_code = translate_code_comments(code)
                    # Split back into lines preserving original structure
                    cell['source'] = [translated_code[i:i+1] if i < len(translated_code) else '' 
                                     for i in range(len(cell['source']))]
                    # Better approach: split by newlines but preserve structure
                    translated_lines = translated_code.split('\n')
                    if len(translated_lines) > 0:
                        cell['source'] = [line + '\n' if i < len(translated_lines) - 1 else line 
                                         for i, line in enumerate(translated_lines)]
                else:
                    cell['source'] = translate_code_comments(cell['source'])
    
    # Write translated notebook
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=2)
    
    print(f"Saved translated notebook to {output_path}")


def main():
    """Main function"""
    lab2_dir = '/home/runner/work/introtodeeplearning_es-/introtodeeplearning_es-/lab2'
    
    # Notebooks to translate
    notebooks = [
        'PT_Part1_MNIST.ipynb',
        'PT_Part2_Debiasing.ipynb',
        'solutions/PT_Part1_MNIST_Solution.ipynb',
        'solutions/PT_Part2_Debiasing_Solution.ipynb'
    ]
    
    for notebook in notebooks:
        input_path = os.path.join(lab2_dir, notebook)
        output_path = input_path  # Overwrite original
        
        if os.path.exists(input_path):
            translate_notebook(input_path, output_path)
        else:
            print(f"Warning: {input_path} not found, skipping...")
    
    print("\nAll Lab2 notebooks translated successfully!")


if __name__ == '__main__':
    main()
