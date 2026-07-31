#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 10A

class Chair:
    def __init__(self, numOfLegs=4, rolling=False, material="plastic"):
        self.numOfLegs = numOfLegs
        self.rolling = rolling
        self.material = material

    def display_info(self):
        rolling_status = "rolling" if self.rolling else "not rolling"
        print(f"Your chair has {self.numOfLegs} legs, is {rolling_status}, and is made of {self.material}.")

print("You are about to create a chair.")
numOfLegs = int(input("How many legs does your chair have: "))
rolling_input = input("Is your chair rolling (true/false): ").strip().lower()
rolling = rolling_input == "true"
material = input("What is your chair made of: ").strip()

chair = Chair(numOfLegs, rolling, material)

chair.display_info()

print("This program is going to change that.")

chair.numOfLegs = 4
chair.rolling = False
chair.material = "wood"

chair.display_info()