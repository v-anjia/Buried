import threading
import time
import os
import sys
import multiprocessing
def thread1():
    print("run function name is :%s" %(sys._getframe().f_code.co_name))
    time.sleep(10)
    print("run function name is :%s" % (sys._getframe().f_code.co_name))

def thread2():
    print("run function name is :%s" %(sys._getframe().f_code.co_name))
    time.sleep(1)
    for i in range(5):
        time.sleep(1)
        print("hello world")




th1 = threading.Thread(target=thread1,name="thread_antony")
th1.start()
thread2()
th1.join()



# # This Python 3 environment comes with many helpful analytics libraries installed
# # It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# # For example, here's several helpful packages to load in
# '''
# Test Project
# author :antony weijiang
# data:2020/4/21
# '''
# import numpy as np  # linear algebra
# import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
# import tensorflow as tf
# import pandas as pd
# # from keras.models import Sequential
# # from keras.layers import Dense,Flatten,Conv2D,MaxPooling2D,Dropout
# from keras.utils import np_utils
# from keras import backend as K
# from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
#
# # K.set_image_dim_ordering('th')
# import matplotlib.pyplot as plt
#
#
# # Input data files are available in the "../input/" directory.
# # For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory
#
# import os
#
# # for dirname, _, filenames in os.walk('/kaggle/input'):
# #     for filename in filenames:
# #         print(os.path.join(dirname, filename))
# # Any results you write to the current directory are saved as output.
#
# tf.test.is_gpu_available()
# print(tf.__version__)
#
# '''
# Load data set
# '''
# (x_train_image, y_train_lable), (x_test_image, y_test_lable) = tf.keras.datasets.fashion_mnist.load_data()
# print("antony@@@debug")
# # print(x_train_image.shape)
# # print(x_train_image)
# # print(y_train_lable)
# print("max value is: %s" % (np.max(x_train_image[0])))
#
# # plt.imshow()
#
# '''
# Numerical normalization
# '''
#
# x_train_image = x_train_image.astype('float32')
# x_test_image = x_test_image.astype('float32')
# x_train_image = x_train_image / 255
# x_test_image = x_test_image / 255
# x_train_image = np.expand_dims(x_train_image, -1)
# x_test_image = np.expand_dims(x_test_image, -1)
#
# print("normalization value is :%s" % (np.max(x_train_image[0])))
# # print(x_train_image.shape)
# '''
# modelling
# '''
#
#
# # def test():
# #     model = tf.keras.Sequential()
# #     model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# #     model.add(tf.keras.layers.Dense(128, activation='relu'))
# #     model.add(tf.keras.layers.Dense(10, activation='softmax'))
#
# #     model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['acc'])
#
# #     model.fit(x_train_image,y_train_lable,epochs=5)
#
# #     model.evaluate(x_test_image,y_test_lable)
#
#
# def train():
#     model = tf.keras.Sequential()
#     model.add(
#         tf.keras.layers.Conv2D(64, (3, 3), input_shape=x_train_image.shape[1:], activation='relu', padding='same'))
#     #     model.add(tf.keras.layers.Conv2D(64,(3,3), input_shape=x_train_image.shape[1:], activation='relu'))
#     print(model.output_shape)
#     model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'))
#     model.add(tf.keras.layers.MaxPool2D())
#     model.add(tf.keras.layers.Dropout(0.5))
#
#     model.add(tf.keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same'))
#     model.add(tf.keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same'))
#     model.add(tf.keras.layers.MaxPool2D())
#     model.add(tf.keras.layers.Dropout(0.5))
#
#     model.add(tf.keras.layers.Conv2D(512, (3, 3), activation='relu', padding='same'))
#     model.add(tf.keras.layers.Conv2D(512, (3, 3), activation='relu', padding='same'))
#     model.add(tf.keras.layers.MaxPool2D())
#     model.add(tf.keras.layers.Dropout(0.5))
#     model.add(tf.keras.layers.GlobalAveragePooling2D())
#     model.add(tf.keras.layers.Dense(256, activation='relu'))
#     model.add(tf.keras.layers.Dense(10, activation='softmax'))
#     model.summary()
#
#     model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])
#     #     model.fit(x_train_image,y_train_lable,epochs=30,validation_data=(x_test_image,y_test_lable))
#     history = model.fit(x_train_image, y_train_lable, epochs=5, validation_data=(x_test_image, y_test_lable))
#
#     print("over all")
#     print(history.history.keys())
#
#     plt.plot(history.epoch, history.history.get('acc'), label='acc')
#     plt.plot(history.epoch, history.history.get('val_acc'), label='val_acc')
#
#     plt.plot(history.epoch, history.history.get('loss'), label='loss')
#     plt.plot(history.epoch, history.history.get('val_loss'), label='val_loss')
#
#
# if __name__ == '__main__':
#     train()
