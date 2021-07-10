import random

print("Number guessing game!")

number = random.randint(1,9)
chances = 0 

print("Guess a number between 1-9 (You only have 5 chances to guess correctly)")

while chances < 5:
    guess = int(input("Enter your guess:"))
    if guess == number:
        print("Congratulations, you won!")
        break
    elif guess < number:
        print("Your guess is too low, guess again", guess)
    else:
        print("Your guess is too high, guess again", guess)
    
    chances += 1

if not chances < 5:
    print("You lose! The number is: ", number)