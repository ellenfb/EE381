'''
EE381
Project 3, Part 1
Ellen Burger
9/24/19
Program that simulates a Bernoulli Random Variable using Python RNG, and creates a discrete Markov Chain based on user-inputted p and q.
'''
import random

#Simulation of Bernoulli RV

chance = float(input('Enter the probability of success.'))
repeat = int(input('Enter the number of experiments.'))
success = 0
failure = 0

for i in range(repeat):
    bin = random.uniform(0,1)       # random binary
    if (bin < chance):              # If binary exceeds probability of success, print 1 (success)
        print('1', end = ' ')
        success = success + 1
    else:                           # If binary doesn't exceed, print 0 (failure)
        print('0', end = ' ')
        failure = failure + 1

print('Successes =', success)
print('Failures =', failure)

'''
Output: Success of 0.4 and 20 experiments
1 1 0 1 0 1 1 1 1 0 0 0 1 1 1 0 0 1 0 0 
Successes = 11
Failures = 9
'''

#Simulation of Discrete Markov Chain

Particle = []                   # What node particle lands on
Node = random.randint(0,1)      # Starting node and where it jumps to
Particle.append(Node)           # Adding starting node to Particle list

p = float(input('Input chance of jumping from node 0 to 1.'))
q = float(input('Input chance of jumping from node 0 to 1.'))

for i in range(24):
    r = random.uniform(0,1)
    if Node == 0 and r < p:     # Jumps from 0 to 1
        Node = 1
    elif Node == 1 and r < q:   # Jumps from 1 to 0
        Node = 0
    Particle.append(Node)
    
for i in range(25):
    print(Particle[i], end=' ')
    
'''
Output:
    a) 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    b) 1 1 0 0 0 1 0 1 1 1 0 0 1 1 1 1 1 0 1 0 1 1 0 1 1 
    c) 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
    d) (0.6 & 1) 0 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 0 
    e) (0.2 & 0.4) 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 
'''

