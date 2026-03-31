heartrate=[72,60,126,85,90,59,76,131,88,121,64]
import numpy
import matplotlib.pyplot as plt
average=numpy.mean(heartrate)
print(f"there are total {len(heartrate)} patients and the mean of their heartrate is {average:.2f}")
low=normal=high=0
#these are numbers in this type of heart rate
for i in heartrate:
    if i<60:
        low+=1
    elif 60<=i<=120:
        normal+=1
    else:
        high+=1
print(f"low heart rate have {low} patients")
print(f"normal heart rate have {normal} patients")
print(f"high heart rate have {high} patients")
number={"low":low,"normal":normal,"high":high}
#create a dictionary to compare which one have the most patients
most=max(number,key=number.get)
#most is the type of heartrate, and most number is the specific number
mostnumber=number[most]
print(f"{most} heart rate have the most patients, there are {mostnumber} patients")
label=["LOW","NORMAL","HIGH"]
#pie chart category
sizes=[low,normal,high]
plt.figure(figsize=(10,10))
plt.pie(sizes,explode=(0,0,0),labels=label)
plt.axis("equal")
plt.title("HEART RATE CATEGORY")
plt.show()