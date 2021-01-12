# Q1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
    
class UpgradeCalculator(Calculator):
    def sub(self, val):
        self.value -= val
               
# Q2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
           self.value = 100

# Q3 단답형
# False, True

# Q4
print(list(filter(lambda x: x>0, [1,-2, 3, -5, 8, -3])))

# Q5
print(int('0xea',16))

# Q6
print(list(map(lambda x: x*3,[1,2,3,4])))

# Q7
def minmaxsum():
    a = min([-8, 2, 7, 5, 3, 5, 0, 1])
    b = max([-8, 2, 7, 5, 3, 5, 0, 1])
    return(a + b)
print(minmaxsum())

# Q8
print(round(17/3,3))

# Q9
import sys
print(sys.argv)

# Q10
import os
os.chdir("c:\python_space")
f = os.popen("dir")
print(f.read())

# Q11
import glob
print(glob.glob("c:/python_space/*.py"))

# Q12
import time
print(time.strftime('%Y/%m/%d %X'))

# Q13
import random
li =[]
while len(li) < 6:
    a = random.randint(1, 45)
    if a not in li:
        li.append(a)
print(li)