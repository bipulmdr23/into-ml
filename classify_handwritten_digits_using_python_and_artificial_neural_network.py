# -*- coding: utf-8 -*-
"""Classify handwritten digits using python and artificial neural network.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15XlgQvyieaLtHduf_F11cXT6sgfRe9vM
"""

! pip install tensorflow keras numpy mnist matplotlib

import matplotlib.pyplot as plt # Graph
import numpy as np
from keras.models import Sequential #ANN architecture
from keras.layers import Dense #The layers in the ANN
from keras.utils import to_categorical
import pandas as pd
import numpy as np
import mnist # Get dataset from

#Load the dataset
train_images = mnist.train_images() # training data images
train_labels = mnist.train_labels() # training data labels
test_images = mnist.test_images() # training data images
test_labels = mnist.test_labels() # training data labels

# Normalize the images the pixel values from [0 ,255]
#[-0.5, 0.5] to make our netwok eaiser to train
train_images = (train_images/255) - 0.5
test_images = (test_images/255) -0.5
#Flatten the images. Flatten each 28x28 image into 28^2 = 784 dimensional vector
#to pass into the neural network
train_images = train_images.reshape((-1,784))
test_images = test_images.reshape((-1,784))
#Print the shape
print(train_images.shape) #60,000 rows and 784 cols
print(test_images.shape) #10,000 rows and 784 cols

#Build the model
# 3 layers, 2layes with 64 neurons and the relu function
# 1 layer with 10 neurons and softmax function
model = Sequential()
model.add( Dense(64, activation='relu', input_dim=784))
model.add( Dense(64, activation='relu'))
model.add( Dense(10, activation='softmax'))

#Compile the model
#The loss function measures how well the model did on training , and then tries
#to improve on it using the optmizer
model.compile(
    optimizer='adam',
      loss = 'categorical_crossentropy', #(classes that are greater than 2)
      metrics = ['accuracy']
)

#Train the model
model.fit(
    train_images,
      to_categorical(train_labels), # Ex. 2 it expects [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
      epochs = 5, # The number of iterations over the entire dataset to train on
      batch_size = 32 # The number of samples per gradient update fro training
)

#Evaluate the model
model.evaluate(
    test_images,
    to_categorical(test_labels)
)

model.save_weights('model.h5')

#predict on the first 5 test images
predictions = model.predict(test_images[:5])
#print(predictions)
#print our models prediction
print(np.argmax(predictions, axis = 1))
print(test_labels[:5])

for i in range(0,10):
  first_image = test_images[4]
  first_image = np.array(first_image, dtype ='float')
  pixels = first_image.reshape((28,28))
  plt.imshow(pixels)
  plt.show()