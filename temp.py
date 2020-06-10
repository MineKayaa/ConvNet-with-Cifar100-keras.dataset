# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:23:42 2020

@author: Mine Kaya
"""


import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, Activation
import matplotlib.pyplot as plt
from keras import optimizers




model = Sequential()
model.add(Conv2D(32,
                 (3, 3),
                 padding='same',
                 input_shape=(32,32,3)))
model.add(Activation('relu'))


model.add(Conv2D(32, 
                 (3, 3),
                 padding= 'same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, 
                 (3, 3), 
                 padding= 'same'))
model.add(Activation('relu'))

model.add(Conv2D(64, 
                 (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))

model.add(Dense(6))
model.add(Activation('softmax'))
model.summary()


# modeli derle

model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])

#data augmentation 

train_datagen= ImageDataGenerator(
        rescale=1./255,
        rotation_range=30,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
      #  horizantal_flip=True,
        vertical_flip=True,
        fill_mode='nearest')

train_dir='C:\\Users\\Name\\Desktop\\derin\\ödev\\dataset\\train'

train_genarator =train_datagen.flow_from_directory(
        train_dir,
        target_size=(32,32),
        batch_size=20,
        class_mode='categorical')

test_datagen= ImageDataGenerator(rescale=1./255)
test_dir='C:\\Users\\Name\\Desktop\\derin\\ödev\\dataset\\test'
validation_genarator =test_datagen.flow_from_directory(
        test_dir,
        target_size=(32,32),
        batch_size=20,
        class_mode='categorical')

history= model.fit_generator(
        train_genarator,
        steps_per_epoch=100,
        epochs=20,
        validation_data= validation_genarator,
        validation_steps=100)



acc=history.history['acc']
val_acc=history.history['val_acc']
loss =history.history['loss']
val_loss=history.history['val_loss']

epochs=range(len(acc))

plt.plot(epochs, acc, 'bo', label='Trainnig acc')
plt.plot(epochs, val_acc, 'r', label='Validation acc')
plt.title('Trainning and Validation acc')
plt.legend()