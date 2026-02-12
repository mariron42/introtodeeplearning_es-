import os
import regex as re
import subprocess
import urllib
import numpy as np
import tensorflow as tf

from IPython.display import Audio


cwd = os.path.dirname(__file__)


def load_training_data():
    with open(os.path.join(cwd, "data", "irish.abc"), "r") as f:
        text = f.read()
    songs = extract_song_snippet(text)
    return songs


def extract_song_snippet(text):
    pattern = "(^|\n\n)(.*?)\n\n"
    search_results = re.findall(pattern, text, overlapped=True, flags=re.DOTALL)
    songs = [song[1] for song in search_results]
    print("Se encontraron {} canciones en el texto".format(len(songs)))
    return songs


def save_song_to_abc(song, filename="tmp"):
    save_name = "{}.abc".format(filename)
    with open(save_name, "w") as f:
        f.write(song)
    return filename


def abc2wav(abc_file):
    path_to_tool = os.path.join(cwd, "bin", "abc2wav")
    cmd = "{} {}".format(path_to_tool, abc_file)
    return os.system(cmd)


def play_wav(wav_file):
    return Audio(wav_file)


def play_song(song):
    basename = save_song_to_abc(song)
    ret = abc2wav(basename + ".abc")
    if ret == 0:  # no tuvo éxito
        return play_wav(basename + ".wav")
    return None


def play_generated_song(generated_text):
    songs = extract_song_snippet(generated_text)
    if len(songs) == 0:
        print(
            "No se encontraron canciones válidas en el texto generado. \
            ¡Intenta entrenar el modelo por más tiempo o aumentar la cantidad de música \
            generada para asegurar que se generen canciones completas!"
        )

    for song in songs:
        play_song(song)
    print(
        "Ninguna de las canciones fue válida, intenta entrenar por más tiempo para \
        mejorar la sintaxis."
    )


def test_batch_func_types(func, args):
    ret = func(*args)
    assert len(ret) == 2, "[FALLO] get_batch debe devolver dos argumentos (entrada y etiqueta)"
    assert type(ret[0]) == np.ndarray, "[FALLO] test_batch_func_types: x no es np.array"
    assert type(ret[1]) == np.ndarray, "[FALLO] test_batch_func_types: y no es np.array"
    print("[APROBADO] test_batch_func_types")
    return True


def test_batch_func_shapes(func, args):
    dataset, seq_length, batch_size = args
    x, y = func(*args)
    correct = (batch_size, seq_length)
    assert (
        x.shape == correct
    ), "[FALLO] test_batch_func_shapes: x {} no tiene la forma correcta {}".format(
        x.shape, correct
    )
    assert (
        y.shape == correct
    ), "[FALLO] test_batch_func_shapes: y {} no tiene la forma correcta {}".format(
        y.shape, correct
    )
    print("[APROBADO] test_batch_func_shapes")
    return True


def test_batch_func_next_step(func, args):
    x, y = func(*args)
    assert (
        x[:, 1:] == y[:, :-1]
    ).all(), "[FALLO] test_batch_func_next_step: x_{t} debe ser igual a y_{t-1} para todo t"
    print("[APROBADO] test_batch_func_next_step")
    return True


def test_custom_dense_layer_output(y):
    # definir el valor de referencia (ground truth) para el arreglo
    true_y = np.array([[0.27064407, 0.1826951, 0.50374055]], dtype="float32")
    assert tf.shape(y).numpy().tolist() == list(
        true_y.shape
    ), "[FALLO] la salida tiene una forma incorrecta. se esperaba {} pero se obtuvo {}".format(
        true_y.shape, y.numpy().shape
    )
    np.testing.assert_almost_equal(
        y.numpy(),
        true_y,
        decimal=7,
        err_msg="[FALLO] la salida tiene un valor incorrecto. se esperaba {} pero se obtuvo {}".format(
            true_y, y.numpy()
        ),
        verbose=True,
    )
    print("[APROBADO] test_custom_dense_layer_output")
    return True
