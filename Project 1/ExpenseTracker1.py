import json

FILENAME= "expenses.json"

def load_expenses():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return{}

def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    category=input("Enter category (Food,Rent,Travel, etc.)")
    amount= float(input("Enter amount:"))
    description=input("Enter description:")

    if category in expenses:
        expenses[category].append({"amount": amount, "description":description})
    else:
        expenses[category]= [{"amount": amount, "description":description}]

    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("NO expenses founds!")
        return
    
    print("\n Expenses Summary:")
    for category, items in expenses.items():
        print(f"\n {category}")
        for entry in items:
            print(f" ${entry['amount']}- {entry['description']}")

def delete_expense(expenses):
    category = input("Enter category to delete:")
    if category in expenses:
        del expenses[category]
        save_expenses(expenses)
        print("Category deleted successfully!")
    else:
        print("Category not found!")

def main():
    expenses = load_expenses()

    while True:
        print("\n Expense Tracker Menu:")
        print("Add Expense")
        print("View Expenses")
        print("Delete Expense Category")
        print("Exit")

        choice= input("Choose an option")

        if choice =="1":
            add_expense(expenses)
        elif choice =="2":
            view_expenses(expenses)
        elif choice =="3":
            delete_expense(expenses)
        elif choice =="4":
            print("Existing.. have a great day!")
            break
        else:
            print('Invalid choice! Try again.')

if __name__=="__main__":
    main()
        





