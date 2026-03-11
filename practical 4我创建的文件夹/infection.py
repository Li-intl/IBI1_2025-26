day=float(0)# is it okay that the start day is day 0?
rate=float(0.4)#rate is 40%
number=float(5)#it is "at the beginning, the number of student who is infected"
all=float(91)# all is that in IBI1 there are 91 students.
#set all the variables
#the infection number= initial number * (rate+100%)
#and after one caculate, day count +1
#If inection number is smaller than students number, start a new day.
#If infection number is larger than students number, end the caculation.
#and the infection number cannot larger that the students number.
while number<91:
    number=number*(1+rate)
    day+=1
    if number>all:
        number=all#infected students can not be more than all student.
    print("day:"+ str(day), "infection number"+ str(number))
print("it need"+ str(day) + "for the whole to get infected")#how many days it takes for the whole class to get infected
