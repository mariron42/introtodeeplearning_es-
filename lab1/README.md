# MIT 6.S191 Laboratorio 1: Introducción al Deep Learning en Python y Generación de Música con RNNs

![alt text](https://github.com/MITDeepLearning/introtodeeplearning/raw/master/lab1/img/music_waveform.png)
## Parte 1: Introducción al Deep Learning en Python -- TensorFlow y PyTorch
TensorFlow ("TF") y PyTorch ("PT") son bibliotecas de software utilizadas en aprendizaje automático. Aquí aprenderemos cómo se representan los cálculos y cómo definir redes neuronales simples en TensorFlow y PyTorch. Los laboratorios de TensorFlow tendrán el prefijo `TF`; los laboratorios de PyTorch tendrán el prefijo `PT`.

TensorFlow utiliza una API de alto nivel llamada [Keras](https://www.tensorflow.org/guide/keras) que proporciona un marco potente e intuitivo para construir y entrenar modelos de aprendizaje profundo. En la Introducción a TensorFlow (`TF_Part1_Intro`) aprenderás los fundamentos de los cálculos en TensorFlow, la API de Keras y el estilo de ejecución imperativa de TensorFlow 2.0.

[PyTorch](https://pytorch.org/) es una biblioteca popular de aprendizaje profundo conocida por su flexibilidad, facilidad de uso y ejecución dinámica. En la Introducción a PyTorch (`PT_Part1_Intro`) aprenderás los fundamentos de los cálculos en PyTorch y cómo definir redes neuronales usando la API secuencial y `torch.nn.Module`.

## Parte 2: Generación de Música con RNNs
En la segunda parte del laboratorio, experimentaremos con la construcción de una Red Neuronal Recurrente (RNN) para la generación de música. Utilizaremos una "RNN de caracteres" para predecir el siguiente carácter de partituras musicales en notación ABC. Finalmente, tomaremos muestras de este modelo para generar un archivo de música completamente nuevo que nunca se ha escuchado antes.

