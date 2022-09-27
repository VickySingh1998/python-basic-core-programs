'''
@Author: Bikash Singh
@Date: 25/09/2022
@Title : To find if a year is leap year or not
'''

Year = int(input("Enter the number: "))

if ((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):
    print ("Year is leap Year")
else:
    print("Year is not a leap Year");