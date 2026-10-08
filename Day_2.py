print('String')
#string
b = 'string'
print(id(b))

b = 'newString'
print(id(b))

print('Float')

#float
c = 2.4
print(id(c))

c = c + 1
print(id(c))

print('Boolean')
#boolean
d = True
print(id(d))
d = not d
print(id(d))

#pop
print('pop-')
example_list = [10, 20.0, 20, 30]

example_list.pop()
print(example_list)
print(example_list.pop())

#sort
print('sort-')
value = [10, 50, 30, 20]
value.sort()
print(value)
print(value.sort())

#reverse
print('reverse-')
value2 = [10, 20, 30, 40]
value2.reverse()
print(value2)
print(value2.reverse())

#count
print('count-')
value3 = [2, 2, 3, 1, 1]
val = value3.count(2)
print(val)

print('---Reverse order---')
value = [1, 2, 3, 4, 5]

print(value[::-1])

# for i in range(5):
#     j = i + 1
#     for j in range(5):
#         if(value[i] < value[j]):
#             temp = value[i]
#             value[i] = value[j]
#             value[j] = temp



print('---Using Membership operator---')
newValue = ['apple', 'banana', 'Orange']

print('banana' in newValue)
print('Grapes' in newValue)

print('Task 1')
colors = ['red']
colors.append('Green')
print(colors)

print('Task 2')
nums = [5, 8, 2, 9]
print(nums[0], nums[3])

print('Task 3')
nums = [5, 8, 2, 9]
print(nums[1:3])

print('Task 4')
pets = ['cat', 'dog']
print('dog' in pets)

# print('Task 5')
# email = input("Enter your Email: ")
# print('@' in email)

i = 0
while i < 10:
    print(i)
    if(i == 2):
        break
    else:
        i += 1

print(list(range(0,4)))

    
