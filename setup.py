from pkg_resources import DistributionNotFound, get_distribution
from distutils.core import setup


def get_dist(pkgname):
    try:
        return get_distribution(pkgname)
    except DistributionNotFound:
        return None

install_deps = [
    'comet_ml',
    'numpy',
    'regex',
    'tqdm',
    'gym',
    'opik',
    'openai',
    'transformers',
    'datasets',
    'peft',
    'lion-pytorch',
]
tf_ver = '2.0.0a'
if get_dist('tensorflow>='+tf_ver) is None and get_dist('tensorflow_gpu>='+tf_ver) is None:
    install_deps.append('tensorflow>='+tf_ver)

setup(
  name = 'mitdeeplearning',         # Nombre de la carpeta de tu paquete (MyLib)
  packages = ['mitdeeplearning'],   # Elige el mismo que "name"
  version = '0.7.5',      # Comienza con un número pequeño y auméntalo con cada cambio que hagas
  license='MIT',        # Elige una licencia de aquí: https://help.github.com/articles/licensing-a-repository
  description = 'Official software labs for MIT Introduction to Deep Learning (http://introtodeeplearning.com)',   # Da una breve descripción sobre tu biblioteca
  author = 'Alexander Amini',                   # Escribe tu nombre
  author_email = 'introtodeeplearning-staff@mit.edu',      # Escribe tu correo electrónico
  url = 'http://introtodeeplearning.com',   # Proporciona el enlace a tu github o a tu sitio web
  download_url = 'https://github.com/MITDeepLearning/introtodeeplearning/archive/v0.7.5.tar.gz',    # Esto lo explico más adelante
  keywords = ['deep learning', 'neural networks', 'tensorflow', 'introduction'],   # Palabras clave que mejor definen tu paquete
  install_requires=install_deps,
  classifiers=[
    'Development Status :: 3 - Alpha',      # Elige "3 - Alpha", "4 - Beta" o "5 - Production/Stable" como el estado actual de tu paquete
    'License :: OSI Approved :: MIT License',   # De nuevo, elige una licencia
    'Programming Language :: Python :: 3',      #Especifica qué versiones de Python deseas soportar
    'Programming Language :: Python :: 3.6',
  ],
  package_data={
      'mitdeeplearning': ['bin/*', 'data/*', 'data/text_styles/*', 'data/faces/DF/*', 'data/faces/DM/*', 'data/faces/LF/*', 'data/faces/LM/*'],
   },

)
