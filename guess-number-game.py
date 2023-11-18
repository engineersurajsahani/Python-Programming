import random

def generate_random_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            user_guess = int(input("Enter your guess (between 1 and 100): "))
            if 1 <= user_guess <= 100:
                return user_guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def evaluate_guess(user_guess, target_number):
    if user_guess == target_number:
        return "Congratulations! You guessed the correct number."
    elif user_guess < target_number:
        return "Too low. Try again."
    else:
        return "Too high. Try again."

def main():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Try to guess it.")

    target_number = generate_random_number()

    while True:
        user_guess = get_user_guess()
        
        result = evaluate_guess(user_guess, target_number)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"The correct number was {target_number}. Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
