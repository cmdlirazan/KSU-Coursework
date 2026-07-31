#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 8A

email_list = []

print("[Mailing List]")
print()

while True:
    print("1 - Add email")
    print("2 - Delete email")
    print("3 - List all emails")
    print("4 - Quit")
    selection = input("Make your selection: ")
    print()

    if selection == "1":
        email = input("Enter the email to be added: ")
        email_list.append(email)
        print("Email added to mailing list.")
        print()

    elif selection == "2":
        email = input("Enter the email to be removed: ")
        if email in email_list:
            email_list.remove(email)
            print(f"{email} has been removed from the mailing list.")
        else:
            print(f"No such email in mailing list: {email}")
        print()

    elif selection == "3":
        for e in email_list:
            print(e)
            print()

    elif selection == "4":
        print("Shutting down...")
        break
    else:
        print("Invalid selection. Please try again.")
        print()