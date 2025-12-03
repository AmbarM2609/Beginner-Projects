import random

DIFFICULTIES = {
    "1": {"name": "Easy",   "low": 1,   "high": 20,   "max_attempts": 10},
    "2": {"name": "Medium", "low": 1,   "high": 100,  "max_attempts": 7},
    "3": {"name": "Hard",   "low": 1,   "high": 1000, "max_attempts": 10},
}

def play_game(low, high, max_attempts):
    
    secret = random.randint(low, high)
    attempts = 0

    print(f"\nI'm thinking of a number between {low} and {high}.")
    
    
    if max_attempts is None:
        print("You have unlimited attempts.")
    else:
        print(f"You have {max_attempts} attempts.")
        

    while True:
        
        user_input = input("Enter your guess: ").strip()
        
        if user_input == "":
            print("You entered nothing. Please type a number.")
            continue

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if not (low <= guess <= high):
            print(f"Out of range. Enter a number between {low} and {high}.")
            continue

        attempts += 1

        if max_attempts is not None:
            attempts_left = max_attempts - attempts
            print(f"Attempts left: {attempts_left}")

        if guess == secret:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
        elif guess < secret:
            print("Too low.")
        else:
            print("Too high.")

        if (max_attempts is not None) and (attempts >= max_attempts):
            print(f"You've used all attempts. The number was {secret}.")
            break

def main_menu():
    while True:
        print("\n--- Number Guessing Game ---")
        print("1. Play")
        print("2. Exit")

        choice = input("Choose an option (1 or 2): ").strip()

        if choice == "1":
            print("\nSelect difficulty:")
            for key, info in DIFFICULTIES.items():
                print(f"{key}. {info['name']} (range {info['low']}–{info['high']}, attempts: {info['max_attempts']})")

            diff_choice = input("Choose difficulty (1/2/3): ").strip()
            if diff_choice in DIFFICULTIES:
                info = DIFFICULTIES[diff_choice]
                play_game(info["low"], info["high"], info["max_attempts"])
            else:
                print("Invalid difficulty choice.")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main_menu()
