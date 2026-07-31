#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 6A

def multiplication(a, b):
    result = 0
    for _ in range(abs(b)):
        result+= abs(a)
    if (a < 0 < b) or (a > 0 > b):
        result = -result
    return result

def exponentiation(base, exponent):
    result = 1
    for _ in range(exponent):
        temp = 0
        for _ in range(result):
            temp += base
        result = temp
    return result

def main():
    while True:
        print("Multiplication and Exponent Calculator")
        print("Choose option 1 for Multiplication")
        print("Choose option 2 for Exponentiation")
        print("Choose option 3 to Exit")
        menu = int(input(""))
        print()

        if menu == 1:
            a = int(input("Enter an operand: "))
            b = int(input("Enter the other operand: "))
            print(f"{a} x {b} = {multiplication(a, b)}")

        elif menu == 2:
            base = int(input("Enter the base: "))
            exponent = int(input("Enter the exponent: "))
            if exponent < 0:
                print("Invalid Choice")
            else:
                print(f"{base}^({exponent}) = {exponentiation(base, exponent)}")

        elif menu == 3:
            print("Closing the Calculator...")
            break

        else:
            print("Invalid Choice")

        print()

if __name__ == "__main__":
    main()