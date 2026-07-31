#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 2A

print("[Discount Calculator]")

total_amount = float(input("Enter your total purchase amount: $"))

membership_status = input("Are you a member of the shopping club (Yes or No)? ")

if total_amount < 50:
    discount_percent = 0
elif 50 <= total_amount <= 200:
    discount_percent = 10 if membership_status == "yes" else 5
else:
    discount_percent = 15 if membership_status == "yes" else 10

discount_amount = round((discount_percent / 100) * total_amount, 1)
final_price = round(total_amount - discount_amount, 1)

print(f"Your discount is: ${discount_amount}")
print(f"Your total price after discount is: ${final_price}")