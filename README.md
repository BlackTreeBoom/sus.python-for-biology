# sus.python-for-biology
南科大python作业的分析布局

 (1)第三周作业

    计算两点欧几里得距离和曼哈顿距离
    欧几里得（平方绝对值）  曼哈顿距离（路径xy）
    建立一个关于基因的字典用于判断基因的表达水平与是否在列表中

（1）第四周的作业第一部分
     读取sgRNA文件，打印name 和sequence 
     
     输出格式要求
     
     1.sgRNA number X
     
     2.The name of the sgRNA is XXX
     
     3.The sequence of the sgRNA is XXX
     
（2）读取condon_table.csv 文件，generate a codon table dictionary  CTT[L,Leu]
     写一个程序，用于从dna_sequence.fa中读取DNA sequence
     
     输出格式要求
     
     1.calculate the GC content
     
     2.print the reverse complement sequence
     
     3.print the coded amino acid in triplr_and single_letter formats
     
 (3)第五周作业
    
    DEG文件夹中包含了不同基因的表达分析，记录了相关的实验遗传信息
    文件夹中各个文件的名字包含了cell type 和 gene perturbation
    
    例如：d7_neuron_top50_edgeR_ATP5A1.csv
    
    要求：
    
    读取文件夹中的每一个文件，判断变换基因（FDR<0.05）如果是就提取出来，并作为新的CSV文件进行打印输出
    输出的文件要求：ID,Symbol,logFC,FDR,gene_perturbed
    
（4）第六周作业
  
    Bonus:
    Create Structure, Chain, Residue and Atom classes. Read the PDB file for TRPV1, 3j5p.pdb, and create a Structure object that contains Chain, Residue and Atom objects             hierarchically.![image](https://user-images.githubusercontent.com/90825733/140929959-0fc8b929-ca00-4b30-9a46-8cb74bb65693.png)

 （5）第七周作业
   
   Load the list of codon tuples from the codon_tuple.pickle file
   Generate a panda DataFrame as below:
   ![image](https://user-images.githubusercontent.com/90825733/140930374-6d41a0f8-657e-4d09-9dd2-00c3390f2bbf.png)
   
 （6）第八周作业
  ![image](https://user-images.githubusercontent.com/90825733/140930526-59243826-6775-4ce5-8bc8-3b943936a177.png)
  3 files:
  1. gene_phenotype.csv:
  Gene names and their knockdown phenotypes (positive : beneficial for survival; negative: toxic for survival; larger absolute value: larger effect )
  2. sgRNA_score.txt
  sgRNA names, their targeting genes and their scores from the screen (the higher the better)
  3. CRISPRi_v2.txt
  sgRNAs for all genes in the genome, and their predicted scores
  Goal:
  Find the sgRNA sequences for the top sgRNAs.
  Generate a csv file that contains sgRNA sequences for the best 3 sgRNAs for each of the top 10 positive and negative genes hits.排名最高的和最低的十个基因提取出来，看那个RNA最好用python操作excel表



   


