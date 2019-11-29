'''
EE381
Project 5
Ellen Burger
015263571
11/20/19
Hypothesis test small sample proportion (binomial RV)
'''

import matplotlib.pyplot as pmf
import random

p = 0.5 # Probablility of success for original system
n = 18 # Number of trials
a = [] # The values for the x-axis for the plot
Y = [] # Contains binomial RVs
b = [0] * (n+1) # List of n + 1 zeroes
N = 100 # Number of experiments performed

for j in range(N):
    
    # Bernoulli random variable
    for i in range(n):
        
        r = random.uniform(0,1)
        if r < p:
            x = 1
        else:
            x = 0
        Y.append(x)
    outcome = sum(Y) # Number of successes from 0 to n
    b[outcome] = b[outcome] + 1 # Record of successes for bar plot
    Y.clear()


# Bar plot
pmf.title('Histogram of binomial R.V., Y', loc = 'right', color = 'b')
pmf.xlabel('Values of the y for the R.V., Y')
pmf.ylabel('Probabilities for the y values of the R.V., Y')
width = 1

for i in range(n+1):
    a.append(i)
    
for i in range(n+1):
    b[i] = b[i]/N
    
pmf.bar(a, b, width, color=['g','r','y','m','c','b'])

#part 3, p = float(input("Enter probability of success"))