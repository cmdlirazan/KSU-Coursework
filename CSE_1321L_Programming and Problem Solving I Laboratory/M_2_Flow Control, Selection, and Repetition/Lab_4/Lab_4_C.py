#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 4C

side_1 = int(input("Enter the first side of the triangle: "))
side_2 = int(input("Enter the second side of the triangle: "))
side_3 = int(input("Enter the third side of the triangle: "))

if side_1 > 0 and side_2 > 0 and side_3 > 0:
    if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
        if side_1 == side_2 == side_3:
            print("The triangle is an equilateral triangle.")
        elif side_1 == side_2  or side_1 == side_3 or side_2 == side_3:
            print("The triangle is an isosceles triangle.")
        else:
            print("The triangle is a scalene triangle.")
    else:
        print("The sides do not form a valid triangle.")
else:
    print("Invalid input. All sides must be greater than 0.")