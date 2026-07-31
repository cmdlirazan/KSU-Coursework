#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 7A

def isvalid(width, height):
    return (width + height) > 30

def area(width, height):
    return width * height

def perimeter(width, height):
    return 2 * (width + height)

def main():
    repeat = True
    while repeat:
        try:
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if isvalid(width, height):
            print("This is a valid rectangle.")
            print("The area is:", area(width, height))
            print("The perimeter is:", perimeter(width, height))
        else:
            print("This is an invalid rectangle.")

        again = input("\nDo you want to enter another width and height (Y/N)?: ")
        if again == 'N':
            repeat = False
            print("\nProgram Ends")

main()