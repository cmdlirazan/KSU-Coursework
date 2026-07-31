#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 2C

def main():
    print("Welcome to the RPG Game!")
    print("Choose your class: 1. Warrior 2. Mage 3. Healer")

    class_choice = input("Enter the number of your class (1/2/3): ")

    match class_choice:
        case "1":
            print("You have chosen Warrior! You are strong and brave.")
            print("What would you like to do? 1. Attack your sword 2. Defend with your shield")
            action = input("Choose your action (1/2): ")
            match action:
                case "1":
                    print("You swing your sword and defeat the enemy!")
                case "2":
                    print("You raise your shield and block the enemy's attack!")
                case _:
                    print("Invalid action choice. The game ends.")

        case "2":
            print("You have chosen Mage! You wield powerful magic.")
            print("What would you like to do? 1. Cast a fireball 2. Cast a healing spell")
            action = input("Choose your action (1/2): ")
            match action:
                case "1":
                    print("You cast a fireball and scorch the enemy!")
                case "2":
                    print("You cast a healing spell and restore your energy.")
                case _:
                    print("Invalid action choice. The game ends.")

        case "3":
            print("You have chosen Healer! You are kind and supportive.")
            print("What would you like to do? 1. Heal your ally 2. Attack with your staff")
            action = input("Choose your action (1/2): ")
            match action:
                case "1":
                    print("You heal your ally and boost their morale!")
                case "2":
                    print("You swing your staff and knock out the enemy!")
                case _:
                    print("Invalid action choice. The game ends.")

        case _:
            print("Invalid class choice. The game ends.")

    print("Thank you for playing!")

if __name__ == "__main__":
    main()