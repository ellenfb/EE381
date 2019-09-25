'''
EE381
Project 3, Part 1
Ellen Burger
9/24/19
Program that simulates a Bernoulli Random Variable using Python RNG, and 
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