#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 5A

print("Please enter 10 numbers and this program will display the largest.")

largest = 0

for i in range(1,11):
    num = int(input(f"Please enter number {i}: "))
    if num > largest:
        largest = num
print(f"The largest number was {largest}")