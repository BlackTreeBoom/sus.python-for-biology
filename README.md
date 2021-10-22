# sus.python-for-biology
南科大python作业的分析布局

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
