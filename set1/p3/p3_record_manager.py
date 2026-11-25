
#Name: Castillo, Airish Dhyn D.
#Section: IV-BSIT A
#Activity: ELEC 4 - Set 1 - P3
#Date: November 23, 2026


#List to store student names
student_records = []

#Set to prevent duplicate student names
student_set = set()


#Function to check for duplicate student names
def check_duplicate(name):
    return name.lower() in student_set


#Function to add a student
def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Student name cannot be empty.")
        return

    if check_duplicate(name):
        print(f"Student {name} already exists.")
    else:
        student_records.append(name)
        student_set.add(name.lower())
        print(f"Student {name} added successfully.")


#Function to remove a student
def remove_student():
    name = input("Enter student name to remove: ").strip()

    if name == "":
        print("Student name cannot be empty.")
        return

    for student in student_records:
        if student.lower() == name.lower():
            student_records.remove(student)
            student_set.remove(student.lower())
            print(f"Student {student} removed successfully.")
            return

    print(f"Student {name} does not exist.")


#Function to search for a student
def search_student():
    name = input("Enter student name to search: ").strip().lower()

    if name == "":
        print("Search name cannot be empty.")
        return

    found_students = []

    for student in student_records:
        if name in student.lower():
            found_students.append(student)

    if found_students:
        print("\nStudent(s) found:")

        for student in found_students:
            print(student)
    else:
        print("Student not found.")


#Function to display all students alphabetically
def display_students():
    if student_records:
        print("\nStudent Records:")

        sorted_students = sorted(student_records, key=str.lower)

        for number, name in enumerate(sorted_students, start=1):
            print(f"{number}. {name}")

        print(f"Total students: {len(student_records)}")

    else:
        print("No student records found.")


#Function to display the menu and handle user choices
def main():
    while True:
        print("\n================================")
        print("    STUDENT RECORD MANAGER")
        print("================================")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()

        elif choice == '2':
            remove_student()

        elif choice == '3':
            search_student()

        elif choice == '4':
            display_students()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


#Explanation of the difference between a list and a set
#A list contains the original student names and is used to
#display them in alphabetical order. Meanwhile, a set keeps
#lowercase versions of the names to check for duplicates.
#Unlike a list, which can store repeated values, a set only
#allows unique entries.
