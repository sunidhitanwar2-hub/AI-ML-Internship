
import numpy as np

# Student names
students = np.array(["Aarav", "Priya", "Rahul", "Neha", "Ananya"])

# Marks in three subjects: Python, Maths, and Science
marks = np.array([
    [85, 90, 88],
    [92, 95, 91],
    [70, 75, 72],
    [60, 65, 68],
    [98, 96, 99]
])

subjects = ["Python", "Maths", "Science"]

# Calculate each student's total and average
totals = np.sum(marks, axis=1)
averages = np.mean(marks, axis=1)

print("===== STUDENT MARKS ANALYSIS =====")

for i in range(len(students)):
    print(f"\nStudent: {students[i]}")
    print("Marks:", marks[i])
    print("Total:", totals[i], "/ 300")
    print(f"Average: {averages[i]:.2f}%")

    if averages[i] >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

# Subject-wise analysis
print("\n===== SUBJECT-WISE ANALYSIS =====")

subject_averages = np.mean(marks, axis=0)

for i in range(len(subjects)):
    print(f"{subjects[i]} average: {subject_averages[i]:.2f}")

# Overall class analysis
print("\n===== CLASS SUMMARY =====")
print("Class average:", round(np.mean(marks), 2))
print("Highest mark:", np.max(marks))
print("Lowest mark:", np.min(marks))

# Identify the student with the highest average
top_index = np.argmax(averages)
print("Top student:", students[top_index])
print(f"Top student's average: {averages[top_index]:.2f}%")
