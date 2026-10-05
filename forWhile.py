print('Task 1')
n = 1
while n < 11:
    print(n)
    n += 1

print('Task 2')
n = 10
while n >= 1:
    print(n)
    n -= 1

print('Task 3')
word = 'python'
for i in word:
    print(i)

print('Task 4')
start = 2
for i in range(1,21):
    if (i % 2 == 0):
        print(i)

print('Task 5')
n = 5
for i in range(1,11):
    print(n, "X", i, "=", n*i)

print('Task 6')
nums = [4, 9, 2]
data = 0
for i in nums:
    data += i

print(data)

name = 'yugan'
listed_value = list(name)
result = str(listed_value)
print(type(listed_value))
print(type(result))
print(result)
print(''.join(listed_value))
print(''.join(result))

print('Another Task')
n = 9
for i in range(1, 11):
    print(n, 'X', i, '=',n*i)

print('Sum of 9')
n = 0
i = 1
while i < 10:
    n += i
    i += 1

print(n)