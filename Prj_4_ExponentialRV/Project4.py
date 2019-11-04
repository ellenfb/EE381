'''
EE381
Project 4
Ellen
11/4/19
Program that simulates exponential random variables using the inverse transformation method from uniform random variables.
'''

import random
import math
import matplotlib.pyplot as plot

n = 10000                # Amount of random variables created
uniform = []             # List of uniform random variables
expon = []               # List of exponential random variables
lamda = 1                # Parameter for exponential RV calculation

for i in range(n):
    r = random.uniform(0,1)     # Generating uniform RV
    uniform.append(r)           # Appending to the uniform list
    e = -(1/lamda)*math.log(1 - r, math.e)  # Calculating the exponential RV
    expon.append(e)             # Appending to the expon list
    
b = max(uniform)
a = min(uniform)
R = b - a               # Range of the uniform list

intervals = int(math.ceil(math.sqrt(n))) # Number of "bins" used in plots to display the results

width = (R / intervals) # Width of the bins

# Creating the uniform and exponential plots
plot.subplot(2, 1, 1)
plot.hist(uniform, intervals, normed = width)
plot.subplot(2, 1, 2)
plot.hist(expon, intervals, normed = width)