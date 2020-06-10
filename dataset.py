# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:52:50 2020

@author: Mine Kaya
"""

import matplotlib.pyplot as plt
import numpy as np
import os
from keras.datasets import cifar100

(x_train,y_train),(x_test, y_test)=cifar100.load_data()

os.mkdir('dataset')
os.mkdir('dataset\\train')
os.mkdir('dataset\\test')

for i in range(100):
    if i==22 or i==23 or i==48 or i==65 or i==90 or i==97 :
        path=os.path.join('dataset\\train',str(i))
        os.mkdir(path)
        path=os.path.join('dataset\\test',str(i))
        os.mkdir(path)

import matplotlib.pyplot as plt
for i in range(500):
    if int(y_train[i])==22:
        path='dataset/train/22/'+str(i)+'.png'
        plt.imsave(path,x_train[i])
    if int(y_train[i])==23:
        path='dataset/train/23/'+str(i)+'.png'
        plt.imsave(path,x_train[i])
    if int(y_train[i])==48:
        path='dataset/train/48/'+str(i)+'.png'
        plt.imsave(path,x_train[i])
    if int(y_train[i])==65:
        path='dataset/train/65/'+str(i)+'.png'
        plt.imsave(path,x_train[i])
    if int(y_train[i])==90:
        path='dataset/train/90/'+str(i)+'.png'
        plt.imsave(path,x_train[i])
    if int(y_train[i])==97:
        path='dataset/train/97/'+str(i)+'.png'
        plt.imsave(path,x_train[i])    



for i in range(100):
    if int(y_test[i])==22:
        path='dataset/test/22/'+str(i)+'.png'
        plt.imsave(path,x_test[i])
    if int(y_test[i])==23:
        path='dataset/test/23/'+str(i)+'.png'
        plt.imsave(path,x_test[i])
    if int(y_test[i])==48:
        path='dataset/test/48/'+str(i)+'.png'
        plt.imsave(path,x_test[i])
    if int(y_test[i])==65:
        path='dataset/test/65/'+str(i)+'.png'
        plt.imsave(path,x_test[i])
    if int(y_test[i])==90:
        path='dataset/test/90/'+str(i)+'.png'
        plt.imsave(path,x_test[i])
    if int(y_test[i])==97:
        path='dataset/test/97/'+str(i)+'.png'
        plt.imsave(path,x_test[i])
    

