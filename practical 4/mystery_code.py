# What does this piece of code do?
# Answer: This script calculates and prints the sum of 11 randomly generated integers (each between 1 and 10).

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil # Note: This function is imported but NEVER actually used in the code below!

total_rand = 0   # Initializes a variable to keep track of the running total sum
progress = 0     # Initializes a counter variable to control the loop

# Starts a while loop. 
# Because progress starts at 0 and the condition is '<= 10', 
# it will run for progress = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. 
# This means the loop executes exactly 11 times.
while progress <= 10:
	progress += 1        # Increments the progress counter by 1 in each iteration
	n = randint(1,10)    # Generates a random integer between 1 and 10
	total_rand += n      # Adds the newly generated random number 'n' to the 'total_rand' sum

# Prints the final accumulated sum to the console after the loop finishes
print(total_rand)
