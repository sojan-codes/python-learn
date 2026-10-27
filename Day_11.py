def greet_name(name):
    def format_name(name):
        return name.strip()
    formatted_name = format_name(name)
    return  f'Welcome to class {formatted_name}'

print(greet_name('  ram sharma  '))

print('Task 1')

def uppercase_only(value):
    def filter_lowercase(value):
        newString = ''
        for i in value:
            if i == i.upper():
                newString += i
        return newString
    return filter_lowercase(value)

value = 'SOjaN BuddhaChaRyA'
print(uppercase_only(value))

print('Task 2')
def sum_of_n(value):
    if value == 0:
        return 0
    return value + sum_of_n(value - 1)

print(sum_of_n(5))

print('Task 3')
def fibo(value):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    return fibo(value - 1) + fibo(value - 2)
       
val = []
for i in range(5):
    val.append(fibo(i))

print(val)