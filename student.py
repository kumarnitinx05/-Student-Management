
students = []

def add_student():
    roll_no = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
        print("\nTotal students:", len(students))

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def display_students():
    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\nRoll Number:", student["roll_no"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")
