import statistics
import array
import random
from numpy import insert
numRay=array.array('i',[])
for i in range(0,100):
    b=random.randrange(100)
    numRay.insert(i,b)
print(numRay)
a = statistics.mode(numRay)
print ("Most frequent number is : " + str(a))