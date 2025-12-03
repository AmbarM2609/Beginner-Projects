# reply and simple menu
import random 

def start_playing_game():
    LOW = 1
    HIGH = 100
    secret_number = random.randint(LOW, HIGH)
    attempts = 0 
    
    print(f"I had picked one number between {LOW} to {HIGH}")
    
    while True: # Start an indefinite loop that runs until we break out (i.e., until the player guesses correctly).
        
        user_input = input(" Guess the number : ").strip()
        
        if user_input == "":
            print("please enter something")
            continue
        try:
            user_input_number = int(user_input)
        except ValueError:
            print(" Enter a valid number please.")
            continue
        if user_input_number not in range (LOW, HIGH+1 ):
            print(f"You had enetered a number that out of reach\nPlease guess a number between {LOW} to {HIGH} ")
            continue 
        
        attempts = attempts + 1 # if player give the proper input then next iteration will carriedd out 
        
        if user_input_number == secret_number :
            print(f"Congrats, you estimate it right in {attempts} attempts,\nthe number was {secret_number}")
            break 
        elif user_input_number < secret_number :
            print("Nah,guess bit more higher")
        elif user_input_number > secret_number:
            print("Nah, guess bit more lower")
            
            
def game_menu():
    
    while True:
        print('...Lets start the game...')
        print(" 1. PLAY/n 2.EXIT/n")
        
        choice = input("Select an option from above:").strip()
        
        if choice == "1":
            start_playing_game()
        elif choice == "2":
            print("Have a good day")
            break
        else:
            print("Please select choice between 1 and 2")
            continue
        
game_menu()