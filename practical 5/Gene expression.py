import matplotlib.pyplot as plt
import matplotlib
print(matplotlib.__version__)
#I search guidance for matplotlib and it told me I can use this to test my matplotlib. it works well, output is "3.10.8"
# and the online vedio told that "as plt" can help me save time so that I do not need print matplotlib for each time.
import numpy
# create dictionary{geneexpression}
geneexpression={"TP53":8.2,"EGFR":9.5,"ALK":7.8,"BRAF":10.1,"KRAS":6.9}
#add MYC
geneexpression["MYC"]=11.6
#print(geneexpression)
#test the dictionary{geneexpression} and output is okay
GENE=list(geneexpression.keys())
#variable:GENE. it is the x in the chart
EXPRESSION=list(geneexpression.values())
#variavle:EXPRESSION. it is the y in the chart
plt.figure(figsize=(10,10)) 
#set size of chart
plt.bar(GENE,EXPRESSION)
#bar chart
plt.title("GENE EXPRESSION LEVEL")
#title
plt.xlabel("GENE")
plt.ylabel("EXPRESSION")
plt.xticks(rotation=45) #this line is written by AI and I now understand what it means
plt.grid(axis='y', linestyle='--', alpha=0.7)#this line is written by AI and I now understand what it means
plt.show()
#output the chart I am happy that it works well.
testgene1="ABC"
testgene2="TP53"
#test gene variable, which is not in dictionary{genedictionary}
test=testgene1
if test in geneexpression:
    print(str(test)+"expression level is:  "+str({geneexpression[test]}))
else:
    print(str(test)+ " is not in dictionary{geneexpression}")
test=testgene2
if test in geneexpression:
    print(str(test)+" expression level is:  "+str({geneexpression[test]}))
else:
    print(str(test)+ " is not in dictionary{geneexpression}")
#caculate the average 
average=numpy.mean(EXPRESSION)
print("the mean of gene expression is "+str(average))


#honestly ,line 25 and line 26 are AI's help. I ask AI whether I can make the bar chart better, AI give me these two line.
#other codes are written by myself. and I understand that 2 lines of codes' meaning.