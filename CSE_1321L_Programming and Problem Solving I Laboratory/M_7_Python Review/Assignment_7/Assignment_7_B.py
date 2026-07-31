#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 7B

def calculate_average(scores):
    return sum(scores) / len(scores)

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def main():
    student_list = []
    num_students = int(input("Enter number of students: "))

    for i in range(num_students):
        print()
        print(f"Enter details for student {i + 1}:")
        name = input("Enter student name: ")

        scores = []
        for subject in ["Math", "English", "Science"]:
            while True:
                try:
                    score = float(input(f"Enter score for {subject}: "))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")

        total = sum(scores)
        average = calculate_average(scores)
        grade = get_grade(average)
        status = "Pass" if grade != "F" else "Fail"

        print(f"Total score: {total:.1f}")
        print(f"Average score: {average:.2f}")
        print(f"Grade: {grade}")
        print(f"Status: {status}")

        student = {
            "name": name,
            "scores": scores,
            "total": total,
            "average": average,
            "grade": grade,
            "status": status
        }
        student_list.append(student)

    print()
    width = 30
    print("=" * 30)
    print(" Summary Report".center(width))
    print("=" * 30)

    total_class_avg = 0
    passed = failed = 0
    top_student = student_list[0]

    for student in student_list:
        print()
        print(f"Name: {student['name']}")
        print(f"Scores: {student['scores']}")
        print(f"Total: {student['total']:.1f}")
        print(f"Average: {student['average']:.2f}")
        print(f"Grade: {student['grade']}")
        print(f"Status: {student['status']}")
        if student["status"] == "Pass":
            passed += 1
        else:
            failed += 1
        if student["average"] > top_student["average"]:
            top_student = student

        total_class_avg += student["average"]

    class_average = total_class_avg / len(student_list)
    print()
    print(f"Class Average: {class_average:.2f}")
    print(f"Students Passed: {passed}")
    print(f"Students Failed: {failed}")
    print(f"Top Student: {top_student['name']}")

main()