#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 4C

from A4C_Functions import display_main_menu, deposit, withdraw, check_balance

def main():
    print("Welcome to the ATM!")
    name = input("Please enter your name: ")
    balance = float(input("Enter your initial balance: $"))

    while True:
        choice = display_main_menu()

        if choice == "1":
            balance = deposit(balance)
        elif choice == "2":
            balance = withdraw(balance)
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            print(f"Goodbye, {name}! Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please try again.")

main()