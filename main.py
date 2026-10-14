
import random

def play_game():
    print("Welcome to Number Guessing Game!")
    print("Guess a number between 1 and 25.")
    print("You have 5 attempts.\n")

    number = random.randint(1, 25)
    attempts = 5

    for i in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {i}: Enter your guess: "))

            if guess < 1 or guess > 25:
                print("Enter a number between 1 and 25.")
                continue

            if guess == number:
                print("Congratulations! Correct guess!")
                print("You guessed it in", i, "attempts.")
                break
            elif guess < number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

        except ValueError:
            print("Invalid input! Enter a valid integer.")

    else:
        print("\nGame Over!")
        print("The correct number was:", number)

def main():
    while True:
        play_game()

        choice = input("\nPlay again? (yes/no): ")

        if choice.lower() not in ["yes", "y"]:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
