import tensorflow as tf
from tensorflow import keras


lr = 1e-3
batchsz = 256
epochs = 50

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
# print(x_train.shape, y_train.shape)  # (60000, 28, 28) (60000,)

x_train = x_train.reshape(60000, 28, 28, 1)
x_test = x_test.reshape(10000, 28, 28, 1)

x_train = x_train / 255
x_test = x_test / 255

train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(batchsz)
test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(batchsz)


model = keras.models.Sequential()

model.add(keras.layers.Conv2D(filters=32, kernel_size=(3, 3), input_shape=(28, 28, 1), activation='relu', ))
model.add(keras.layers.MaxPooling2D((2, 2)))
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D((2, 2)))
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))

model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(10, activation='softmax'))

print(model.summary())

model.compile(optimizer=tf.keras.optimizers.Adam(lr=lr),
              loss=tf.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

model.fit(train_ds, epochs=epochs)
model.evaluate(test_ds)