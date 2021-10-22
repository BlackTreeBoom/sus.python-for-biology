file_name = 'd:\sgRNA_sequence.fa'#定义文件路径
file_handle = open(file_name,'r')#打开保存的文件，通过read方法打开
listRNA=file_handle.readlines()#将打开的文件转为列表
listname=listRNA[0::2]#采用间隔2的读取方式，从0位读取name
listseq=listRNA[1::2]#方法同上，差别在于从第一位开始
for name,seq in zip(listname,listseq): #将两个列表通过zip合并为一个字典
    for i in range(len(listname)):#遍历，i range 整个长度
        print('sgRNAnumber'+str(i+1)+'\nThe name of sgRNA is'+name+'The sequence of sgRNA is'+seq)
       #\n表示换行符，str（i+1）用于标记序号，换行符的位置要注意