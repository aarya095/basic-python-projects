import random

def number_guessing_game():

    print("Welcome to number guessing game!")
    print("I am thinking of a number between 1 and 50.")
    print("You have 10 chances to guess it!")

    target_number = random.randint(1,50)
    attempts_left = 10

    while attempts_left >0:
        try:

            guess = int(input("Enter you guess: "))

            if guess < target_number:
                print("Too low! Try again!")
            elif guess > target_number:
                print("Too high! try again!")
            else:
                print(f"Congratulations! you guessed the number {target_number} correctly!")
                break

            attempts_left -= 1
            print(f"Attempts remaining: {attempts_left}")

        except ValueError:
            print("please enter a valid number.")

    if attempts_left == 0:
        print(f"Game Over! The number was {target_number}. Better luck nest time!")

if __name__=="__main__":
    number_guessing_game()