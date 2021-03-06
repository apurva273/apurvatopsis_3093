# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 01:10:07 2020

@author: BEST BUY
"""
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
d={'Mobile':['M1','M2','M3','M4','M5'],'Price':[250,200,300,275,225],'Storage Space':[16,16,32,32,16],'Camera':[12,8,16,8,16],'Looks':[5,3,4,4,2]}
df = pd.DataFrame(data=d)

def topsis(d,w,t):
  fd = d.copy()
  n = len(d.axes[0])
  m = len(d.axes[1])
  d = d.astype(dtype='float')
  d = d.values
  for j in range(m):
    s=0
    for i in range(n):
      s+=d[i][j]*d[i][j]
    s = s**0.5
    for i in range(n):
      d[i][j]=float(d[i][j])/float(s)
  for j in range(m):
    for i in range(n):
      d[i][j]=d[i][j]*w[j]
  v1=[]
  v2=[]  
  for j in range(m):
    if t[j]=='+':
      v1.append(max(d[:,j]))
      v2.append(min(d[:,j]))
    else:
      v1.append(min(d[:,j]))
      v2.append(max(d[:,j]))    
  p1=[]
  p2=[]
  for i in range(n):
    s1=0
    s2=0
    for j in range(m):
      s1+=(d[i][j]-v1[j])*(d[i][j]-v1[j])
      s2+=(d[i][j]-v2[j])*(d[i][j]-v2[j])
    s1 = s1**0.5
    s2 = s2**0.5
    p1.append(s1)
    p2.append(s2)  
  r = []
  for i in range(n):
    k = p2[i]/(p1[i]+p2[i])
    r.append(k)  
  fd['Performance'] = r
  fd['Rank'] = fd['Performance'].rank(ascending=False)
  print(fd)
del df['Mobile']
w = [0.25,0.25,0.25,0.25]
i = ['-','+','+','+']
topsis(df,w,i)   