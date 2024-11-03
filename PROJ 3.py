import json
import os
from datetime import datetime

# File to store expenses data
EXPENSE_FILE = 'expenses.json'

def load_expenses():
    """Load expenses from the JSON file."""
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    """Save expenses to the JSON file."""
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Prompt user to add a new expense."""
    try:
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")
        category = input("Enter the expense category (e.g., food, transportation, entertainment): ")
        
        # Create an expense entry
        expense = {
            "amount": amount,
            "description": description,
            "category": category,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        
        # Append expense to the list
        expenses.append(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

def view_expenses(expenses):
    """Display all recorded expenses."""
    if not expenses:
        print("No expenses recorded.")
        return
    
    for expense in expenses:
        print(f"{expense['date']}: ${expense['amount']:.2f} - {expense['description']} (Category: {expense['category']})")

def categorize_expenses(expenses):
    """Categorize and summarize expenses by category."""
    categories = {}
    for expense in expenses:
        category = expense['category']
        if category not in categories:
            categories[category] = 0
        categories[category] += expense['amount']
    
    print("\nCategory-wise Summary:")
    for category, total in categories.items():
        print(f"Category: {category}, Total Spent: ${total:.2f}")

def monthly_summary(expenses):
    """Provide a summary of expenses by month."""
    summaries = {}
    for expense in expenses:
        month = expense['date'][:7]  # Extract year-month
        if month not in summaries:
            summaries[month] = 0
        summaries[month] += expense['amount']
    
    print("\nMonthly Summary:")
    for month, total in summaries.items():
        print(f"Month: {month}, Total Spent: ${total:.2f}")

def main():
    """Main function to run the Expense Tracker CLI."""
    expenses = load_expenses()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Categorize Expenses")
        print("4. Monthly Summary")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            categorize_expenses(expenses)
        elif choice == '4':
            monthly_summary(expenses)
        elif choice == '5':
            print("Exiting the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
