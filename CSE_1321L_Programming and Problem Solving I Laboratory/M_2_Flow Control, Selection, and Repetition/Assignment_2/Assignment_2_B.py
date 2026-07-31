#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 2B

def loan_approval_system():
    print("[Loan Approval System]")

    age = int(input("Enter your age: "))
    income = int(input("Enter your income: $"))
    credit_score = int(input("Enter your credit score: "))

    if age < 18:
        print("You do not qualify for a loan due to age.")
        return

    if credit_score < 300 or credit_score > 850:
        print("Invalid credit score. Please enter a score between 300 and 850.")
        return

    match credit_score:
        case score if 700 <= score <= 850:
            credit_category = "Good"
        case score if 600 <= score <= 699:
            credit_category = "Fair"
        case score if 300 <= score <= 599:
            print("You do not qualify for a loan due to poor credit.")
            return

    if income >= 100000 and credit_category == "Good":
        print("You qualify for a Premium Loan.")
    elif 50000 <= income < 100000 and (credit_category == "Good" or credit_category == "Fair"):
        print("You qualify for a Standard Loan.")
    elif income < 50000 and credit_category == "Fair":
        print("You qualify for a Basic Loan.")
    else:
        print("Your income is too low for a loan.")

loan_approval_system()