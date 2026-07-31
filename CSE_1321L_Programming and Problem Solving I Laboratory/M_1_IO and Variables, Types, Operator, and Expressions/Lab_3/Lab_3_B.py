#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 3B

Course_1 = int(input("Course 1 hours: "))
Grade_1 = int(input("Grade for course 1: "))
Course_2 = int(input("Course 2 hours: "))
Grade_2 = int(input("Grade for course 2: "))
Course_3 = int(input("Course 3 hours: "))
Grade_3 = int(input("Grade for course 3: "))
Course_4 = int(input("Course 4 hours: "))
Grade_4 = int(input("Grade for course 4: "))

Total_Hours = Course_1+Course_2+Course_3+Course_4

Total_Quality_Points = (Course_1*Grade_1)+(Course_2*Grade_2)+(Course_3*Grade_3)+(Course_4*Grade_4)

GPA = Total_Quality_Points/Total_Hours
GPA_rounded = round(GPA, 2)

print("Total hours: " + str(Total_Hours))
print("Total quality points: " + str(Total_Quality_Points))
print("Your GPA for this semester is " + str(GPA_rounded))