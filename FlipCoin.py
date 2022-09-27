'''
@Author: Bikash Singh
@Date: 23/09/2022
@Title : To flip a coin and calculate its percentage
'''
import random

heads = 0
tails = 0
number = int(input('Enter the number to flip coin :\n'))

for i in range(0, number):
    coin = random.randint(0,1)
    if coin < 0.5:
        print("Tails")
        tails +=1
    else:
        print("Heads")
        heads +=1
headsPercentage = heads / number * 100
tailsPercentage = tails / number * 100
print("Total Percentage of Head ", headsPercentage)
print("Total Percentage of Tails ", tailsPercentage)