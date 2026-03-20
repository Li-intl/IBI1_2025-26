import numpy
import matplotlib.pyplot as plt
dailysleep=float(input())
#all students' sleep time data
index=0
caculatelist=[0,0,0,0,0,0,0]
for i in dailysleep:
    caculatelist[index]=i
    index=(index+1)%7
    average=numpy.mean(caculatelist)
    print(average)
plt.figure(figsize=(10,10))
