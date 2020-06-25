# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:49:37 2020

@author: Ethan
"""

import numpy as np
from PIL import Image

a = np.zeros(640)
a[320] = 1
rule = [0,1,0,0,1,0,0,1]
#rule222
def next_gen(p,rule):
    result = np.zeros(640)
    for i in range(0,len(result)):
#        if(i==0):
#            if(p[i]==1 and p[i+1]==1):
#                result[i]=rule[4]
#            if(p[i]==1 and p[i+1]==0):
#                result[i] = rule[5]
#            if(p[i]==0 and p[i+1]==1):
#                result[i] = rule[6]
#            if(p[i]==0 and p[i+1]==0):
#                result[i] = rule[7]
        if(i==639):
            if(p[i-1] ==1 and p[i]==1 and p[0]==1):
                result[i]=rule[0]
            if(p[i-1] ==1 and p[i]==1 and p[0]==0):
                result[i] = rule[1]
            if(p[i-1] ==1 and p[i]==0 and p[0]==1):
                result[i] = rule[2]
            if(p[i-1] ==1 and p[i]==0 and p[0]==0):
                result[i] = rule[3]
            if(p[i-1] ==0 and p[i]==1 and p[0]==1):
                result[i]=rule[4]
            if(p[i-1] ==0 and p[i]==1 and p[0]==0):
                result[i] = rule[5]
            if(p[i-1] ==0 and p[i]==0 and p[0]==1):
                result[i] = rule[6]
            if(p[i-1] ==0 and p[i]==0 and p[0]==0):
                result[i] = rule[7]
        else:
            if(p[i-1] ==1 and p[i]==1 and p[i+1]==1):
                result[i]=rule[0]
            if(p[i-1] ==1 and p[i]==1 and p[i+1]==0):
                result[i] = rule[1]
            if(p[i-1] ==1 and p[i]==0 and p[i+1]==1):
                result[i] = rule[2]
            if(p[i-1] ==1 and p[i]==0 and p[i+1]==0):
                result[i] = rule[3]
            if(p[i-1] ==0 and p[i]==1 and p[i+1]==1):
                result[i]=rule[4]
            if(p[i-1] ==0 and p[i]==1 and p[i+1]==0):
                result[i] = rule[5]
            if(p[i-1] ==0 and p[i]==0 and p[i+1]==1):
                result[i] = rule[6]
            if(p[i-1] ==0 and p[i]==0 and p[i+1]==0):
                result[i] = rule[7]
    
        
        
        
    return result
        


image = np.empty((0,1))
image = np.append(image,a)

for j in range(0,1000):
    a = next_gen(a,rule)
    #print(a)
    image = np.append(image,a)
image = image.reshape(j+2,640)
image[image>0] = 255
im  = Image.fromarray(image)
im.show()
    