'''
@Author: Bikash Singh
@Date: 26/09/2022
@Title : To find the Value of Nth Harmonic Number
'''

result = 1.0
number = int(input("Enter a Number: "))

for i in range(1, number):
    result = result+1/i
    print(result, " ")
print("")
print("Nth Harmonic Value : ", result)