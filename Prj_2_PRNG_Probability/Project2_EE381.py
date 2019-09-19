'''
EE381
Project 2, Part 1
Ellen Burger
9/11/19
Program that generates 100 pseudorandom numbers based on user input
'''

### 1) Generating Pseudorandom Numbers
M = 8601
A = 4857
N = 10000

# Taking the seed from the user
S = float(input('Enter a value to start RNG.'))
print(S)

# Generating and printing to four decimals
for i in range(100):
    S = (M * S + A) % N
    print("{:.4f}".format(S))
    
'''Results:
Enter a value to start RNG.
5.123
5.123
8919.9230
5114.7230
6589.5232
1345.7869
9970.2624
9083.5569
2529.7123
2912.4598
4923.4669
1595.3893
6800.0398
1999.4871
2445.3962
7709.4243
3614.9833
7328.1823
4553.2622
7465.3347
4200.7390
5412.8278
588.4957
6508.2622
2420.2219
1185.6743
2841.7459
6713.8171
398.0659
8621.9417
2177.8812
6813.0786
4145.6235
1364.8185
3660.9883
3017.5943
9185.9660
3350.4619
2179.3730
9644.3811
6178.8834
9432.9977
8070.5597
9740.9242
6545.8845
6009.5209
2746.2915
5710.1777
8095.1968
1645.0948
4317.5304
9935.5644
646.7667
7697.7517
3219.4569
5405.9761
1657.2592
8943.4926
7836.4706
6340.7729
1845.0580
4201.2871
127.1896
8814.7841
815.2658
6958.0738
1249.4508
1383.3075
2684.7037
5993.7598
7185.3099
5707.1096
1706.9119
6006.2213
4366.0412
7177.4259
7897.1491
8236.3028
5297.1380
5540.9604
2657.3928
1092.8178
4183.3122
5524.8860
4401.3394
777.5487
2553.4943
7461.8443
4179.4039
1910.2463
4885.8340
7914.9456
1303.7201
8153.6305
4232.6992
302.7690
8973.1405
2838.3896
7845.6769
5524.3624
9898.2364
9588.1809
'''

'''
EE381
Project 2, Part 2
Ellen Burger
9/11/19
Program that simulates three balls being tossed into five cans
'''
import math
import time
t = time.process_time()

M = 8601
A = 4857
N = 10000

S = 1000 * t
Total = 0 # amount of times there are no repeats
Cups = [0,0,0]

Repeat = 1000
for i in range (Repeat):
    
    for j in range (3):
        S = (M * S + A) % N
        R = S/N
        result = math.floor(5*R + 1)
        Cups[j] = result
    #print(Cups)
    
    if (Cups[0] != Cups[1]):
        if (Cups[0] != Cups[2]):
            if (Cups[1] != Cups[2]):
                Total = Total + 1
                
Answer = Total/Repeat
print('Chance of a repeat =', Answer)

'''
Output:
Chance of a repeat = 0.499
'''

'''
EE381
Project 2, Part 3
Ellen Burger
9/11/19
Program that simulates two dice being rolled and recording occurence of sum three before seven
'''
import math
import time
t = time.process_time()

M = 8601
A = 4857
N = 10000

Total = 0 # amount of times sum is three
Range = 0 # occurences of three or seven
Cups = [0,0,0]

S1 = 1000 * t
S2 = 1000 + t

Repeat = 1000
for i in range (Repeat):
    
    
    S1 = (M * S1 + A) % N
    result = S1/N
    D1 = math.floor(6*result + 1)
    
    
    S2 = (M * S2 + A) % N
    result = S2/N
    D2 = math.floor(6*result + 1)
    
    Sum = D1 + D2
    #print(D1, D2, Sum)
    if Sum == 7:
        Range = Range + 1
    if Sum == 3:
        Total = Total + 1
        Range = Range + 1
                
Answer = Total/Range
print('Chance of three before seven =', Answer)

'''
Output:
Chance of three before seven = 0.24
'''

