'''
@Author: Bikash Singh
@Date: 25/309/2022
@Title : To find the factor of a number
'''

number = int(input("Enter The Number:"))

print("The factors of",number,"are,")

for i in range(1,number+1):
    if number % i == 0:
        print(i)

