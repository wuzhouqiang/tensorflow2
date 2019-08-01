import numpy as np
import tensorflow as tf

a = np.arange(31)
b = tf.range(3)
print(a.dtype)
print(b.numpy())

print(tf.is_tensor(b))
print(int(b))
