#!/usr/bin/env python
# coding: utf-8

# In[31]:


file_handle=open('d:\codon_table.csv','r')
#file_handle.readlines()因为已经读过文件了，光标在文件末尾，再读无内容


# In[32]:


listdna=file_handle.readlines()#读取的返回值就是列表


# In[33]:


alist=[]#创建空列表
for x in listdna:#遍历列表中的每一个元素
    alist.append(x.split(','))#对每一个元素进行分割，分割后存入空列表


# In[34]:


alist[1][0]#提取列表第N个元素的第N个值


# In[35]:


dnakey=[]#将二重列表中元素列表的单个值分别提取出来，建立新的列表
for i in range(0,len(alist)):
        dnakey.append(alist[i][0]) #列表中第i个元素的第i个内容，这里是密码子


# In[36]:


dnavalue1=[]#将二重列表中元素列表的单个值分别提取出来，建立新的列表
for i in range(0,len(alist)):
        dnavalue1.append(alist[i][1]) #第二个是蛋白质的缩写


# In[37]:


dnavalue2=[]#将二重列表中元素列表的单个值分别提取出来，建立新的列表
for i in range(0,len(alist)):
        dnavalue2.append(alist[i][2]) #第三个是蛋白质的名称


# In[38]:


dnavalue2mx=[]#同样建立空列表，往里面添加元素
for i in range(0,len(dnavalue2)):
        dnavalue2mx.append(dnavalue2[i][:3])#这里采用的方法比较笨，提取第i个元素从0到3的字节消除符号\n


# In[39]:


RNAseqlist=list(zip(dnakey ,dnavalue1,dnavalue2mx))#将三个列表压缩为一个字典


# In[40]:


DNAseq = {}#定义字典
for i in range(0, len(dnakey)):#列表长度都一样，任意一个都可以
    DNAseq[dnakey[i]]=[dnavalue1[i], dnavalue2mx[i]]#构建一个字典，key为密码子，value为氨基酸列表


# In[41]:


DNAseq['TAA']=['*','STOP']#往里面添加这三个终止密码子，虽然不美观但是完美实现了代码
DNAseq['TAG']=['*','STOP']#一个关于密码子和对应氨基酸的字典就实现啦
DNAseq['TGA']=['*','STOP']


# In[42]:


filedna=open('d:\dna_sequence.fa','r')#采用r方式打开文件


# In[43]:


listdna2=filedna.readlines()#将文件读为列表


# In[44]:


listdna2


# In[45]:


dnanew=[]#采用for循环的方式，遍历每一个元素用repalce方法去除\n符号简直完美
for i in range(0,len(listdna2)):
        dnanew.append(listdna2[i].replace('\n','')) #去掉\n符号


# In[46]:


def DNA_complement(sequence):#copy的字典函数
    sequence = sequence.upper()#全部升为大写
    sequence = sequence.replace('A', 't')#大写A替换为小写t，这思路厉害了
    sequence = sequence.replace('T', 'a')#有效避免了A换为T后又被替换为A的问题，大小写分为了不同的但是意义相同的符号
    sequence = sequence.replace('C', 'g')
    sequence = sequence.replace('G', 'c')
    return sequence.upper()#最后全部升为大写就可以了
def DNA_reverse(sequence):
    sequence = sequence.upper()
    return sequence[::-1]#第三个空格表示取反读取


# In[48]:


DNA_sequence_1=dnanew[1]#验证一下，完美去除了\n符号
DNA_sequence_1


# In[109]:


def DNA_trans_protein1(rnaSeq):#copy，定义一个函数，这个函数包含了密码子与对应氨基酸缩写
    codonTable = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
        'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }
    proteinSeq = ""#定义一个空的字符串，神奇
    for codonStart in range(0, len(rnaSeq), 3):#range函数的使用，range(start, stop[, step])步长默认为1，这里设定步长为3
        #start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
        #stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
        #step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
        codon = rnaSeq[codonStart:codonStart + 3]#取列表rnaSeq中元素，这里可以三个三个的取
        if codon in codonTable:#取出来判断一下
            proteinSeq += codonTable[codon]#加进去字符串
    return proteinSeq

