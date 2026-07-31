#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 9B

def main():
    users = {}

    while True:
        print("Choose an option")
        print(" 1 - Login")
        print(" 2 - Register")
        print(" E - Exit")
        print()
        option = input().strip()
        print()

        if option == "1":
            print("[Login]")
            print(" Username:")
            username = input().strip()
            print(" Password:")
            password = input().strip()

            if users.get(username) == password:
                print("Success!")
                print()
                while True:
                    print("Choose an option")
                    print(" 3 - Change Password")
                    print(" 4 - Logout")
                    print(" E - Exit")
                    print()
                    sub_option = input().strip()
                    print()

                    if sub_option == "3":
                        print("[Changing password]")
                        print(" Password:")
                        new_password = input().strip()
                        users[username] = new_password
                        print()
                    elif sub_option == "4":
                        print("Logging Out...")
                        print()
                        break
                    elif sub_option == "E":
                        print("Terminating...")
                        return
            else:
                print("Incorrect username/password!")
                print()

        elif option == "2":
            print("[Register]")
            print(" Username:")
            username = input().strip()
            print(" Password:")
            password = input().strip()
            users[username] = password
            print("User successfully added!")
            print()

        elif option == "E":
            print("Terminating...")
            break

main()