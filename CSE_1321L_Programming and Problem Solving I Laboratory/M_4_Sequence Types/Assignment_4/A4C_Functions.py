#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: A4C Functions

def display_main_menu():
    print("ATM Main Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Please choose an option (1-4): ")
    return choice

def deposit(balance):
    amount = float(input("Enter the amount to deposit: $"))
    balance += amount
    print(f"Deposited ${amount}. New balance: ${balance}")
    return balance

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: $"))
    if amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"Withdrew ${amount}. New balance: ${balance}")
    return balance

def check_balance(balance):
    print(f"Your current balance is: ${balance}")