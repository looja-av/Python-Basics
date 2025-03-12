import random

def guessthenum():
    print("Welcome")
    print("Lets start")

    randomnum=random.randint(1,50)
    attempts=0

    while True:
        try:
            yournumber=int(input("Enter your guess"))
            attempts+=1

            if yournumber<randomnum:
                print("Not emough")

            elif yournumber>randomnum:
                print("Too emough")

            else:
                print(f"You did it in {attempts} attempts")

        except:
            print("Invalid")
guessthenum()

