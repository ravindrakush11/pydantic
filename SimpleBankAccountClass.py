class BankAccount:
    def __init__(self, name: str, balance: float = 0.0):
        assert isinstance(name, str), "Name must be a string"
        assert isinstance(balance, (int, float)), "Balance must be a number"
        self.name = name
        self.balance = float(balance)

    def deposit(self, amount):
        assert isinstance(amount, (int, float)), "Deposit amount must be numeric"
        assert amount > 0, "Deposit must be positive"
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        assert isinstance(amount, (int, float)), "Withdrawal amount must be numeric"
        assert amount > 0, "Withdrawal must be positive"
        assert amount <= self.balance, "Insufficient funds"
        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"{self.name}'s Account Balance: ₹{self.balance:.2f}"


# Create account
account = BankAccount("Ravindra", 1000)

# Valid transactions
print(account.deposit(500))     # ✅ 1500.0
print(account.withdraw(200))    # ✅ 1300.0
print(account)                  # ✅ Ravindra's Account Balance: ₹1300.00

# Invalid types
account.deposit("five hundred")  # ❌ AssertionError



# Experimnet with Type Errors

# BankAccount(123, 100)           # ❌ Name must be string
# BankAccount("Ravi", "100")      # ❌ Balance must be numeric
# account.withdraw(-10)           # ❌ Withdrawal must be positive
