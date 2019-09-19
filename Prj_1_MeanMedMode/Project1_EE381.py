'''
EE381
Project 1
Ellen Burger
8/26/19
Program that takes user-submitted integers and finds the mean, median, and mode.
'''
        
list = [] # Empty list for input
v = 1 # Boolean
print('Enter a letter to stop submitting integers.')
while(v == 1):
    try:
        l = int(input('Enter a nonnegative integer.'))
        list.append(l)
                
    except:
        print('Input stopped.')
        v = 0
print(list)

'''Finding the mean'''
s = sum(list) # Sum of inputted numbers
N = len(list) # Number of numbers inputted
mean = s/N
print('Mean = ', mean)

'''Finding the median'''
N = len(list) # Number of numbers entered
list.sort() # Sorting ascendingly
if N % 2 == 0: # Even
    m1 = N/2
    m2 = (N/2) + 1
    m1 = int(m1)
    m2 = int(m2)
    m1 = m1 - 1
    m2 = m2 - 1
    median = (list[m1] + list[m2])/2
else: # Odd
    m = (N + 1)/2
    m = int(m)
    median = list[m]
print('Median = ', median)
        
'''Finding the mode'''
from collections import Counter
c = Counter(list) # creates tuples of elements in list
print(c)
        
freq = c.most_common() # most common method
max_occur = freq[0][1] # second element of tuples will be max
        
if max_occur != 1:
    modes = [] # empty list
    for m in freq:
        if m[1] == max_occur: # second position in tuple equal to max_occur
            modes.append(m[0])
            print('The mode(s) are: ', modes)
            
else:
    print('There is no mode.')
    