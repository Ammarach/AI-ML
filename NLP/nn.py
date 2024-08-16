import tensorflow as tf
from tensorflow import keras
#from keras.models import Sequential
#from keras.layers import Dense



def build_discriminator(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy']):
    model = tf.keras.models.Sequential()

    #input layer
    model.add(tf.keras.models.Dense(128, activation = 'relu', input_shape=(1, )))

    #Hidden Layers
    model.add(tf.keras.models.Dense(64, activstion = 'relu'))
    model.add(tf.keras.models.Dense(32, activstion = 'relu'))

    #output Layer
    model.add(tf.keras.models.Dense(1, activation = 'sigmoid'))

    #compile the model 
    model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    return model