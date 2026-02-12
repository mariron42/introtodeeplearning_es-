# MIT 6.S191 Lab 1: Intro to Deep Learning in Python and Music Generation with RNNs

![alt text](https://github.com/MITDeepLearning/introtodeeplearning/raw/master/lab1/img/music_waveform.png)
## Part 1: Intro to Deep Learning in Python -- TensorFlow and PyTorch
TensorFlow ("TF") and PyTorch ("PT") are software libraries used in machine learning. Here we'll learn how computations are represented and how to define simple neural networks in TensorFlow and PyTorch. The TensorFlow labs will be prefixed by `TF`; PyTorch labs will be prefixed by `PT`.

TensorFlow uses a high-level API called [Keras](https://www.tensorflow.org/guide/keras) that provides a powerful, intuitive framework for building and training deep learning models. In the TensorFlow Intro (`TF_Part1_Intro`) you will learn the basics of computations in TensorFlow, the Keras API, and TensorFlow 2.0's imperative execution style.

[PyTorch](https://pytorch.org/) is a popular deep learning library known for its flexibility, ease of use, and dynamic execution. In the PyTorch Intro (`PT_Part1_Intro`) you will learn the basics of computations in PyTorch and how to define neural networks using either the sequential API and `torch.nn.Module`.

## Part 2: Music Generation with RNNs
In the second portion of the lab, we will play around with building a Recurrent Neural Network (RNN) for music generation. We will be using a "character RNN" to predict the next character of sheet music in ABC notation. Finally, we will sample from this model to generate a brand new music file that has never been heard before!

