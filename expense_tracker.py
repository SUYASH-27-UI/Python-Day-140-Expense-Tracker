import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"


def add_expense():
    category = input("Enter category: ").strip()

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    description = input("Enter description: ").strip()

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writerow(
                ["Date", "Category", "Amount", "Description"]
            )

        writer.writerow([
            date.today(),
            category,
            amount,
            description
        ])

    print("Expense saved successfully!")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("No expenses recorded yet.")
        return

    for row in rows:
        print(" | ".join(row))


def show_total():
    total = 0

    if not os.path.exists(FILE_NAME):
        print("Total expenses: 0.00")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"Total expenses: ₹{total:.2f}")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Try again.")
