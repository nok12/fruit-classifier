import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPool2D
from keras.optimizers import Adam
from keras.utils import np_utils

X = np.load("/content/drive/My Drive/X_data.npy")
y = np.load("/content/drive/My Drive/Y_data.npy")

