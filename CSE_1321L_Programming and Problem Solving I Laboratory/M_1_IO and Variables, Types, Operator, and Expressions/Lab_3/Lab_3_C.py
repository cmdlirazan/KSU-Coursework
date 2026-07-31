#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 3C

Small_Sandwich_Amount = int(input("Enter the number of small sandwiches: "))
Medium_Sandwich_Amount = int(input("Enter the number of medium sandwiches: "))
Large_Sandwich_Amount = int(input("Enter the number of large sandwiches: "))
Extra_Large_Sandwich_Amount = int(input("Enter the number of extra-large sandwiches: "))

print()
print("You've entered " + str(Small_Sandwich_Amount) + " small sandwiches.")
print("You've entered " + str(Medium_Sandwich_Amount) + " medium sandwiches.")
print("You've entered " + str(Large_Sandwich_Amount) + " large sandwiches.")
print("You've entered " + str(Extra_Large_Sandwich_Amount) + " extra-large sandwiches.")

Total_Cooking_Time = (Small_Sandwich_Amount * 30) + (Medium_Sandwich_Amount * 60) + (Large_Sandwich_Amount * 75) + (Extra_Large_Sandwich_Amount * 135)

Minutes = int(Total_Cooking_Time/60)
Seconds = int(Total_Cooking_Time % 60)

print()
print("Total cooking time is " + str(Minutes) + " minutes and " + str(Seconds) + " seconds.")