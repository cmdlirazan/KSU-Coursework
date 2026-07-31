#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 3C

print("Welcome to the Guess the Word game!")
secret = input("Enter a word to guess (lowercase letters only): ")
guess = ""
for ch in secret:
    guess += "_"

while guess != secret:
    print("The word to guess is:", end=" ")
    for ch in guess:
        print(ch, end=" ")
    print()
    user = input("Guess a letter: ")
    if user in secret:
        print("Good guess!")
        new = ""
        for i in range(len(secret)):
            if secret[i] == user:
                new += user
            else:
                new += guess[i]
        guess = new
    else:
        print("Oops! That letter is not in the word.")
print(f"Congratulations! You've guessed the word: {secret}")