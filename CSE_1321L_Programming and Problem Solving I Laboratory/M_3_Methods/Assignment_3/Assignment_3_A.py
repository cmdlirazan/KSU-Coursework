#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 3A

size = int(input("Enter an odd number for the size of the diamond: "))
if size % 2 == 0:
    size += 1
    print(f"Size must be an odd number; we will increase it to {size}")
mid = size // 2
num = 0

for i in range(mid + 1):
    for s in range(mid - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print(num % 10, end="")
        num += 1
    print()

for i in range(mid - 1, -1, -1):
    for s in range(mid - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print(num % 10, end="")
        num += 1
    print()