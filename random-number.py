# This is a guess the number game.
import random
import time

while True:
    secretNumber = random.randint(1,100)
    print('I am thinking of a number between 1 and 100.')

    # Ask the player to guess 5 times.
    for guessesTaken in range(1,5):
        print('Take a guess.')
        guess = int(input())

        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break # This is the correct guess!

    if guessesTaken == 1:
            print('Holy Cow! You guessed my number in ' + str(guessesTaken) + ' try!')
    
    if guess == secretNumber:
        print('Congrats! You guessed my number in ' + str(guessesTaken) + ' guesses!')
        print('Try Again? (y/n)')
        if input() != "y":
            break
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')
        time.sleep(.50)
        print('Try Again? (y/n)')
        if input() != "y":
            break