import array
import random

from numpy import insert
numRay=array.array('i',[])
for i in range(0,100):
    b=random.randrange(100)
    numRay.insert(i,b)
print(numRay)
arr_size = len(numRay)
for i in range(arr_size):
    x = numRay[i] % 100
    numRay[x] = numRay[x] + 100
 
print("The repeating elements are : ")
for i in range(arr_size):
    if (numRay[i] >= 100*2):
        print(i, " ")
 