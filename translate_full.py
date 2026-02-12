#!/usr/bin/env python3
"""
Comprehensive Jupyter Notebook Translation Script
Translates all markdown cells and code comments from English to Spanish
"""

import json
import re
import os
import sys

# Comprehensive translation dictionary
TRANSLATIONS = {
    # Navigation and headers
    "Visit MIT Deep Learning": "Visita MIT Deep Learning",
    "Run in Google Colab": "Ejecutar en Google Colab",
    "View Source on GitHub": "Ver Código Fuente en GitHub",
    "Copyright Information": "Información de Derechos de Autor",
    
    # Main titles
    "Lab 1: Intro to PyTorch and Music Generation with RNNs": "Laboratorio 1: Introducción a PyTorch y Generación de Música con RNNs",
    "Lab 1: Intro to TensorFlow and Music Generation with RNNs": "Laboratorio 1: Introducción a TensorFlow y Generación de Música con RNNs",
    
    # Parts
    "Part 1: Intro to PyTorch": "Parte 1: Introducción a PyTorch",
    "Part 1: Intro to TensorFlow": "Parte 1: Introducción a TensorFlow",
    "Part 2: Music Generation with RNNs": "Parte 2: Generación de Música con RNNs",
    
    # Copyright
    "All Rights Reserved": "Todos los Derechos Reservados",
    "Licensed under the MIT License. You may not use this file except in compliance": "Licenciado bajo la Licencia MIT. No puedes usar este archivo excepto en cumplimiento",
    "with the License. Use and/or modification of this code outside of MIT Introduction": "con la Licencia. El uso y/o modificación de este código fuera de MIT Introduction",
    "to Deep Learning must reference:": "to Deep Learning debe hacer referencia a:",
    
    # Introduction paragraphs
    "In this lab, you'll get exposure to using": "En este laboratorio, obtendrás experiencia usando",
    "and learn how it can be used for deep learning.": "y aprenderás cómo se puede usar para aprendizaje profundo.",
    "Go through the code and run each cell.": "Revisa el código y ejecuta cada celda.",
    "Along the way, you'll encounter several": "En el camino, encontrarás varios bloques",
    "blocks -- follow the instructions to fill them out before running those cells and continuing.": "-- sigue las instrucciones para completarlos antes de ejecutar esas celdas y continuar.",
    
    # Installation sections
    "Install PyTorch": "Instalar PyTorch",
    "Install TensorFlow": "Instalar TensorFlow",
    "is a popular deep learning library known for its flexibility and ease of use.": "es una popular biblioteca de aprendizaje profundo conocida por su flexibilidad y facilidad de uso.",
    "Here we'll learn how computations are represented and how to define a simple neural network in": "Aquí aprenderemos cómo se representan los cálculos y cómo definir una red neuronal simple en",
    "For all the labs in Introduction to Deep Learning": "Para todos los laboratorios en Introducción al Aprendizaje Profundo",
    "there will be a": "habrá una versión de",
    "version available.": "disponible.",
    "Let's install": "Instalemos",
    "and a couple of dependencies.": "y un par de dependencias.",
    
    # Code comments - Package imports
    "Download and import the MIT Introduction to Deep Learning package": "Descargar e importar el paquete MIT Introduction to Deep Learning",
    "Import TensorFlow and other libraries for this lab": "Importar TensorFlow y otras bibliotecas para este laboratorio",
    
    # What is PyTorch/TensorFlow
    "What is PyTorch?": "¿Qué es PyTorch?",
    "What is TensorFlow?": "¿Qué es TensorFlow?",
    "is a machine learning library, like TensorFlow.": "es una biblioteca de aprendizaje automático, como TensorFlow.",
    "is a machine learning library, like PyTorch.": "es una biblioteca de aprendizaje automático, como PyTorch.",
    "At its core,": "En su núcleo,",
    "provides an interface for creating and manipulating": "proporciona una interfaz para crear y manipular",
    "which are data structures that you can think of as multi-dimensional arrays.": "que son estructuras de datos que puedes considerar como arreglos multidimensionales.",
    "Tensors are represented as n-dimensional arrays of base datatypes such as a string or integer --": "Los tensores se representan como arreglos n-dimensionales de tipos de datos base como cadenas o enteros --",
    "they provide a way to generalize vectors and matrices to higher dimensions.": "proporcionan una manera de generalizar vectores y matrices a dimensiones superiores.",
    "provides the ability to perform computation on these tensors, define neural networks, and train them efficiently.": "proporciona la capacidad de realizar cálculos en estos tensores, definir redes neuronales y entrenarlas eficientemente.",
    
    # Tensor properties
    "tensor defines its number of dimensions and the size of each dimension.": "tensor define su número de dimensiones y el tamaño de cada dimensión.",
    "tensor provides the number of dimensions": "tensor proporciona el número de dimensiones",
    "this is equivalent to the tensor's rank": "esto es equivalente al rango del tensor",
    "and you can also think of this as the tensor's order or degree.": "y también puedes pensar en esto como el orden o grado del tensor.",
    
    # Instructions
    "Let's start by creating some tensors and inspecting their properties:": "Comencemos creando algunos tensores e inspeccionando sus propiedades:",
    "Vectors and lists can be used to create 1-d tensors:": "Los vectores y listas se pueden usar para crear tensores 1-d:",
    "Next, let's create": "A continuación, vamos a crear",
    "and higher-rank tensors.": "y tensores de rango superior.",
    "In image processing and computer vision, we will use 4-d Tensors with dimensions corresponding to batch size, number of color channels, image height, and image width.": "En procesamiento de imágenes y visión por computadora, usaremos tensores 4-d con dimensiones correspondientes al tamaño del lote, número de canales de color, altura de imagen y ancho de imagen.",
    
    # Section headers (code comments)
    "Defining higher-order Tensors": "Definiendo tensores de orden superior",
    "Defining Tensor computations": "Definiendo cálculos de tensores",
    "Gradient computation": "Cálculo de gradientes",
    "Gradient computation with GradientTape": "Cálculo de gradientes con GradientTape",
    "Function minimization with autograd and gradient descent": "Minimización de funciones con autograd y descenso de gradiente",
    "Function minimization with automatic differentiation and SGD": "Minimización de funciones con diferenciación automática y SGD",
    "Defining a dense layer": "Definiendo una capa densa",
    "Defining a network Layer": "Definiendo una capa de red",
    "Defining a neural network using the PyTorch Sequential API": "Definiendo una red neuronal usando la API Secuencial de PyTorch",
    "Defining a neural network using the Sequential API": "Definiendo una red neuronal usando la API Secuencial",
    "Defining a model using subclassing": "Definiendo un modelo usando subclasificación",
    "Defining a model using subclassing and specifying custom behavior": "Definiendo un modelo usando subclasificación y especificando comportamiento personalizado",
    "Custom behavior with subclassing nn.Module": "Comportamiento personalizado con subclasificación de nn.Module",
    
    # Music generation sections
    "Define numerical representation of text": "Definir representación numérica del texto",
    "Vectorize the songs string": "Vectorizar la cadena de canciones",
    "Batch definition to create training examples": "Definición de lotes para crear ejemplos de entrenamiento",
    "Defining the RNN Model": "Definiendo el modelo RNN",
    "Defining the loss function": "Definiendo la función de pérdida",
    "Hyperparameter setting and optimization": "Configuración de hiperparámetros y optimización",
    "Define optimizer and training operation": "Definir optimizador y operación de entrenamiento",
    "Create a Comet experiment to track our training run": "Crear un experimento de Comet para rastrear nuestra ejecución de entrenamiento",
    "Prediction of a generated song": "Predicción de una canción generada",
    "Play back generated songs": "Reproducir canciones generadas",
    
    # TODO instructions
    "Define a 2-d Tensor": "Define un tensor 2-d",
    "Define a 4-d Tensor": "Define un tensor 4-d",
    "Define a 4-d Tensor.": "Define un tensor 4-d.",
    "Use torch.zeros to initialize a 4-d Tensor of zeros with size": "Usa torch.zeros para inicializar un tensor 4-d de ceros con tamaño",
    "Use tf.zeros to initialize a 4-d Tensor of zeros with size": "Usa tf.zeros para inicializar un tensor 4-d de ceros con tamaño",
    "You can think of this as": "Puedes pensar en esto como",
    "images where each image is RGB": "imágenes donde cada imagen es RGB",
    
    # Common words
    "TODO": "HACER",
    "Note:": "Nota:",
    "Example:": "Ejemplo:",
    "Exercise:": "Ejercicio:",
    "Solution": "Solución",
    "solution": "solución",
}

