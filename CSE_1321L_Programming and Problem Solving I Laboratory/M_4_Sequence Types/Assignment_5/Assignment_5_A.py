#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 5A

def pairDifferences(numbers):
    if len(numbers) < 2:
        print("Not enough numbers to calculate differences.")
        return ()

    differences = tuple(abs(numbers[i] - numbers[i + 1]) for i in range(len(numbers) - 1))
    return differences

user_input = input("Enter a list of numbers: ")

try:
    number_list = [int(num) for num in user_input.split(",")]
    result = pairDifferences(number_list)
    if result:
        print("The absolute differences between consecutive numbers:", result)
except ValueError:
    print("Invalid input. Please enter a comma-separated list of integers.")