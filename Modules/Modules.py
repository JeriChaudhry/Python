# Modules


#import math

#number = float(input("Enter a number: "))

#answer =math.sqrt(number)

#print(answer)

import math
import random

def multiply_pi():
    return random.randint(1,7) * math.pi

for i in range(3):
    print(multiply_pi())



