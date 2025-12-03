import random

LOW = 1
HIGH = 100
secret = random.randint(LOW, HIGH)
attempts = 0

print(f"I'm thinking of a number between {LOW} and {HIGH}...")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")
