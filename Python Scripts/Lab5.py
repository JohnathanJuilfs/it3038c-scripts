# Takes 2 integers as input and calculates how many prime numbers come between it and zero.
upper = 1000
lower = 900
print ("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower,upper):
    if all(num%i!=0 for i in range(2,num)):
        print (num)