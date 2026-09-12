import json


class Transaction:
    def __init__(self, transaction_type, amount, category, description, month):
        self.transaction_type = transaction_type
        self.amount = amount
        self.category = category
        self.description = description
        self.month = month


class FinanceTracker:
    def __init__(self):
        self.transactions = []

    # Add income
    def add_income(self):
        amount = float(input("Enter income amount: £"))
        category = input("Enter category (Salary, Gift, Other): ")
        description = input("Enter description: ")
        month = input("Enter month: ")

        new_transaction = Transaction(
            "Income",
            amount,
            category,
            description,
            month
        )

        self.transactions.append(new_transaction)

        print("Income added successfully.")

    # Add expense
    def add_expense(self):
        amount = float(input("Enter expense amount: £"))
        category = input("Enter category (Food, Travel, Shopping, Bills, Other): ")
        description = input("Enter description: ")
        month = input("Enter month: ")

        new_transaction = Transaction(
            "Expense",
            amount,
            category,
            description,
            month
        )

        self.transactions.append(new_transaction)

        print("Expense added successfully.")

    # Show all transactions
    def show_transactions(self):
        if len(self.transactions) == 0:
            print("No transactions found.")
        else:
            print("\n--- All Transactions ---")

            for transaction in self.transactions:
                print("--------------------")
                print("Type:", transaction.transaction_type)
                print("Amount: £", transaction.amount)
                print("Category:", transaction.category)
                print("Description:", transaction.description)
                print("Month:", transaction.month)

    # Monthly summary
    def monthly_summary(self):
        month = input("Enter month: ")

        total_income = 0
        total_expenses = 0

        for transaction in self.transactions:

            if transaction.month.lower() == month.lower():

                if transaction.transaction_type == "Income":
                    total_income = total_income + transaction.amount

                elif transaction.transaction_type == "Expense":
                    total_expenses = total_expenses + transaction.amount

        balance = total_income - total_expenses

        print("\n---", month, "Summary ---")
        print("Total Income: £", total_income)
        print("Total Expenses: £", total_expenses)
        print("Balance: £", balance)

    # Category summary
    def category_summary(self):
        category = input("Enter category: ")

        total = 0

        for transaction in self.transactions:

            if transaction.transaction_type == "Expense":

                if transaction.category.lower() == category.lower():
                    total = total + transaction.amount

        print("Total spent on", category, ": £", total)

    # Save transactions to JSON file
    def save_file(self):
        data = []

        for transaction in self.transactions:

            transaction_data = {
                "type": transaction.transaction_type,
                "amount": transaction.amount,
                "category": transaction.category,
                "description": transaction.description,
                "month": transaction.month
            }

            data.append(transaction_data)

        file = open("finance_data.json", "w")

        json.dump(data, file, indent=4)

        file.close()

        print("Transactions saved successfully.")

    # Load transactions from JSON file
    def load_file(self):
        try:
            file = open("finance_data.json", "r")

            data = json.load(file)

            file.close()

            self.transactions = []

            for item in data:

                transaction = Transaction(
                    item["type"],
                    item["amount"],
                    item["category"],
                    item["description"],
                    item["month"]
                )

                self.transactions.append(transaction)

            print("Transactions loaded successfully.")

        except FileNotFoundError:
            print("No saved finance file found.")


# Main program

tracker = FinanceTracker()

tracker.load_file()

choice = ""

while choice != "6":

    print("\n===== PERSONAL FINANCE TRACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Transactions")
    print("4. Monthly Summary")
    print("5. Category Summary")
    print("6. Save and Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        tracker.add_income()

    elif choice == "2":
        tracker.add_expense()

    elif choice == "3":
        tracker.show_transactions()

    elif choice == "4":
        tracker.monthly_summary()

    elif choice == "5":
        tracker.category_summary()

    elif choice == "6":
        tracker.save_file()
        print("Goodbye!")

    else:
        print("Invalid option. Please choose 1-6.")
