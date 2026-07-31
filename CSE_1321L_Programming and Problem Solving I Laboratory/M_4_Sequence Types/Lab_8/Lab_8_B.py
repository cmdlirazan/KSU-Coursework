#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 8B

friend_list = []

print("[Friend List]")
print()

while True:
    print("1 - Add friend")
    print("2 - List friends")
    print("3 - Quit")
    selection = input("Make your selection: ")
    print()

    if selection == "1":
        name = input("Enter your friend's name: ")
        age = input("Enter your friend's age: ")
        friend = (name, age)
        friend_list.append(friend)
        print("Friend added")
        print()

    elif selection == "2":
        for friend in friend_list:
            print(f"Name: {friend[0]}, Age: {friend[1]}")
        print()

    elif selection == "3":
        print("Shutting down...")
        break
    else:
        print("Invalid selection. Please try again.")
        print()