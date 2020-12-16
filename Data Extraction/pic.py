import requests
import pandas as pd
import re


def entrydata(data,column,i):    #column is the colname datatype:string;
    
    a=re.search(column,data["attribute"][i])
    if(a==None):
        data[column][i]="N\A"
    else:
        loc=a.span()
        temp=data["attribute"][i][loc[1]+1:]
        a=re.search(',',temp)
        if(a==None):
            data[column][i]=temp
        else:
            loc=a.span()
            data[column][i]=temp[0:loc[0]]


def main():
    data=pd.read_csv(r'/Users/hsuyunhuung/Documents/機器學習/competition/mlchallenge_set_2021.tsv',encoding = "ISO-8859-1", sep='\t',header=None)
    data.columns=["Category","primary_image_url","all_image_url","attribute","index"]
    
    n=2000 #enter the number of data that want to extract
    #add empty column
    data["Brand"]=""
    Nike="/Users/hsuyunhuung/Documents/機器學習/brand/nike/Nike"
    adidas="/Users/hsuyunhuung/Documents/機器學習/brand/Adidas/Adidas"
    Vans="/Users/hsuyunhuung/Documents/機器學習/brand/VANS/VANS"
    Shimano="/Users/hsuyunhuung/Documents/機器學習/brand/Shimano/Shimano"
    FILA="/Users/hsuyunhuung/Documents/機器學習/brand/FILA/FILA"
    NB="/Users/hsuyunhuung/Documents/機器學習/brand/NB/NB"
    Converse="/Users/hsuyunhuung/Documents/機器學習/brand/Converse/Converse"
    Kith="/Users/hsuyunhuung/Documents/機器學習/brand/Kith/Kith"
    undefin="/Users/hsuyunhuung/Documents/機器學習/brand/undefin/undefin"
    Jordan="/Users/hsuyunhuung/Documents/機器學習/brand/Jordan/Jordan"
    ASICS="/Users/hsuyunhuung/Documents/機器學習/brand/ASICS/ASICS"
    Reebok="/Users/hsuyunhuung/Documents/機器學習/brand/Reebok/Reebok"
    Chrome="/Users/hsuyunhuung/Documents/機器學習/brand/Chrome/Chrome"
    for i in range(0,n):
        data["attribute"][i] =data["attribute"][i][1:]
        data["attribute"][i] =data["attribute"][i][0:len( data["attribute"][i])-1]
        entrydata(data,"Brand",i)
        if("nike" in data["Brand"][i].lower()):
            r = requests.get(data["primary_image_url"][i], allow_redirects=True)
            path=Nike+str(i)+".JPG"
            open(path,'wb').write(r.content)
        elif("shimano" in data["Brand"][i].lower() ):
            r = requests.get(data["primary_image_url"][i], allow_redirects=True)
            path=Shimano+str(i)+".JPG"
            open(path,'wb').write(r.content)
        elif("adidas" in data["Brand"][i].lower() ):
            r = requests.get(data["primary_image_url"][i], allow_redirects=True)
            path=adidas+str(i)+".JPG"
            open(path,'wb').write(r.content)
        elif("vans" in data["Brand"][i].lower()):
            r = requests.get(data["primary_image_url"][i], allow_redirects=True)
            path=Vans+str(i)+".JPG"
            open(path,'wb').write(r.content)
        elif("fila" in data["Brand"][i].lower()):
            r = requests.get(data["primary_image_url"][i], allow_redirects=True)
            path=FILA+str(i)+".JPG"
            open(path,'wb').write(r.content)
        elif("new balance" in data["Brand"][i].lower()):
            r = requests.get(data["primary_image_url"][i], allow_redirects=True)
            path=NB+str(i)+".JPG"
            open(path,'wb').write(r.content)
        elif("converse" in data["Brand"][i].lower()):
            r = requests.get(data["primary_image_url"][i], allow_redirects=True)
            path=Converse+str(i)+".JPG"
            open(path,'wb').write(r.content)
        elif("kith" in data["Brand"][i].lower()):
            r = requests.get(data["primary_image_url"][i], allow_redirects=True)
            path=Kith+str(i)+".JPG"
            open(path,'wb').write(r.content)
        elif("jordan" in data["Brand"][i].lower()):
            r = requests.get(data["primary_image_url"][i], allow_redirects=True)
            path=Jordan+str(i)+".JPG"
            open(path,'wb').write(r.content)
        elif("asics" in data["Brand"][i].lower()):
            r = requests.get(data["primary_image_url"][i], allow_redirects=True)
            path=ASICS+str(i)+".JPG"
            open(path,'wb').write(r.content)
        elif("asics" in data["Brand"][i].lower()):
            r = requests.get(data["primary_image_url"][i], allow_redirects=True)
            path=ASICS+str(i)+".JPG"
            open(path,'wb').write(r.content)
        elif("reebok" in data["Brand"][i].lower()):
            r = requests.get(data["primary_image_url"][i], allow_redirects=True)
            path=Reebok+str(i)+".JPG"
            open(path,'wb').write(r.content)
        elif("chrome" in data["Brand"][i].lower()):
            r = requests.get(data["primary_image_url"][i], allow_redirects=True)
            path=Chrome+str(i)+".JPG"
            open(path,'wb').write(r.content)
        else:
            r = requests.get(data["primary_image_url"][i], allow_redirects=True)
            path=undefin+str(i)+".JPG"
            open(path,'wb').write(r.content)
if __name__ == '__main__':
    main()
    

