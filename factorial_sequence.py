# Sum of factorials
from math import factorial
import numpy as np
#import math

i = 1
results = [] #np.array([[0, 0, 0]])
#results.reshape
accsum = 0

while i < 40:
    accsum += factorial(i)
    if accsum ** 0.5 - int(accsum ** 0.5) < 0.00001 :
        #np.append(results, [[i, int(accsum ** 0.5), accsum]], axis = 0)
        results.append((i, int(accsum ** 0.5), accsum))
    i += 1
    
print(results)
    