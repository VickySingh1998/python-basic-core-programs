'''
@Author: Bikash Singh
@Date: 25/09/2022
@Title : To calculate the power of 2 table
'''

number = 1
power = int(input("Enter the power of 2 :"))

for i in range(1, power + 1):

    if 0<=power<31:
        number = 2 * number
        print("2","^", i,"=", number)
    else:
        print("Invalid Input")
        break

