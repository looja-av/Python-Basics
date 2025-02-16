import random

def number_guessing_name():
    print("Welcome to the Number guessing game!")
    print("I'm thinking of a number between 1 and 100")

    secret_number=random.randint(1,100)
    attempts=0

    while True:
        try:
            guess=int(input("Enter your guess:"))
            attempts +=1

            if guess < secret_number:
                print("Too low!Try again")
            elif guess> secret_number:
                print("Too high.Please try agains!")
            else:
                print(f"Congrats! You guess it in {attempts} attempts ")
        except ValueError:
            print("INvalid inout! Please enter a number.")

number_guessing_name()

