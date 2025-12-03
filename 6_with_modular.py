import random
import json
import os

SCORE_FILE = "highscores.json"

def load_high_score():
    if not os.path.exists(SCORE_FILE):
        return None
    with open(SCORE_FILE, "r") as file:
        return json.load(file)

def save_high_score(score):
    with open(SCORE_FILE, "w") as file:
        json.dump(score, file)

def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy   (1–10,    5 attempts)")
    print("2. Medium (1–50,   7 attempts)")
    print("3. Hard   (1–100, 10 attempts)")
    
    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice == "1":
            return (1, 10, 5)
        elif choice == "2":
            return (1, 50, 10)
        elif choice == "3":
            return (1, 100, 15)
        else:
            print("Invalid choice! Try again.")

def get_valid_guess(low, high):
    while True:
        guess = input(f"Enter your guess ({low}-{high}): ").strip()
        if guess.isdigit():
            guess = int(guess)
            if low <= guess <= high:
                return guess
        print("Invalid input. Try again.")

def play_game():
    low, high, max_attempts = choose_difficulty()
    secret = random.randint(low, high)
    attempts = 0

    while attempts < max_attempts:
        guess = get_valid_guess(low, high)
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"You guessed it in {attempts} attempts!")
            return attempts

    print(f"You ran out of attempts! The number was {secret}.")
    return None

def update_high_score(result, high_score):
    if result is None:
        return high_score  # no win, no update

    if high_score is None:  
        print("First score saved!")
        return result

    if result < high_score:
        print("New high score!")
        return result
    else:
        print("You did not beat the high score.")
        return high_score

def main():
    print("\n=== NUMBER GUESSING GAME ===")

    high_score = load_high_score()

    while True:
        result = play_game()
        high_score = update_high_score(result, high_score)
        save_high_score(high_score)

        print("\nPlay again? (y/n)")
        again = input("> ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

main()