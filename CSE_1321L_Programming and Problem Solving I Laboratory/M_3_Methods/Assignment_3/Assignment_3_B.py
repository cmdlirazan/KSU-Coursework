#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 3B

print("[Character Frequencies]")
text = input("Enter a string: ").lower()
text = text.replace(" ", "")
i = 0

while text != "":
    found_char = False
    current = ""
    for ch in text:
        if ch.isalpha():
            current = ch
            found_char = True
            break
    if not found_char:
        break
    count = 0
    for ch in text:
        if ch == current:
            count += 1
    if count == 1:
        print(f"{current} appears 1 time")
    else:
        print(f"{current} appears {count} times")
    text = text.replace(current, "0")