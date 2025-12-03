
# applying some input validation while entering number 
import random 

LOW = 1
HIGH = 100
secret_number = random.randint(LOW, HIGH)
attempts = 0

print(f"I am thinking of a number between {LOW} to {HIGH}")

# Start an indefinite loop that runs until we break out (i.e., until the player guesses correctly).
while True:
    user_input = input('Guess a number : ').strip() # we are not directly taking intiger input because we are using strip() 
    
    # Check if the user submitted nothing (empty after stripping). If so, warn and reprompt.
    if user_input == "" or user_input == " ":
        print("You have not enter anything , enter a number ")
        continue
    try: 
        guess = int(user_input) #Convert the validated (non-empty) string to an integer and assign it to guess.
    except ValueError: #Catch conversion failures (ValueError) and run the follow-up block instead of crashing.
         print("Invalide input , please enter an intiger eg. 45 ")
         continue
        
    if not (LOW <= guess <= HIGH):
        print(f"You had enetered a number that out of reach\nPlease guess a number between {LOW} to {HIGH} ")    
        continue 
    
    attempts = attempts+1
    
    if guess == secret_number :
        print(f"Congrats, you estimate it right in {attempts} attempts,\nthe number was {secret_number}")
        break 
    elif guess < secret_number :
        print("Nah,guess bit more higher")
    elif guess > secret_number:
        print("Nah, guess bit more lower")
    