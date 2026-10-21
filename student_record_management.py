
# Day 3: Student Record Management System

FILE_NAME = "students.txt"


def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()

    if not student_id or not name:
        print("Student ID and name cannot be empty.")
        return

    # Prevent duplicate student IDs
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line in file:
            record = line.strip().split("|")
            if record[0] == student_id:
                print("This student ID already exists.")
                return

    try:
        age = int(input("Enter student age: "))
        marks = float(input("Enter student marks: "))
    except ValueError:
        print("Age must be a whole number and marks must be numeric.")
        return

    if age <= 0 or not 0 <= marks <= 100:
        print("Enter a positive age and marks between 0 and 100.")
        return

    if "|" in name:
        print("The name cannot contain the | character.")
        return

    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"{student_id}|{name}|{age}|{marks}\n")

    print("Student record saved successfully!")


def view_students():
    print("\n--- All Student Records ---")

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        records = file.readlines()

    if not records:
        print("No student records found.")
        return

    for line in records:
        student_id, name, age, marks = line.strip().split("|")
        print(
            f"ID: {student_id} | Name: {name} | "
            f"Age: {age} | Marks: {marks}"
        )


def search_student():
    print("\n--- Search Student ---")
    search_id = input("Enter student ID to search: ").strip()

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line in file:
            student_id, name, age, marks = line.strip().split("|")

            if student_id == search_id:
                print("Student found!")
                print(f"ID: {student_id}")
                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"Marks: {marks}")
                return

    print("Student not found.")


def main():
    # Create the text file if it does not exist
    with open(FILE_NAME, "a", encoding="utf-8"):
        pass

    while True:
        print("\n===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
