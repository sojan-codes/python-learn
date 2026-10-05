secret = 7
tries = 0
while True:
    tries += 1
    guess = int(input(f'Try {tries},Enter a Number: '))
    if guess == secret:
        print('Congratulations!, Correct Guess')
        break
    elif guess > secret:
        print('Too High')
    else:
        print('Too Low')
