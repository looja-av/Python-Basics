import random

def guess_the_numm():

    print("Welcome to the guessing game")
    print("guess the number between 1-100")

    right_num= random.randint(1,100)
    attempts=0

    while True:
        try:
            guess=int(input("Enter your guess:"))
            attempts+=1

            if guess<right_num:
                print("Your guess is lower. try again")

            elif guess > right_num:
                print("your guess is lsightly ")

            else:
                print("you guessed it right in {attempts} attempts")
        except:
            print("You have enetered wrong input")

guess_the_numm()




