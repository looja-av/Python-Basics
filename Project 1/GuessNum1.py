import random

def Guess_theNum():
    print("Welcome to the guessing game")
    print("Put your guess down below")

    secretNumber=random.randint(1,50)
    attempts=0

    while True:
        try:
            guess=int(input("what is your guess"))
            attempts+=1

            if guess<secretNumber:
                print("Too low.try again")
            elif guess > secretNumber:
                print("too much.try again")
            else:
                print("You have guess it in {attempts} attempts")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

Guess_theNum()
            
            

            
   
    
      
    
    

