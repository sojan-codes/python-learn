from functools import reduce
# Task 1
list_value = ["a", "e", "i", "o", "u"]

new_list = list(map(lambda x: x.upper(), list_value))

print(new_list)

# Task 2
list_items = list(range(1,101))

odd_items = list(filter(lambda x: x % 2 != 0, list_items))
print(odd_items)

#Task 3
nums = [4, 5, 2, 7, 1, 6, 19]

min = reduce(lambda x,y: x if x < y else y, nums)
print("Min:", min)

#Task 1
cube = lambda x: x**3

print(cube(3))

# Task 2
temps = [0, 25, 100]

fahrenheit = list(map(lambda x: x * 9/5 + 32, temps))
print(fahrenheit)

# Task 3
names = ["Ram", "Sita", "Hari", "Om"]

names_list = list(filter(lambda x: len(x) > 3, names))
print(names_list)

nums = list(range(1,6))
square = [x**2 for x in nums]
print(square)

fruits = ["apple", "mango"]
upper_case = [x.upper() for x in fruits]
print(upper_case)

nums = [-2, 5, -1, 8]
new_num = [x if x > 0 else 0 for x in nums]
# another = [x for x in nums if x > 0]
# print(another)
print(new_num)