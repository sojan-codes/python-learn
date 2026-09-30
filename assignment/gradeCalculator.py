#Grade Calculator
name = input('Enter your Name: ')
score = int(input('Enter your Score: '))

isPass = True
A = 'your grade is A'
B = 'your grade is B'
C = 'your grade is C'
F = 'your grade is F'

if (score >= 0 and score <=100):
    if (score > 90):
        print('Name:', name, '\nScore:', score, '\nPassed:', isPass, f'\n{name},', A)
    elif (score > 75):
        print('Name:', name, '\nScore:', score, '\nPassed:', isPass, f'\n{name},', B)
    elif (score > 60):
        print('Name:', name, '\nScore:', score, '\nPassed:', isPass, f'\n{name},', C)
    else:
        isPass = False
        print('Name:', name, '\nScore:', score, '\nPassed:', isPass, f'\n{name},', F)
else:
    print('Invalid Score.')