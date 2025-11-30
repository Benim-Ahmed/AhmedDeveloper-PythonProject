num1 = float(input("Please enter first number: "))
num2 = float(input("Pleasae enter second number: "))

print(f"Sum of {num1} and {num2} = ", num1 + num2)
print(f"Difference of {num1} and {num2} = ", num1 - num2)
print(f"Product of {num1} and {num2} = ", num1 * num2)
if num2 != 0:
    print(f"Quotient of {num1} and {num2} = ", num1 / num2)
elif num2 == 0:
    print("Cannot divide by zero! enter a valid number")

import random

def haroon_game():
    print("Welcome to Haroon's Guessing Game!")
    print("I have selected a number between 1 and 50.")
    number = random.randint(1, 50)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
while True:
    haroon_game()
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Goodbye :)")
        break