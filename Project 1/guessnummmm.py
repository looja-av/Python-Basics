import random

def guessnum():
    print("welcome")

    randomnumber=random.randint(1,20)
    attempts=0

    while True:
        try:
            guess=int(input("guess your number"))
            attempts+=1

            if randomnumber<guess:
                print("its lower")

            elif randomnumber>guess:
                print("its higheer")

            else:

                print("you have correct answer ")
            break 

        except ValueError:
            print("invalid input")

guessnum()