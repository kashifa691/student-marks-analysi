import pandas as pd

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

results = []

for student in students:
    obtained = (
        student["math"]
        + student["english"]
        + student["computer"]
    )

    percentage = (obtained / 300) * 100
    grade = calculate_grade(percentage)
    result = "Pass" if percentage >= 50 else "Fail"

    results.append({
        "Name": student["name"],
        "Math": student["math"],
        "English": student["english"],
        "Computer": student["computer"],
        "Total": obtained,
        "Percentage": round(percentage, 2),
        "Grade": grade,
        "Result": result
    })

df = pd.DataFrame(results)

print("\nSTUDENT MARKS ANALYSIS")
print(df.to_string(index=False))

print("\nClass Average:",
      round(df["Percentage"].mean(), 2), "%")

top_student = df.loc[df["Total"].idxmax()]
print("Top Student:", top_student["Name"])

df.to_csv("student_marks.csv", index=False)

print("\nCSV file created successfully!")