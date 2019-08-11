import numpy 
A = [['Ty', 'Suu','Dan','Meo','Thin','Ty','Ngo', 'Mui', 'Than','Dau','Tuat','Hoi'],
                [4 ,     5   ,  6   , 7  ,  8   ,    9 ,     10  ,  11  ,   12    ,  13 ,    14 ,    15],
                [16  ,  17   , 18 ,   19  ,  20     ,  21 ,  22   , 23    , 24   ,   25   ,  26  ,   27],
                [28   , 29   , 30  ,  31  ,  32    ,   33 ,  34   , 35   ,  36    ,  37   ,  38   ,  39],
                [40   , 41  ,  42   , 43  ,  44    ,   45 ,  46   , 47  ,   48    ,  49   ,  50   ,  51],
                [52   , 53 ,   54   , 55 ,   56    ,   57 ,  58   , 59  ,   60    ,  61    , 62   ,  63]]
with open('./data_out.csv', 'r',encoding ='utf-8',errors='ignore') as fin:
    lines= fin.readlines()
    b=[]
    for line in lines[1:50]:
        info=line.split('\t')
        info[2]=int(info[2])
        info[2]=2019-info[2]
        for i in range(len(A)):
            for j in range(len(A[i])):
                if (info[2]% 60)==A[i][j]:
                    b=b+[A[0][j]]
    print(b)
                    
                    
