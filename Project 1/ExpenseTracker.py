import json

# File to store expenses
FILENAME = "expenses.json"

# Load expenses from file
def load_expenses():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save expenses to file
def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    category = input("Enter category (Food, Rent, Travel, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    if category in expenses:
        expenses[category].append({"amount": amount, "description": description})
    else:
        expenses[category] = [{"amount": amount, "description": description}]

    save_expenses(expenses)
    print("✅ Expense added successfully!")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("❌ No expenses found!")
        return

    print("\n📊 Expense Summary:")
    for category, items in expenses.items():
        print(f"\n🔹 {category}:")
        for entry in items:
            print(f"   💰 ${entry['amount']} - {entry['description']}")

# Delete an expense category
def delete_expense(expenses):
    category = input("Enter category to delete: ")
    if category in expenses:
        del expenses[category]
        save_expenses(expenses)
        print("✅ Category deleted successfully!")
    else:
        print("❌ Category not found!")

# Main program loop
def main():
    expenses = load_expenses()

    while True:
        print("\n🔹 Expense Tracker Menu:")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Delete Expense Category")
        print("4️⃣ Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            print("🚀 Exiting... Have a great day!")
            break
        else:
            print("⚠️ Invalid choice! Try again.")

# Run the program
if __name__ == "__main__":
    main()
