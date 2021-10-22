#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


listDEG=os.listdir('d:\DEG')#用os函数打开DEG文件，读取每个头文件名并存入列表中
listDEG


# In[9]:


#有冒号就要空一格，一般啥都不用操作
listwork6=[]
for i in range(0,len(listDEG)):#利用for循环遍历每一个元素，因为在最外层，可以直接用
    listwork=[]#每一次循环都初始化了
    handle=listDEG[i].split('.')#要提取gene_perturbed, cell_type加入文件中
    handlename=handle[0].split('_')
    with open ('d:\DEG\\'+ listDEG[i]) as f:#通过withopen函数打开文件，（）利用for遍历每一个要打开的excel文件
        #打开文件用完后才能处理
        f.readline()#默认读取第一行，鼠标停留在读取后的位置
        listwork=f.readlines()#这样就可以跳过第一行直接往下读了，避免了头文件的干扰 
        listwork2=[]#去掉换行符
        for i in range(0,len(listwork)):
            listwork2.append(listwork[i].replace('\n','')) #去掉\n符号
        for i in range(0,len(listwork2)):#遍历读取该列表中的每个字符并将它们转为小列表
            listwork3=listwork2[i].split(',')#读取到的是str字符，用split函数即可分割为一个个的列表，也就是我想要的小列表
            
            listwork3.append(handlename[0]) #将需要的元素添加进来
            listwork3.append(handlename[3])#gene_perturbed, cell_type加入文件中
            
            if float(listwork3[6]) < 0.05 :#判断是否小于0.05,如果小于就存入listwork4
                listwork5=[]
                for i in [1,2,3,6,8,7]:
                    listwork5.append(listwork3[i]) #将需要的元素添加进来
                listwork6.append(listwork5)


# In[11]:


listwork6


# In[16]:


file_name='myhomework.csv'
with open (file_name,'w') as f:#这样的方法最好，不用考虑关闭的问题，老师课堂上教的
    f.write("ID, Symbol, logFC, FDR, gene_perturbed, cell_type\n")#写入标题，默认在第一行
    for x in listwork6:
        f.write('%s,%s,%s,%s,%s,%s\n'%(x[0],x[1],x[2],x[3],x[4],x[5]))#通过课堂作业方法写入二重列表中的list元素


# In[34]:




