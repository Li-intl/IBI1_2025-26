import numpy
import matplotlib.pyplot as plt
dailysleep=float(input())
#all students' sleep time data这个变量是所有的数据，就是全部的睡眠时长
index=0
#index是用来取数的，在列表caculatelist里面将第index序列的数换成睡眠数据，然后让index+=1，这样下一次替换就会替换掉下一个列表中的数而不会替换掉刚放进来的
#因为需要“动态循环”，所以要用%7取余数，这样过了7，又回回到0：0.1.2.3.4.5.6.0.1.2.3....
caculatelist=[0,0,0,0,0,0,0]
for i in dailysleep:
    caculatelist[index]=i
    index=(index+1)%7
    average=numpy.mean(caculatelist)
    print(average)
plt.figure(figsize=(10,10))


#haven't finished! Chinese are my note. My classmates at the tutorial taught me the code aboving.