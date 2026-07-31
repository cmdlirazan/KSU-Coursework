#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 6C

while True:
    n = int(input("Enter Number for Rows or 0 to quit: "))
    if n == 0:
        break
    else:
        for i in range(1, n + 1):
            print(" " * (n - i), end="")
            for j in range(i, 0, -1):
                print(j, end="")
            for j in range(2, i + 1):
                print(j, end="")
            print()