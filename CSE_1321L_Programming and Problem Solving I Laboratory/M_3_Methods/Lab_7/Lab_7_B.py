#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 7B

from MyMath import my_max, my_min, my_avg

def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    max = my_max(num1, num2)
    min = my_min(num1, num2)
    avg = my_avg(num1, num2)

    print(f"Min is {min}")
    print(f"Max is {max}")
    print(f"Average is {avg}")

main()