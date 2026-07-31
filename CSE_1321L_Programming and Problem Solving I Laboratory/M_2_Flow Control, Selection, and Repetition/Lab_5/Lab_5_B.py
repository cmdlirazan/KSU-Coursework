#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 5B

size = int(input("Please enter a value for the size: "))

print("This is the requested " + str(size) + "x" + str(size) + " box: ")
for i in range(size):
    for j in range(size):
        print("*", end="")
    print()
print("This is the requested right-facing " + str(size) + "x" + str(size) + " right-triangle: ")
for i in range(1, size + 1):
    for j in range(i):
        print("*", end="")
    print()
print("This is the requested left-facing " + str(size) + "x" + str(size) + " right-triangle: ")
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()