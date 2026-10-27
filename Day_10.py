# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def div(x, y):
#     return x / y

# def power(x, y):
#     return x ** y

# def calculator():
#     operation = input('Enter operation: ')
#     match(operation):
#         case 'add':
#             print('Result: ',add(first_value, second_value))
#         case 'sub':
#             print('Result: ',sub(first_value, second_value))
#         case 'multiply':
#             print('Result: ',multiply(first_value, second_value))
#         case 'div':
#             print('Result: ',div(first_value, second_value))
#         case 'power':
#             print('Result: ',power(first_value, second_value))


# first_value = int(input('Enter first number: '))
# second_value = int(input('Enter second number: '))
# calculator()


print('==============')
print('Task 1')

def greet(name):
    print(f'Hello {name}')

name = 'Sojan'
greet(name)

print('Task 2')

def square(n):
    return n**2
n = int(input('Enter a number:'))
print(square(n))

print('Task 3')

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input('Enter a number: '))
print('Is Even: ', is_even(n))

print('Task 4')
def area(l, m):
    return l * m

l = int(input('Enter Length: '))
m = int(input('Enter bredth: '))
print("Area", area(l,m))


print('Task 5')
def biggest(a, b, c):
    list = [a, b, c]
    big = list[0]
    for i in list:
        if i > big:
            big = i
    return big

a = int(input('Enter first number: '))
b = int(input('Enter Second number: '))
c = int(input('Enter Third number: '))

print('Biggest', biggest(a, b, c))

print('Task 5')

count = 0
def add():
    global count
    count += 1

add()
print(count)
    



