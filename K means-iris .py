#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import collections
data=pd.read_csv('iris.data',header=None)
x,y=data.shape
r,c=x,y
lis=data.iloc[:,4].unique()
dict={}
count=0
for i in lis:
    dict[i]=count
    count+=1
for i in range(0,x):
    data.iloc[i,4]=dict[data.iloc[i,4]]
list=[i for i in range(5,31)]
acc=[]
for cl in list:
    k=[]
    for i in range(0,100):
        c=np.random.randint(0,149)
        if c not in k:
            k.append(c)
        if len(k)==cl:
            break
    data1=data.to_numpy()
    means_prev=[]
    for i in k:
        means_prev.append(data1[i,:5])
    print(means_prev)
    l1=np.ones((150,1))
    for i in k:
        l=np.sqrt(np.sum((data1[i]-data1)**2,axis=1))
        l1=np.hstack((l1,l.reshape(-1,1)))
    l=np.argmin(l1[:,1:],axis=1)
    data1=np.hstack((data1,l.reshape(-1,1)))
    count=200
    while(count):
        new_means=[]
        for i in range(0,cl):
            x=data1[data1[:,5]==i]
            x=x[:,:5]
            x1,y1=x.shape
            new_means.append(1/x1*(np.sum(x,axis=0)))
        m=0
        for i,j in zip(new_means,means_prev):
            t=0
            for a,b in zip(i,j):
                if a==b:
                    t+=1
            if t==5:
                m+=1
        if m==cl:
            break
        else:
            means_prev=new_means
        l1=np.ones((150,1))
        for i in new_means:
            l=np.sqrt(np.sum((i-data1[:,:5])**2,axis=1))
            l1=np.hstack((l1,l.reshape(-1,1)))
        l=np.argmin(l1[:,1:],axis=1)
        data1=np.hstack((data1[:,:5],l.reshape(-1,1)))
        count-=1
    comp=np.hstack((l.reshape(-1,1),data1[:,4].reshape(-1,1)))
    gr=[0,1,2]
    acc=[]
    for i in range(0,cl):
        x=comp[comp[:,0]==i]
        t=[]
        for j in gr:
            t.append(len(x[x[:,1]==j]))
        acc.append(t)
    acc
    count=0
    for i in acc:
        i.sort()
        count=count+i[1]+i[2]
    acc.append(((r-count)/r)*100)

    # In[ ]:




