#Question no 1
n1 = int(input('Enter a Number: '))

if (n1 > 0):
    print('Positive')
elif (n1 < 0):
    print('Negative')
else:
    print('Zero')

#Question no 2
n2 = int(input('Enter a Number: '))

if(n2 % 2 == 0):
    print('Even')
else:
    print('Odd')

#Question no 3
age = int(input("Enter Age: "))

if(age < 13 and age >= 0):
    print('Child')
elif(age >= 13 and age < 20):
    print('Teen')
else:
    print('Adult')

#Question no 4
a, b = 8, 3

if (a > b):
    print('A is Larger')
else:
    print('B is Larger')

#Question no 5
password = 'python2026'
pw = input('Enter Password: ')

if (pw == password):
    print('Welcome for django123')
else:
    print('Access Denied.')

#Question no 6
year = int(input('Enter Year: '))

if year % 400 == 0:
    print('It is a Leap year.')
elif year % 100 == 0:
    print('It is not a Leap year.')
elif year % 4 == 0:
    print('It is a Leap year.')
else:
    print('It is not a Leap year.')