#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 4A

def format_word(word):
    return word.capitalize()

def convert_to_pascal_case(text):
    pascal_case = ""
    word = ""
    for char in text:
        if char != " ":
            word += char
        elif word:
            pascal_case += format_word(word)
            word = ""
    if word:
        pascal_case += format_word(word)
    return pascal_case

def main():
    user_input = input("Enter a string: ")
    pascal_case_result = convert_to_pascal_case(user_input)
    print("Pascal Case:", pascal_case_result)

main()