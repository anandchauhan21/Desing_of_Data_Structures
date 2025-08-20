import os
import json
from datetime import datetime

# Structure-like data: using dictionary for each transaction
transactions = []  # This acts like an "array of structures"
DATA_FILE = os.path.join("data", "transactions.txt")


# ------------------------------
# Core Functions
# ------------------------------
def add_transaction():
    date_str = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Income/Expense): ").capitalize()
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    transaction = {
        "date": date_str,
        "category": category,
        "description": description,
        "amount": amount
    }
    transactions.append(transaction)
    print("✅ Transaction added!")


def view_transactions():
    if not transactions:
        print("⚠ No transactions recorded.")
        return
    print("\n--- Transaction List ---")
    for t in transactions:
        print(f"{t['date']} | {t['category']} | {t['description']} | ${t['amount']:.2f}")


def search_transactions():
    keyword = input("Enter keyword to search: ").lower()
    results = [t for t in transactions if keyword in t['description'].lower()]
    if results:
        print("\n--- Search Results ---")
        for t in results:
            print(f"{t['date']} | {t['category']} | {t['description']} | ${t['amount']:.2f}")
    else:
        print("⚠ No matching transactions found.")


def filter_expenses_over():
    threshold = float(input("Show expenses over: $"))
    results = [t for t in transactions if t['category'] == "Expense" and t['amount'] > threshold]
    if results:
        print(f"\n--- Expenses over ${threshold} ---")
        for t in results:
            print(f"{t['date']} | {t['description']} | ${t['amount']:.2f}")
    else:
        print("⚠ No expenses found above that amount.")


def sort_transactions():
    transactions.sort(key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d"))
    print("✅ Transactions sorted by date.")


# ------------------------------
# File Handling
# ------------------------------
def save_data():
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f)
    print("💾 Data saved successfully!")


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            loaded = json.load(f)
            transactions.extend(loaded)
        print("📂 Data loaded successfully!")


# ------------------------------
# ASCII Graph
# ------------------------------
def monthly_spending_chart():
    spending = {}
    for t in transactions:
        if t['category'] == "Expense":
            month = t['date'][:7]  # YYYY-MM
            spending[month] = spending.get(month, 0) + t['amount']

    if not spending:
        print("⚠ No expenses to display.")
        return

    print("\n--- Monthly Spending Chart ---")
    for month, total in spending.items():
        bar = "#" * int(total // 10)  # Scale: $10 = 1 #
        print(f"{month}: {bar} (${total:.2f})")


# ------------------------------
# Main Menu
# ------------------------------
def main():
    load_data()
    while True:
        print("\n📌 Personal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Search Transactions")
        print("4. Filter Expenses Over Amount")
        print("5. Sort Transactions by Date")
        print("6. Monthly Spending Chart")
        print("7. Save & Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            search_transactions()
        elif choice == "4":
            filter_expenses_over()
        elif choice == "5":
            sort_transactions()
        elif choice == "6":
            monthly_spending_chart()
        elif choice == "7":
            save_data()
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid choice, try again.")


if __name__ == "__main__":
    main()
