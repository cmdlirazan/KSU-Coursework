#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 4B

def check_length(password):
    return len(password) >= 8

def check_upper_lower(password):
    has_upper = False
    has_lower = False
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if has_upper and has_lower:
            return True
    return False

def check_special_character(password):
    for char in password:
        if char in "!@#":
            return True
    return False

def main():
    while True:
        password = input("Enter a password: ")
        errors = ""

        if not check_length(password):
            errors += "Must be at least 8 characters long. "
        if not check_upper_lower(password):
            errors += "Must contain both uppercase and lowercase letters. "
        if not check_special_character(password):
            errors += "Must include at least one special character (!, @, #). "

        if errors:
            print("Password does not meet the requirements:", errors.strip())
        else:
            print("Password is strong!")
            break

main()