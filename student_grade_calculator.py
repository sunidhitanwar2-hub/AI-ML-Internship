
# Student Grade Calculator
# Enter marks for five subjects and calculate the grade.

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def main():
    student_name = input("Enter student name: ")
    subjects = ["Python", "Mathematics", "Science", "English", "Computer Science"]
    marks_list = []

    for subject in subjects:
        while True:
            try:
                marks = float(input(f"Enter marks for {subject} (0-100): "))

                if 0 <= marks <= 100:
                    marks_list.append(marks)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks_list)
    percentage = total / len(subjects)
    grade = calculate_grade(percentage)

    print("\n===== STUDENT REPORT =====")
    print("Student:", student_name)
    print("Total Marks:", total, "/ 500")
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", grade)
    print("Result:", "Pass" if percentage >= 40 else "Fail")


if __name__ == "__main__":
    main()
