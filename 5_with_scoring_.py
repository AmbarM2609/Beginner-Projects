import random
import json
import os
from datetime import datetime

HIGHSCORE_FILE = "Number_Game\approaches\highscores.json"

DIFFICULTIES = {
    "1": {"name": "Easy",   "low": 1,   "high": 20,   "max_attempts": 10},
    "2": {"name": "Medium", "low": 1,   "high": 100,  "max_attempts": 7},
    "3": {"name": "Hard",   "low": 1,   "high": 1000, "max_attempts": 10},
}

import os
import json # Assumed imports needed for the function to run

def load_highscores():
    """
    Loads highscores from the disk file (HIGHSCORE_FILE).
    Returns:
        dict: The loaded highscore data, or an empty dictionary if the file
              is missing, unreadable, or contains invalid data.
    """
    try:
        # 1. Open and load the JSON file
        with open(HIGHSCORE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            
            # 2. Validate the data type
            if isinstance(data, dict):
                return data
            
            # 3. If data is not a dict (e.g., a list or string), treat as invalid
            return {} 
            
    except FileNotFoundError:
        # File doesn't exist. This is the cleanest way to handle the "missing file" case.
        return {}
        
    except (json.JSONDecodeError, OSError) as e:
        # Handles corrupt JSON data or other file/OS-related read errors.
        # print(f"Error loading highscores: {e}") # Optional: log the error
        return {}

def save_highscores(data):
    """Save highscores dict to disk."""
    try:
        with open(HIGHSCORE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except OSError:
        print("Warning: could not save highscores.")

def compute_score(attempts, max_attempts, low, high):
    """Compute score: higher is better. Always return non-negative integer."""
    if max_attempts is not None:
        raw = max_attempts - attempts + 1
    else:
        raw = (high - low + 1) - attempts + 1
    return max(0, int(raw))

def update_highscore_for(difficulty_key, attempts, max_attempts, low, high):
    """Update highscore for a difficulty if this run is better. Return True if updated."""
    data = load_highscores()
    score = compute_score(attempts, max_attempts, low, high)
    now = datetime.utcnow().isoformat() + "Z"
    current = data.get(difficulty_key)

    better = False
    if current is None:
        better = True
    else:
        # Prefer higher score; on tie prefer fewer attempts; else keep existing
        if score > current.get("score", -1):
            better = True
        elif score == current.get("score", -1) and attempts < current.get("best_attempts", 999999):
            better = True

    if better:
        data[difficulty_key] = {
            "best_attempts": attempts,
            "score": score,
            "when": now
        }
        save_highscores(data)
        return True
    return False

def show_highscores():
    """Print current highscores in a readable form."""
    data = load_highscores()
    if not data:
        print("No highscores yet.")
        return
    print("\n--- Highscores ---")
    for key, info in DIFFICULTIES.items():
        record = data.get(key)
        name = info["name"]
        if record:
            print(f"{name}: {record['score']} points (best attempts: {record['best_attempts']}) on {record['when']}")
        else:
            print(f"{name}: — no record —")

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
            return True, attempts
        elif guess < secret:
            print("Too low.")
        else:
            print("Too high.")

        if (max_attempts is not None) and (attempts >= max_attempts):
            print(f"You've used all attempts. The number was {secret}.")
            return False, attempts

def main_menu():
    while True:
        print("\n--- Number Guessing Game ---")
        print("1. Play")
        print("2. Highscores")
        print("3. Exit")

        choice = input("Choose an option (1, 2 or 3): ").strip()

        if choice == "1":
            print("\nSelect difficulty:")
            for key, info in DIFFICULTIES.items():
                print(f"{key}. {info['name']} (range {info['low']}–{info['high']}, attempts: {info['max_attempts']})")

            diff_choice = input("Choose difficulty (1/2/3): ").strip()
            if diff_choice in DIFFICULTIES:
                info = DIFFICULTIES[diff_choice]
                won, attempts = play_game(info["low"], info["high"], info["max_attempts"])
                if won:
                    updated = update_highscore_for(diff_choice, attempts, info["max_attempts"], info["low"], info["high"])
                    if updated:
                        print("New highscore! Well done.")
                    else:
                        print("Good job — you didn't beat the highscore this time.")
            else:
                print("Invalid difficulty choice.")
        elif choice == "2":
            show_highscores()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2 or 3.")

if __name__ == "__main__":
    main_menu()
