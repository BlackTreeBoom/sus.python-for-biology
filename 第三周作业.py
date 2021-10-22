#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np#计算A,B两点欧几里得距离
a = np.array((1, 10, -5))
b = np.array((5, -7, 6))
dist = np.linalg.norm(a-b)
print(dist)


# In[9]:


import numpy as np#计算A,C两点欧几里得距离
a = np.array((1, 10, -5))
c = np.array((-3, 2, 5))
dist = np.linalg.norm(a-c)
print(dist)


# In[10]:


import numpy as np#计算B,C两点欧几里得距离
b = np.array((5, -7, 6))
c = np.array((-3, 2, 5))
dist = np.linalg.norm(b-c)
print(dist)


# In[11]:


def manhattanDistance(x,y):#定义曼哈顿距离函数
    return sum(map(lambda i, j: abs(i-j),x,y))


# In[13]:


print(manhattanDistance(a,b))#A,B曼哈顿距离


# In[14]:


print(manhattanDistance(a,c))#A,C曼哈顿距离


# In[15]:


print(manhattanDistance(b,c))#B,C曼哈顿距离


# In[1]:


genes = ['BORCS8','MEX3C','PKD1','RPL9P7','PFDN5','HMGCR','RRP7A',
         'DIO2','ISG15','IFNAR1','IRF9','MX1','CTSE','IFITM2']
l2fc = [-4.0737246460000005,
-4.336649973,
 4.679153667,
 -6.598944265,
 -5.416135367000001,
 -4.619810193,
 -5.0381476130000005,
 3.871477169,
 -4.1870398280000005,
 -5.203271895,
 -0.409021619,
 -2.375481128,
 0.5079779170000001,
 -0.87356034]

p_values = [4.08e-11,
 4.9299999999999994e-11,
 6e-11,
 0.043676405999999994,
 0.227105224,
 0.0025278270000000003,
 0.002532635,
 0.002581624,
 0.002581624,
 0.04367192,
 6.509999999999999e-11,
 7.109999999999999e-11,
 0.22728711100000001,
 0.227404988]
#导入文档内所有信息并组合


# In[2]:


RNAseqlist=list(zip(genes ,l2fc,p_values))


# In[3]:


RNAseqlist


# In[4]:


DNAseq = {}#定义包含干扰素通路基因的字典
for i in range(0, len(genes)):
    DNAseq[genes[i]]=[l2fc[i], p_values[i]]
print(DNAseq)


# In[7]:


import math#通过字典，先查询key，判断是否在其中，再判断显著水平与log2的值
def DNAcheck(DNAname):
    if DNAname in DNAseq:   
        DNAname1=DNAseq[DNAname][0]
        DNAname2=DNAseq[DNAname][1]  
        print("该基因存在于列表中")
        if DNAname1 < 0.01:
            print("该基因在列表中但是没有显著表达水平变化")
            if  abs(DNAname2) > 1:#abs表示返回绝对值
                print("该基因在列表中，显著表达，但是log2绝对值小于等于1")
            else:
                print("该基因在列表中，显著表达，且log2绝对值大于1")
        else:
            print("该基因有显著变化")
    else:
        print("该基因不在列表中")


# In[8]:


DNAname=input("请输入干扰素通路基因名称：")
DNAcheck(DNAname)
# 60


# In[ ]:




