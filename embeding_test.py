import tensorflow as tf
import tensorflow.python.keras as keras
import pandas as pd


(x_train, y_train), (x_test, y_test) = keras.datasets.imdb.load_data(num_words=10000)

x_train = keras.preprocessing.sequence.pad_sequences(x_train, maxlen=80)

print(x_train.shape, y_train.shape)



