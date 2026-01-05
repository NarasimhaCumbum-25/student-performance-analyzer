# Student Performance Analytics System
# Python + Pandas (Clean Start)

import pandas as pd

# Read data files
students = pd.read_csv("data/students.csv")
marks = pd.read_csv("data/marks.csv")
attendance = pd.read_csv("data/attendance.csv")

# Merge all data
data = (
    students
    .merge(marks, on="student_id")
    .merge(attendance, on="student_id")
)

# Calculate average marks per student
avg_marks = (
    data
    .groupby("student_id")["marks"]
    .mean()
    .reset_index()
)

avg_marks.rename(
    columns={"marks": "average_marks"},
    inplace=True
)

# Grade assignment logic
def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

avg_marks["grade"] = avg_marks["average_marks"].apply(assign_grade)

# Top and weak students
top_students = avg_marks.sort_values(
    by="average_marks",
    ascending=False
).head(3)

weak_students = avg_marks.sort_values(
    by="average_marks"
).head(3)

# Subject-wise performance
subject_analysis = (
    data
    .groupby("subject")["marks"]
    .mean()
    .reset_index()
)

# Attendance impact
performance = avg_marks.merge(
    attendance,
    on="student_id"
)

high_attendance = performance[
    performance["attendance_percentage"] >= 85
]

low_attendance = performance[
    performance["attendance_percentage"] < 75
]

# Display results
print("\nAverage Marks & Grades:")
print(avg_marks)

print("\nTop Performers:")
print(top_students)

print("\nStudents Needing Improvement:")
print(weak_students)

print("\nSubject-wise Performance:")
print(subject_analysis)

print("\nHigh Attendance Students:")
print(high_attendance)

print("\nLow Attendance Students:")
print(low_attendance)
