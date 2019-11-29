#header

import random

cv = 13
p = float(input('Enter a value of p from 0.5 to 1 in steps of 0.5')) # Probablility of success for original system
beta = [0] * 11
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
    
beta = 0
for i in range(0, cv):
    beta = beta + b[i]
    
print("For value of p",p,"you chose the prob of rejecting the new system with prob",p,"of success in favor of old system is",beta,".")
#Higher p, less chance of rejecting the new systems