//
//  main.cpp
//  Color classification
//
//  Created by Hsu yun hung on 2021/1/4.
//  Copyright © 2021 Hsu yun hung. All rights reserved.
//


#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <iostream>
#include <string>
#include <cstdlib>
#include <cmath>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include<sys/types.h>
#include <vector>
#include "Header.h"
using namespace std;
std::string findcode(string color, string classa[11]);
std::string findcolor(int wordlen[500],int indexsize,std::string color[500],std::string ctrain, std::string classifedcolor[500]);
vector<string> distinct(vector<string> classes);

int main(int argc, const char * argv[]) {
    ifstream ColorIndex;
    ifstream trainset;
    ofstream outData;
    ColorIndex.open("/Users/hsuyunhuung/Documents/機器學習/color problem/colors(1).csv");
    trainset.open("/Users/hsuyunhuung/Documents/機器學習/all clean data/clean0.csv");
    //trainset.open("/Users/hsuyunhuung/Documents/機器學習/color problem/test.csv");
    outData.open("/Users/hsuyunhuung/Documents/機器學習/traindata/train.txt");
    string colorname[500];
    string hue[500];
    string color[500];
    string classa[11];
    int wordlen[500];
    string non;
    string Category;
    string primary_image_url;
    string all_image_url;
    string attribute;
    string Brand;
    string index;//this one is for extra index, meaningless
    string colors;
    string shoesize;
    string style;
    string material;
    string country;
    string width;
    string scolor;
    string code;
    int n1=0;//this one will represent the size of colorindex
    int n=0;

    
    //while (!Class.eof()) {
     //       getline ( Class, classa[c] );
      //      c+=1;
    
    //}
    while (!ColorIndex.eof()) {

        if (n==0) {
            n+=1;
            continue;
        }else{
            getline ( ColorIndex, colorname[n-1], ',' );
            wordlen[n-1]=colorname[n-1].length();
            getline ( ColorIndex,hue[n-1], ',' );
            getline ( ColorIndex,color[n-1]);
        
            
            n+=1;
        }
    }


    

    //cout<<"-----"<<endl;
    //cout<<color[1]<<endl;
    //cout<<color[2]<<endl;
    //string temp=color[1];
    //cout<<classa[8]<<endl;
    //cout<<(classa[8]==color[2])<<endl;


    n1=n-1;
    n=0;
    outData<<"Category"<<',';
    outData<<"primary_image_url"<<',';
    outData<<"all_image_url"<<',';
    outData<<"attribute"<<',';
    outData<<"Brand"<<',';
    outData<<"colors"<<',';
    outData<<"black"<<',';
    outData<<"blue"<<',';
    outData<<"gray"<<',';
    outData<<"green"<<',';
    outData<<"brown"<<',';
    outData<<"pink"<<',';
    outData<<"purple"<<',';
    outData<<"red"<<',';
    outData<<"white"<<',';
    outData<<"yellow"<<endl;
    
    while (!trainset.eof()) {
        if (n==0) {
            getline ( trainset, non, ',' );
            getline ( trainset, Category, ',' );
            getline ( trainset,primary_image_url, ',' );
            getline ( trainset,all_image_url, ',' );
            getline ( trainset,attribute, ',' );
            getline ( trainset,index,','); //index will not output
            getline ( trainset,Brand,',');
            getline ( trainset,colors,',');
            getline ( trainset,shoesize,',');
            getline ( trainset,style,',');
            getline ( trainset,material,',');
            getline ( trainset,country,',');
            getline ( trainset,width,',');
            n+=1;
        }else if(n==1){
     
            getline ( trainset, Category, ',' );
            getline ( trainset,primary_image_url, ',' );
            getline ( trainset,all_image_url, ',' );
            getline ( trainset,attribute,'"' );
            getline ( trainset,attribute,'"' );
            getline ( trainset,index,',');
            getline ( trainset,index,',');//index will not output
            getline ( trainset,Brand,',');
            getline ( trainset,colors,',');
            getline ( trainset,shoesize,',');
            getline ( trainset,style,',');
            getline ( trainset,material,',');
            getline ( trainset,country,',');
            getline ( trainset,width,',');
            
            scolor=findcolor(wordlen, n1, colorname, colors,color);
            scolor = scolor.substr(1, scolor.size() - 3);
            
            outData<<Category<<',';
            outData<<primary_image_url<<',';
            outData<<all_image_url<<',';
            outData<<'"';
            outData<<attribute<<'"';
            outData<<',';
            outData<<Brand<<',';
            outData<<scolor<<endl;
            n+=1;
            cout<<scolor<<endl;
            
        }else{
            getline ( trainset, Category, ',' );
            getline ( trainset,primary_image_url, ',' );
            getline ( trainset,all_image_url, ',' );
            getline ( trainset,attribute,'"' );
            getline ( trainset,attribute,'"' );
            getline ( trainset,index,',');
            getline ( trainset,index,',');//index will not output
            getline ( trainset,Brand,',');
            getline ( trainset,colors,',');
            getline ( trainset,shoesize,',');
            getline ( trainset,style,',');
            getline ( trainset,material,',');
            getline ( trainset,country,',');
            getline ( trainset,width,',');
            scolor=findcolor(wordlen, n1, colorname, colors,color);
            scolor = scolor.substr(1, scolor.size() - 3);
            
        
            //cout<<colors<<endl;
            outData<<Category<<',';
            outData<<primary_image_url<<',';
            outData<<all_image_url<<',';
            outData<<'"';
            outData<<attribute<<'"';
            outData<<',';
            outData<<Brand<<',';
            outData<<scolor<<endl;
            n+=1;
        }
    }
    
    
    
    
    trainset.close();
    ColorIndex.close();
    
}

std::string findcolor(int wordlen[500],int indexsize,std::string color[500],std::string ctrain,std::string classifedcolor[500]){
    //use binary search to find the color code
    if(ctrain.compare("N\A")==0){
        return "NA";
    }
    
    int clen=ctrain.length();
    int stop=0;
    int hi=indexsize-1;
    int mid=indexsize/2;
    int lo=0;
    while(mid<=hi and lo<=mid){
        if(clen>wordlen[mid]){
            lo=mid+1;
            mid=(hi-lo)/2+lo;
        }else if(clen<wordlen[mid]){
            hi=mid-1;
            mid=(hi-lo)/2+lo;
        }else{
            stop=1;
            break;
        }
    }
    int u=0;
    int d=0;
    bool found=false;
    bool up=false;
    bool down=false;
    while(wordlen[mid+u]==clen and found==false){
        if(color[mid+u].compare(ctrain)==0){
            found=true;
            up=true;
        }else{
            u+=1;
        }
    }
 
    while(wordlen[mid-d]==clen and found==false){
          if(color[mid-d].compare(ctrain)==0){
              found=true;
              down=true;
          }else{
              d+=1;
          }
      
      }

    
    if(found==true){
        if(up==true){
           return classifedcolor[mid+u];
        }else if(down==true){
            return classifedcolor[mid-d];
        }else{
            return "NA";
        }
    }else{
        return "NA";
    }
    
}



