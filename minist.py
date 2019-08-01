import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# print(x_train.shape, y_train.shape)

x_train, x_test = x_train / 255 , x_test/255

modle = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, ))
    ]
)