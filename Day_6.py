# names = ['ram','hari', 'sita', 'gita']

# first_name = input('Enter Name:')

# if first_name in names:
#     print("Name Found")
# else:
#     print('Name not found')

#Task 1
values = [10, 20, 30, 40, 50]

for i in values:
    if i == 20:
        print('20 is found')
        break

#Task 2
values = [5, 10, 15, 20, 50, 25]

for i in values:
    if i > 30:
        print('Number greater than 30 is found in the list.')

#Task 3
values = ['ram', 'hari', 'shyam', 'Gita', 'Narayan']

for i in values:
    l = len(i)
    if l > 5:
        print(f'{i} has length greater then 5')

print('=====================')

strings = ['10', '20', 'abc', '30', 'xyz', '40']
newValue = []

for i in strings:
    try:
        int_value = int(i)
        newValue.append(int_value)
    except:
        print(f"{i} cannot be converted into integer")

print(newValue)
print('=====================')
set_guess_number = int(input("Enter a number: "))
attempt = 5
while True:
    if attempt == 0:
        print('Game Over!')
        break
    user_input = int(input(f'Attempt: {attempt}, Guess Number: '))
    if user_input == set_guess_number:
        print('Congratulation Correct Number!')
        break
    elif user_input > set_guess_number:
        print('Too high!')
        attempt -= 1
    else:
        print('Too low!')
        attempt -= 1

#Task 1
n = int(input('Enter a number: '))
sum = 0
for i in range(n + 1):
    sum += i

print(sum)

#Task 2
word = input('Enter a Word: ')
length = len(word)
revWord = ''
for i in range(1, length + 1):
    revWord += word[-i]
    length -= 1

print(revWord)

#Task 3
word = input('Enter a Word: ')
data = word.lower()
count = 0

for i in data:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        count += 1

print(f'The number of Vowels is {count}') 

#Task 4
n = int(input('Enter a number: '))
fact = 1
for i in range(1, n + 1):
    fact = fact * i

print(f'The Factorial of {n} is {fact}')

#Task 5
password = 'django123'

while True:
    pw = input('Enter the Password: ')
    if pw == password:
        print('Correct Password')
        break
    else:
        print('Incorrect Password. Try Again')

#Task 6
nums = [8, 3, 120, 5, 30, 5]
max = nums[0]
for i in nums:
    if i > max:
        max = i

print(max)





