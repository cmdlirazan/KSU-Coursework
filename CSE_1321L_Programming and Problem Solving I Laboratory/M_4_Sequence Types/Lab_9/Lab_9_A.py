#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 9A

def allMath(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else None
    floor_division = num1 // num2 if num2 != 0 else None
    modulus = num1 % num2 if num2 != 0 else None
    power = num1 ** num2

    def format_number(n):
        return int(n) if isinstance(n, (int, float)) and n.is_integer() else n

    return tuple(format_number(n) if n is not None else None for n in
                 (addition, subtraction, multiplication, division, floor_division, modulus, power))

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

result = allMath(num1, num2)
print(f"Your resulting tuple is {result}")