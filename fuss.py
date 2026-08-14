import tensorflow as tf
import numpy as np
classifierLoad = tf.keras.models.load_model('predict.pkl')


data = np.array([[8.4,8.9,3.9,5.1]])
my_prediction = classifierLoad.predict(data)
print(my_prediction)

print(my_prediction)
ind = np.argmax(my_prediction)
print(ind)