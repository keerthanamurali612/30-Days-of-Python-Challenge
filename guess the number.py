import random

# Generate a random number between 1 and 9
secret_number = random.randint(1, 9)

# Initialize a variable to keep track of the number of guesses
attempts = 0

# Main game loop
while True:
    try:
        # Get a guess from the user
        guess = int(input("Guess the number between 1 and 9: "))
        
        # Increment the number of attempts
        attempts += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")
    except ValueError:
        print("Please enter a valid number between 1 and 9.")

# End of the game

