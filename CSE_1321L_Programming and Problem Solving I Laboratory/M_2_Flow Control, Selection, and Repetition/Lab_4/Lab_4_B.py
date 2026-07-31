#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 4B

print("Welcome!")
num = float(input("Please input a number: "))
print()
print("What would you like to do with this number:")
print("0) Get the additive inverse of the number")
print("1) Get the reciprocal of the number")
print("2) Square the number")
print("3) Cube the number")
print("4) Exit the program")
option = int(input(""))
print()

match option:
    case 0:
        additive_inverse = 0 - num
        print("The additive inverse of " + str(num) + " is " + str(additive_inverse))
    case 1:
        if num == 0:
            print("Cannot divide by 0!")
        else:
            reciprocal = 1/num
            reciprocal_rounded = round(reciprocal, 3)
            print("The reciprocal of " + str(num) + " is " + str(reciprocal_rounded))
    case 2:
        square = num ** 2
        print("The square of " + str(num) + " is " + str(square))
    case 3:
        cube = num ** 3
        print("The cube of " + str(num) + " is " + str(cube))
    case 4:
        print("Thank you, goodbye!")
    case _:
       print("Invalid option!")