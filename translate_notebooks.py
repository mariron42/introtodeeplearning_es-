#!/usr/bin/env python3
"""
Script to translate Jupyter notebooks to Spanish.
Translates markdown cells and code comments while preserving code structure.
"""

import json
import re
import sys

def get_comprehensive_translations():
    """Returns comprehensive translation dictionary"""
    return {
        # Headers and Navigation
        "Visit MIT Deep Learning": "Visita MIT Deep Learning",
        "Run in Google Colab": "Ejecutar en Google Colab",
        "View Source on GitHub": "Ver Código Fuente en GitHub",
        "Copyright Information": "Información de Derechos de Autor",
        
        # Lab titles
        "Lab 1: Intro to PyTorch and Music Generation with RNNs": "Laboratorio 1: Introducción a PyTorch y Generación de Música con RNNs",
        "Lab 1: Intro to TensorFlow and Music Generation with RNNs": "Laboratorio 1: Introducción a TensorFlow y Generación de Música con RNNs",
        "Part 1: Intro to PyTorch": "Parte 1: Introducción a PyTorch",
        "Part 1: Intro to TensorFlow": "Parte 1: Introducción a TensorFlow",
        "Part 2: Music Generation with RNNs": "Parte 2: Generación de Música con RNNs",
        
        # Copyright
        "All Rights Reserved": "Todos los Derechos Reservados",
        "Licensed under the MIT License. You may not use this file except in compliance": "Licenciado bajo la Licencia MIT. No puedes usar este archivo excepto en cumplimiento",
        "with the License. Use and/or modification of this code outside of MIT Introduction": "con la Licencia. El uso y/o modificación de este código fuera de MIT Introduction",
        "to Deep Learning must reference:": "to Deep Learning debe hacer referencia a:",
        
        # Introduction
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
        
        # Code comments - Common
        "Download and import the MIT Introduction to Deep Learning package": "Descargar e importar el paquete MIT Introduction to Deep Learning",
        "Import TensorFlow and other libraries for this lab": "Importar TensorFlow y otras bibliotecas para este laboratorio",
        "Import PyTorch and other libraries for this lab": "Importar PyTorch y otras bibliotecas para este laboratorio",
        
        # What is PyTorch/TensorFlow
        "What is PyTorch?": "¿Qué es PyTorch?",
        "What is TensorFlow?": "¿Qué es TensorFlow?",
        "is a machine learning library": "es una biblioteca de aprendizaje automático",
        "At its core,": "En su núcleo,",
        "provides an interface for creating and manipulating": "proporciona una interfaz para crear y manipular",
        "which are data structures that you can think of as multi-dimensional arrays.": "que son estructuras de datos que puedes considerar como arreglos multidimensionales.",
        "Tensors are represented as n-dimensional arrays of base datatypes such as a string or integer": "Los tensores se representan como arreglos n-dimensionales de tipos de datos base como cadenas o enteros",
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
        
        # TODO blocks
        "Defining higher-order Tensors": "Definiendo tensores de orden superior",
        "Define a 2-d Tensor": "Define un tensor 2-d",
        "Define a 4-d Tensor": "Define un tensor 4-d",
        "Use torch.zeros to initialize a 4-d Tensor of zeros with size": "Usa torch.zeros para inicializar un tensor 4-d de ceros con tamaño",
        "Use tf.zeros to initialize a 4-d Tensor of zeros with size": "Usa tf.zeros para inicializar un tensor 4-d de ceros con tamaño",
        "You can think of this as": "Puedes pensar en esto como",
        "images where each image is RGB": "imágenes donde cada imagen es RGB",
        
        # Common words and phrases
        "matrix": "matriz",
        "matrices": "matrices", 
        "vector": "vector",
        "vectors": "vectores",
        "tensor": "tensor",
        "tensors": "tensores",
        "Note:": "Nota:",
        "Example:": "Ejemplo:",
        "Exercise:": "Ejercicio:",
        "Solution:": "Solución:",
    }

TRANSLATIONS = get_comprehensive_translations()

def translate_text(text):
    """
    Translate English text to Spanish.
    This is a simplified translation - for production use an API like DeepL or Google Translate.
    """
    if not text or not text.strip():
        return text
    
    # First, apply direct translations from dictionary
    result = text
    for eng, esp in TRANSLATIONS.items():
        result = result.replace(eng, esp)
    
    # Common patterns
    patterns = [
        (r'\bLab (\d+):', r'Laboratorio \1:'),
        (r'\bPart (\d+):', r'Parte \1:'),
        (r'\bSection (\d+)\.(\d+)', r'Sección \1.\2'),
        (r'\btodo\b', r'HACER', flags=re.IGNORECASE),
        (r'\bTODO\b', r'HACER'),
        (r'\bNote:', r'Nota:'),
        (r'\bExample:', r'Ejemplo:'),
        (r'\bExercise:', r'Ejercicio:'),
    ]
    
    for pattern, replacement in patterns:
        flags = pattern[2] if len(pattern) > 2 else 0
        result = re.sub(pattern if len(pattern) == 2 else pattern[0], 
                       replacement if len(pattern) == 2 else replacement, 
                       result, 
                       flags=flags if flags else 0)
    
    return result

def translate_code_comments(code):
    """
    Translate comments in code (lines starting with #) while preserving code.
    """
    if not code:
        return code
    
    lines = code.split('\n')
    translated_lines = []
    
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('#'):
            # This is a comment line
            indent = line[:len(line) - len(stripped)]
            comment = stripped[1:].strip()
            if comment:
                translated_comment = translate_text(comment)
                translated_lines.append(f"{indent}# {translated_comment}")
            else:
                translated_lines.append(line)
        else:
            # Check for inline comments
            if '#' in line:
                code_part, comment_part = line.split('#', 1)
                comment = comment_part.strip()
                if comment:
                    translated_comment = translate_text(comment)
                    translated_lines.append(f"{code_part}# {translated_comment}")
                else:
                    translated_lines.append(line)
            else:
                translated_lines.append(line)
    
    return '\n'.join(translated_lines)

def translate_notebook(input_path, output_path=None):
    """
    Translate a Jupyter notebook to Spanish.
    """
    if output_path is None:
        output_path = input_path
    
    print(f"Translating {input_path}...")
    
    # Load notebook
    with open(input_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Translate cells
    for cell in notebook.get('cells', []):
        if cell['cell_type'] == 'markdown':
            # Translate markdown content
            if 'source' in cell:
                if isinstance(cell['source'], list):
                    cell['source'] = [translate_text(line) for line in cell['source']]
                else:
                    cell['source'] = translate_text(cell['source'])
        
        elif cell['cell_type'] == 'code':
            # Translate comments in code
            if 'source' in cell:
                if isinstance(cell['source'], list):
                    # Join, translate, then split back
                    code = ''.join(cell['source'])
                    translated = translate_code_comments(code)
                    # Preserve the line structure
                    cell['source'] = [translated]
                else:
                    cell['source'] = translate_code_comments(cell['source'])
    
    # Save notebook
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=2)
    
    print(f"  ✓ Saved to {output_path}")

def main():
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
    
    for notebook_path in notebooks:
        try:
            translate_notebook(notebook_path)
        except Exception as e:
            print(f"  ✗ Error translating {notebook_path}: {e}")
            sys.exit(1)
    
    print("\n✓ All notebooks translated successfully!")

if __name__ == "__main__":
    main()
