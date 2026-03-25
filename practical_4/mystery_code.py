# What does this piece of code do?
# Answer:It extracted ten random numbers(from 1 to 10, including 1 and 10) and calculated their sum.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

#set variable, total is their sum
#progess is "how many times it had worked",and it helps the progrem end at the 10th time.
total_rand = 0
progress=0
while progress<=10:
	progress+=1
	n = randint(1,10)
	total_rand+=n

#output the sum
print(total_rand)

