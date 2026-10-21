# Student Marks Analysis Project

students = [
    {"name": "Ali", "math": 85, "english": 78, "computer": 92},
    {"name": "Sara", "math": 95, "english": 88, "computer": 96},
    {"name": "Ahmed", "math": 65, "english": 72, "computer": 68},
    {"name": "Ayesha", "math": 45, "english": 55, "computer": 60},
    {"name": "Zain", "math": 35, "english": 42, "computer": 38},
]


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


total_marks = 300

for student in students:
    obtained = (
        student["math"]
        + student["english"]
        + student["computer"]
    )

    percentage = (obtained / total_marks) * 100
    grade = calculate_grade(percentage)

    print("-" * 35)
    print("Student:", student["name"])
    print("Total Marks:", obtained, "/", total_marks)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)

    if percentage >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")

class_averages = []

for student in students:
    total = student["math"] + student["english"] + student["computer"]
    class_averages.append(total / 3)

print("\nClass Average:", round(sum(class_averages) / len(class_averages), 2))

top_student = max(
    students,
    key=lambda student: (
        student["math"] + student["english"] + student["computer"]
    )
)

print("Top Student:", top_student["name"])