def DNA_trans_protein2(rnaSeq):#copy，定义一个函数，这个函数包含了密码子与对应氨基酸
    codonTable = {
        'ATA':'Ile', 'ATC':'Ile', 'ATT':'Ile', 'ATG':'Met',
        'ACA':'Thr', 'ACC':'Thr', 'ACG':'Thr', 'ACT':'Thr',
        'AAC':'Asn', 'AAT':'Asn', 'AAA':'Lys', 'AAG':'Lys',
        'AGC':'Ser', 'AGT':'Ser', 'AGA':'Arg', 'AGG':'Arg',
        'CTA':'Leu', 'CTC':'Leu', 'CTG':'Leu', 'CTT':'Leu',
        'CCA':'Pro', 'CCC':'Pro', 'CCG':'Pro', 'CCT':'Pro',
        'CAC':'His', 'CAT':'His', 'CAA':'Gln', 'CAG':'Gln',
        'CGA':'Arg', 'CGC':'Arg', 'CGG':'Arg', 'CGT':'Arg',
        'GTA':'Val', 'GTC':'Val', 'GTG':'Val', 'GTT':'Val',
        'GCA':'Arg', 'GCC':'Arg', 'GCG':'Arg', 'GCT':'Arg',
        'GAC':'Asp', 'GAT':'Asp', 'GAA':'Glu', 'GAG':'Glu',
        'GGA':'Gly', 'GGC':'Gly', 'GGG':'Gly', 'GGT':'Gly',
        'TCA':'Ser', 'TCC':'Ser', 'TCG':'Ser', 'TCT':'Ser',
        'TTC':'Phe', 'TTT':'Phe', 'TTA':'Leu', 'TTG':'Leu',
        'TAC':'Tyr', 'TAT':'Tyr', 'TAA':'STOP', 'TAG':'STOP',
        'TGC':'Cys', 'TGT':'Cys', 'TGA':'STOP', 'TGG':'Trp',
    }
    proteinSeq = ""#这里的原理也和上面的一样
    for codonStart in range(0, len(rnaSeq), 3):
        codon = rnaSeq[codonStart:codonStart + 3]
        if codon in codonTable:
            proteinSeq += codonTable[codon]
    return proteinSeq


# In[110]:


DNA_sequence_1#count函数
#str.count(sub, start= 0,end=len(string))参数
#sub -- 搜索的子字符串
#start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
#end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
a=DNA_sequence_1.count("G")
b=DNA_sequence_1.count("C")


# In[111]:


c=len(DNA_sequence_1)
d=((a+b)/c)*100#计算出百分数


# In[112]:


print('DNA_sequence_1的GC含量为:'+str(d)+"%")
print('DNA_sequence_1的反向互补序为'+DNA_reverse(DNA_complement(DNA_sequence_1)))
print('DNA_sequence_1的DNA蛋白符号为：'+DNA_trans_protein1(DNA_sequence_1))
print('DNA_sequence_1的DNA蛋白为：'+DNA_trans_protein2(DNA_sequence_1))


# In[113]:


DNA_sequence_2=dnanew[3]
a=DNA_sequence_2.count("G")
b=DNA_sequence_2.count("C")
c=len(DNA_sequence_2)
d=((a+b)/c)*100
print('DNA_sequence_2的GC含量为:'+str(d)+"%")
print('DNA_sequence_2的反向互补序为：'+DNA_reverse(DNA_complement(DNA_sequence_2)))
print('DNA_sequence_2的DNA蛋白符号为：'+DNA_trans_protein1(DNA_sequence_2))
print('DNA_sequence_2的DNA蛋白为：'+DNA_trans_protein2(DNA_sequence_2))


# In[114]:


DNA_sequence_3=dnanew[5]
a=DNA_sequence_3.count("G")
b=DNA_sequence_3.count("C")
c=len(DNA_sequence_3)
d=((a+b)/c)*100
print('DNA_sequence_3的GC含量为:'+str(d)+"%")
print('DNA_sequence_3的反向互补序为'+DNA_reverse(DNA_complement(DNA_sequence_3)))
print('DNA_sequence_3的DNA蛋白符号为：'+DNA_trans_protein1(DNA_sequence_3))
print('DNA_sequence_3的DNA蛋白为：'+DNA_trans_protein2(DNA_sequence_3))


# In[115]:


DNA_sequence_4=dnanew[7]
a=DNA_sequence_4.count("G")
b=DNA_sequence_4.count("C")
c=len(DNA_sequence_4)
d=((a+b)/c)*100
print('DNA_sequence_4的GC含量为:'+str(d)+"%")
print('DNA_sequence_4的反向互补序为'+DNA_reverse(DNA_complement(DNA_sequence_4)))
print('DNA_sequence_4的DNA蛋白符号为：'+DNA_trans_protein1(DNA_sequence_4))
print('DNA_sequence_4的DNA蛋白为：'+DNA_trans_protein2(DNA_sequence_4))


# In[116]:


DNA_sequence_5=dnanew[9]
a=DNA_sequence_5.count("G")
b=DNA_sequence_5.count("C")
c=len(DNA_sequence_5)
d=((a+b)/c)*100
print('DNA_sequence_5的GC含量为:'+str(d)+"%")
print('DNA_sequence_5的反向互补序为'+DNA_reverse(DNA_complement(DNA_sequence_5)))
print('DNA_sequence_5的DNA蛋白符号为：'+DNA_trans_protein1(DNA_sequence_5))
print('DNA_sequence_5的DNA蛋白为：'+DNA_trans_protein2(DNA_sequence_5))


# In[ ]:





# In[ ]:




