from random import *

number = randint(1,9)
turnsDone = 0


while True:

    guess = int(input("Guess a number between 1 and 9 : "))

    turnsDone = turnsDone + 1

    if guess == number:
        print("You win!")
        break
    elif not turnsDone < 5:
        print("You lose :(, it was", number)
        break
    elif guess > number:
        print("Guess lower next time")
    elif guess < number:
        print("Guess higher next time")  
    

    