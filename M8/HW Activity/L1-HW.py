import random
def guess_the_number_game():

    secret_number = random.randint(1, 100)
    guess_history = []  
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            user_guess_str = input("Enter your guess: ")
            user_guess = int(user_guess_str)  
            guess_history.append(user_guess) 

            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                print("Your guesses were:", guess_history) 
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


guess_the_number_game() 
