#header

import matplotlib.pyplot as pmf
import random

p = 0.5 # Probablility of success for original system
n = 18 # Number of trials
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
    
    
for i in range(n+1):
    b[i] = b[i]/N # Probabilities
    p = 0

cv = int(input('Enter a choice for the CV.'))

for i in range(cv, 19):
    p = p + b[i]
    
print('For a critical value of', cv, 'the probability of rejecting the old system in favor of a new system that is no better than is', p,'.')
#cv = 13, 1/20 or the 5% rule