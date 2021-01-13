import pandas as pd
import re


data=pd.read_csv(r'/Users/hsuyunhuung/Documents/機器學習/competition/mlchallenge_set_2021.tsv',encoding = "ISO-8859-1", sep='\t',header=None )

data.columns=["Category","primary_image_url","all_image_url","attribute","index"]

temp5=data["Category"]==5
temp4=data["Category"]==4
temp3=data["Category"]==3
temp2=data["Category"]==2
temp1=data["Category"]==1
fifth=data[temp5]
forth=data[temp4]
third=data[temp3]
second=data[temp2]
first=data[temp1]


fifthr=fifth.sample(n=1000)
forthr=forth.sample(n=1000)
thirdr=third.sample(n=1000)
secondr=second.sample(n=1000)
firstr=first.sample(n=1000)


fifthr.to_csv(r'/Users/hsuyunhuung/Documents/機器學習/productrandom/5.csv',index=False)
forthr.to_csv(r'/Users/hsuyunhuung/Documents/機器學習/productrandom/4.csv',index=False)
thirdr.to_csv(r'/Users/hsuyunhuung/Documents/機器學習/productrandom/3.csv',index=False)
secondr.to_csv(r'/Users/hsuyunhuung/Documents/機器學習/productrandom/2.csv',index=False)
firstr.to_csv(r'/Users/hsuyunhuung/Documents/機器學習/productrandom/1.csv',index=False)
