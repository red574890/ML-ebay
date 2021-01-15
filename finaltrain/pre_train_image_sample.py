import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers 
from tensorflow.keras import Model 
import matplotlib.pyplot as plt
import cv2
import numpy as np 

base_dir = "/Users/hsuyunhuung/Documents/機器學習/product visual/test/train/2"


def loadImages(path):
    # Put files into lists and return them as one list of size 4
    image_files = sorted([os.path.join(path, file)
         for file in os.listdir(path) if      file.endswith('.JPG')])
 
    return image_files



allimage=loadImages(base_dir)
histogram=[]
for i in allimage:
    image = cv2.imread(i)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray_image], [0],  
                         None, [256], [0, 256])
    histogram.append(hist)

   

   
   
c1, c2 = 0, 0
   
# Euclidean Distace between data1 and test 
i = 0
while i<len(histogram[0]) and i<len(histogram[1]): 
    c1+=(histogram[0][i]-histogram[1][i])**2
    i+= 1
c1 = c1**(1 / 2) 
   
  
# Euclidean Distace between data2 and test 
i = 0
while i<len(histogram[0]) and i<len(histogram[2]): 
    c2+=(histogram[0][i]-histogram[2][i])**2
    i+= 1
c2 = c2**(1 / 2) 
   
if(c1<c2): 
    print("1 is more similar to 2") 
else: 
    print("1 is more similar to 3") 
