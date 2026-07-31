#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 6B

import random

def guess():
    random_number = random.randint(1, 100)
    print("Guess the number I am thinking!")

    while True:
        enter = int(input("Enter any number between 1 and 100: "))
        if enter > random_number:
            print("Too high!")
        elif enter < random_number:
            print("Too low!")
        else:
            print(f"Correct! I was thinking of {random_number}")
            break

guess()