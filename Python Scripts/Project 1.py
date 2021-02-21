# Must display: current time and date, total, free, and used hard disk space, and randomly generated number from 0-100.
import datetime
import shutil
import random
from random import randint

# Import python libraries that allow us to use functions for completing basic tasks.

x = ' '
print(x)
# A trick to print a blank line in your script so it looks like a clean break between outputs of different functions.
# X is defined as a blank line so it prints a blank line.

today = datetime.datetime.today()
print("The current date and time is: ")
print(today.strftime("%Y-%m-%d %H:%M:%S"))

print(x)
# Using datetime library to make a function that is told to print "The current date and time is: "
# Then printing strftime in the format that we choose, in this case I chose %Y-%m-%d %H:%M:%S for simplicity.

total, used, free = shutil.disk_usage("/")
print("The breakdown of the storage on your hard disk is: ")
print("Total Space: %d GiB" % (total // (2 ** 30)))
print("Used Space: %d GiB" % (used // (2 ** 30)))
print("Free Space: %d GiB" % (free // (2 ** 30)))

print(x)
# Telling shutil to use disk_usage to give us statistics on a given path with the attributes total, used, and free.
# Then printing each line for total, used and free, as well as printing a title and formatting each one with %d.

for _ in range(100):
    randomNumber = randint(0, 100)
print("Your random number is: ")
print(randomNumber)
# Using randint from the random library to generate a random integer on a given range.
# Using a for loop to search for any integer in the range 0-100 and then defining it as randomNumber and printing it.

print(x)
print("This is the end of Johnathan Juilfs' Python Project 1!")
# Print ending line.
