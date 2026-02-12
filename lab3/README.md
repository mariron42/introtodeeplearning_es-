# MIT 6.S191 Laboratorio 3: ¡Ajustar un LLM, debes!

![yoda](https://github.com/MITDeepLearning/introtodeeplearning/raw/2025/lab3/img/yoda_wallpaper.jpg)
En este laboratorio, realizarás el ajuste fino (fine-tuning) de un modelo de lenguaje grande (LLM) de varios miles de millones de parámetros. Recorreremos varios conceptos fundamentales de los LLMs, incluyendo tokenización, plantillas y ajuste fino (fine-tuning). Este laboratorio proporciona un pipeline completo para el ajuste fino de un modelo de lenguaje para generar respuestas en un estilo específico, y explorarás no solo el ajuste fino de modelos de lenguaje, sino también formas de evaluar el rendimiento de un modelo de lenguaje.

Utilizarás el modelo [LFM2-1.2B](https://www.liquid.ai/liquid-foundation-models) de [Liquid AI](https://www.liquid.ai/) como modelo de lenguaje base para el ajuste fino; [Gemini 2.5](https://huggingface.co/google/gemma-2b-it) de Google como modelo "juez" de evaluación; y [Opik](https://www.comet.com/site/products/opik/) de Comet ML como marco para la evaluación simplificada de LLMs.
