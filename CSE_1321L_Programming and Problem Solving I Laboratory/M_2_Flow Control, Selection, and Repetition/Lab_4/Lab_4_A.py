#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 4A

grade = float(input("Enter your grade: "))

if 97.1 <= grade <= 100.0:
    letter_grade = "A+"
elif 94.1 <= grade <= 97.0:
    letter_grade = "A"
elif 91.1 <= grade <= 94.0:
    letter_grade = "A-"
elif 88.1 <= grade <= 91.0:
    letter_grade = "B+"
elif 85.1 <= grade <= 88.0:
    letter_grade = "B"
elif 82.1 <= grade <= 85.0:
    letter_grade = "B-"
elif 79.0 <= grade <= 82.0:
    letter_grade = "C+"
elif 76.1 <= grade <= 79.0:
    letter_grade = "C"
elif 73.1 <= grade <= 76.0:
    letter_grade = "C-"
elif 70.1 <= grade <= 73.0:
    letter_grade = "D+"
elif 67.1 <= grade <= 70.0:
    letter_grade = "D"
elif 64.1 <= grade <= 67.0:
    letter_grade = "D-"
elif 0.0 <= grade <= 64.0:
    letter_grade = "F"

print("Letter grade is: " + str(letter_grade))