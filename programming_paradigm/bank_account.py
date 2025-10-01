class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the bank account with an optional starting balance."""
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw an amount from the account if funds are sufficient.
        Returns True if successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
