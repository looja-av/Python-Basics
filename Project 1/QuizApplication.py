<<<<<<< HEAD
import json
import random
import time

FILENAME="quiz_questions.json"

def load_questions():
    try:
        with open(FILENAME,"r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return[] 

def save_questions(questions):
    with open(FILENAME,"w") as file:
        json.dump(questions, file, indent=4)

def add_question(questions):
    question_text=input("Enter the question")
    options=[]

    for i in range(4):
        option=input(f"Enter option{i+1}")
        options.append(option)

    correct_option=int(input("Enter the correct option number(1-4):")) -1

    questions.append({
        "question":question_text,
        "options":options,
        "correct":correct_option
    })

    save_questions(questions)
    print("Questions added succesfuly")

def play_quiz(questions):
    if not questions:
        print("No questions available! add some quesitions first")
        return
    
    random.shuffle(questions)
    score=0

    for question in questions:
        print("\n*", question["question"])
        for i, option in enumerate(question["options"],1):
            print("f{i}. {option}")

        start_time=time.time()
        answer= input("Your answer (1-4):")

        elapsed_time= time.time() - start_time
        if elapsed_time > 10:
            print("Time;s up! Moving to the next question")
            continue

        if answer.isdigit() and  1<=int(answer) <=4:
            if int(answer) -1==question["correct"]:
                print("Correct!")
                score +=1
            else:
                print(f"Wrong! The correct answewr was {question['options'][questions['correct']]} ")
        else:
            print("⚠️ Invalid input! Moving to the next question.")

        print(f"\n🎉 You scored {score}/{len(questions)}!")

def view_questions(questions):
    if not questions:
        print(" NO quesitons available!")
        return
    
    print("\n Quiz Questions:")
    for i, question in enumerate(question, 1):
        print(f"{i}. {question['question']} (Correct: {question['options'][question['correct']]})")

def main():
    questions = load_questions()

    while True:
        print("\n* Quiz Application Menu:")
        print("1. Add a Question")
        print("2. Play the Quiz")
        print("3. View Questions")
        print("4. EXit")

        choice= input("Choose an option")

        if choice =="1":
            add_question(questions)
        elif choice =="2":
            play_quiz(questions)

        elif choice=="3":
            view_questions(questions)
        elif choice=="4":
            print("Existing.. Have a great day!")
            break
        else:
            print("INvalid choice! Try again")

if __name__=="__main__":
    main()


=======
import json
import random
import time

FILENAME="quiz_questions.json"

def load_questions():
    try:
        with open(FILENAME,"r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return[] 

def save_questions(questions):
    with open(FILENAME,"w") as file:
        json.dump(questions, file, indent=4)

def add_question(questions):
    question_text=input("Enter the question")
    options=[]

    for i in range(4):
        option=input(f"Enter option{i+1}")
        options.append(option)

    correct_option=int(input("Enter the correct option number(1-4):")) -1

    questions.append({
        "question":question_text,
        "options":options,
        "correct":correct_option
    })

    save_questions(questions)
    print("Questions added succesfuly")

def play_quiz(questions):
    if not questions:
        print("No questions available! add some quesitions first")
        return
    
    random.shuffle(questions)
    score=0

    for question in questions:
        print("\n*", question["question"])
        for i, option in enumerate(question["options"],1):
            print("f{i}. {option}")

        start_time=time.time()
        answer= input("Your answer (1-4):")

        elapsed_time= time.time() - start_time
        if elapsed_time > 10:
            print("Time;s up! Moving to the next question")
            continue

        if answer.isdigit() and  1<=int(answer) <=4:
            if int(answer) -1==question["correct"]:
                print("Correct!")
                score +=1
            else:
                print(f"Wrong! The correct answewr was {question['options'][questions['correct']]} ")
        else:
            print("⚠️ Invalid input! Moving to the next question.")

        print(f"\n🎉 You scored {score}/{len(questions)}!")

def view_questions(questions):
    if not questions:
        print(" NO quesitons available!")
        return
    
    print("\n Quiz Questions:")
    for i, question in enumerate(question, 1):
        print(f"{i}. {question['question']} (Correct: {question['options'][question['correct']]})")

def main():
    questions = load_questions()

    while True:
        print("\n* Quiz Application Menu:")
        print("1. Add a Question")
        print("2. Play the Quiz")
        print("3. View Questions")
        print("4. EXit")

        choice= input("Choose an option")

        if choice =="1":
            add_question(questions)
        elif choice =="2":
            play_quiz(questions)

        elif choice=="3":
            view_questions(questions)
        elif choice=="4":
            print("Existing.. Have a great day!")
            break
        else:
            print("INvalid choice! Try again")

if __name__=="__main__":
    main()


>>>>>>> a8c9fe4c200c692df3775823284ee4eed2626cc3
        