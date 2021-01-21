import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from tensorflow.keras import layers 
from tensorflow.keras import Model 
import matplotlib.pyplot as plt
import cv2
import numpy as np 
import pandas as pd
from urllib.request import urlopen
import urllib
from annoy import AnnoyIndex
import re

#row data
data = pd.read_csv("/Users/hsuyunhuung/Documents/ML competition/mlchallenge_set_2021.tsv",encoding = "ISO-8859-1", sep='\t',header=None)
data.columns=["Category","primary_image_url","all_image_url","attribute","index"]
data1=data[data["Category"]==1]
data2=data[data["Category"]==2]
data3=data[data["Category"]==3]
data4=data[data["Category"]==4]
data5=data[data["Category"]==5]
url1=data1["primary_image_url"]
url2=data2["primary_image_url"]
url3=data3["primary_image_url"]
url4=data4["primary_image_url"]
url5=data5["primary_image_url"]


#url test 3000, pls test irl2
url1=data1["primary_image_url"]
url2=data2["primary_image_url"]
url3=data3["primary_image_url"]
#url4=data4["primary_image_url"]
#url5=data5["primary_image_url"]




# pic to vector
def histogram(data):
    f=256
    histogram=AnnoyIndex(f, 'angular')
    index=[]
    a=0
    
    for i in data:
        try:
            req = urlopen(i)
            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            img = cv2.imdecode(arr, 1) # 'Load it as it is'
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            hist = cv2.calcHist([gray_image], [0],None, [256], [0, 256])
            histogram.add_item(a,hist)
            index.append(a)
        except urllib.error.HTTPError:
            print("cannot find"+str(a))
        except cv2.error:
            print("cannot find"+str(a))
        a+=1  
    return histogram,index





#pic to vector
hist1, d1index= histogram(url1)
print("firstoneover")
hist2, d2index= histogram(url2)
print("secondoneover")
hist3, d3index= histogram(url3)
print("overoneover")

f=256
# can adjust tree
#data1
hist1.build(10)
hist1.save('data1.ann')
indexdict1={"index":d1index}
df1=pd.DataFrame(indexdict1)
df1.to_csv('data1index.csv',index=None)


#data2
hist2.build(10)
hist2.save('data2.ann')
indexdict2={"index":d2index}
df2=pd.DataFrame(indexdict2)
df2.to_csv('data2index.csv',index=None)

#data3
hist3.build(10)
hist3.save('data3.ann')
indexdict3={"index":d3index}
df3=pd.DataFrame(indexdict3)
df3.to_csv('data3index.csv',index=None)

    