# Additional pattern-based translations
PATTERN_TRANSLATIONS = [
    (r'## ([\d.]+)', lambda m: f'## {m.group(1)}'),  # Keep section numbers
    (r'0\.(\d+)', lambda m: f'0.{m.group(1)}'),  # Keep subsection numbers
    (r'(\d+)\.(\d+)', lambda m: f'{m.group(1)}.{m.group(2)}'),  # Keep all numbers
]


def translate_text(text, is_code_comment=False):
    """
    Translate English text to Spanish
    Args:
        text: Text to translate
        is_code_comment: True if this is a code comment (preserves code-like syntax)
    """
    if not text or not text.strip():
        return text
    
    result = text
    
    # Apply direct translations (longest first to avoid partial matches)
    for eng_text, spa_text in sorted(TRANSLATIONS.items(), key=lambda x: -len(x[0])):
        result = result.replace(eng_text, spa_text)
    
    return result


def translate_code_cell(source_lines):
    """Translate comments in code cell while preserving code"""
    translated_lines = []
    
    for line in source_lines:
        stripped = line.lstrip()
        
        # Skip pip install commands
        if '!pip' in line or '!wget' in line or '!curl' in line:
            translated_lines.append(line)
            continue
        
        # Handle full-line comments
        if stripped.startswith('#'):
            indent = line[:len(line) - len(stripped)]
            comment_text = stripped[1:].strip()
            
            if comment_text:
                # Don't translate shebang or special markers
                if comment_text.startswith('!') or comment_text in ['TODO', '###', '####', '#####']:
                    translated_lines.append(line)
                else:
                    translated_comment = translate_text(comment_text, is_code_comment=True)
                    # Preserve newline if present
                    if line.endswith('\n'):
                        translated_lines.append(f"{indent}# {translated_comment}\n")
                    else:
                        translated_lines.append(f"{indent}# {translated_comment}")
            else:
                translated_lines.append(line)
        
        # Handle inline comments (be careful with strings)
        elif '#' in line:
            # Simple heuristic: if # appears after code and not in quotes
            in_string = False
            quote_char = None
            hash_pos = -1
            
            for i, char in enumerate(line):
                if char in ['"', "'"] and (i == 0 or line[i-1] != '\\'):
                    if not in_string:
                        in_string = True
                        quote_char = char
                    elif char == quote_char:
                        in_string = False
                        quote_char = None
                elif char == '#' and not in_string:
                    hash_pos = i
                    break
            
            if hash_pos > 0:
                code_part = line[:hash_pos]
                comment_part = line[hash_pos+1:].strip()
                
                if comment_part:
                    translated_comment = translate_text(comment_part, is_code_comment=True)
                    if line.endswith('\n'):
                        translated_lines.append(f"{code_part}# {translated_comment}\n")
                    else:
                        translated_lines.append(f"{code_part}# {translated_comment}")
                else:
                    translated_lines.append(line)
            else:
                translated_lines.append(line)
        else:
            # No comment, keep as is
            translated_lines.append(line)
    
    return translated_lines


def translate_notebook(filepath):
    """Translate a Jupyter notebook file in-place"""
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
                cell['source'] = [translate_text(line) for line in source]
            else:
                cell['source'] = translate_text(source)
            cells_translated += 1
        
        elif cell_type == 'code':
            # Translate code comments
            source = cell.get('source', [])
            if isinstance(source, list):
                cell['source'] = translate_code_cell(source)
            else:
                # Convert to list, translate, keep as string if it was a string
                lines = source.split('\n')
                translated = translate_code_cell([l + '\n' for l in lines[:-1]] + [lines[-1]])
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
    
    print("=" * 60)
    print("Jupyter Notebook Spanish Translation")
    print("=" * 60)
    
    success_count = 0
    for notebook_path in notebooks:
        if os.path.exists(notebook_path):
            if translate_notebook(notebook_path):
                success_count += 1
        else:
            print(f"  ✗ File not found: {notebook_path}")
    
    print("=" * 60)
    print(f"✓ Translation complete! {success_count}/{len(notebooks)} notebooks translated")
    print("=" * 60)
    
    return success_count == len(notebooks)


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
