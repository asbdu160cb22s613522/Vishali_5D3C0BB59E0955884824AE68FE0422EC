class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      return f"Deposited ${amount}. New balance is ${self.__account_balance}."
    else:
      return "Invalid deposit amount. Amount must be greater than zero."

  def withdraw(self, amount):
    if 0 < amount <= self.__account_balance:
      self.__account_balance -= amount
      return f"Withdrew ${amount}. New balance is ${self.__account_balance}."
    else:
      return "Insufficient funds or invalid withdrawal amount."

  def display_balance(self):
    return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}"


# Testing the BankAccount class
if __name__ == "__main__":
  # Creating an instance of BankAccount
  my_account = BankAccount("123456789", "Vishali", 1000.0)

  # Testing deposit and withdrawal
  print(my_account.display_balance())  # Display initial balance
  print(my_account.deposit(500))  # Deposit $500
  print(my_account.withdraw(200))  # Withdraw $200
  print(my_account.withdraw(
      1500))  # Attempt to withdraw $1500 (insufficient funds)
