# Law of large numbers
import numpy as np
from numpy.random import randn

randn(100)

mylist = [10, 100, 1000]

for i in mylist:
    print("hello ", i)
    
    
N = 100                      #specify sample size
counter = 0                  # reset counter
for i in randn(N):           #iterate over random values
    if(i >- 1 and i < 1):    # check where iterated variable falls
        counter = counter + 1 #increase counter if condition is met
answer = counter / N         #calculate hit-ratio
print(answer)                #print answer
