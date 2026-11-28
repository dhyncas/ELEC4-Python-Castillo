#Name: Castillo, Airish Dhyn D.
#Section: A
#Activity: ELEC 4 - Set 1 - P1
#Date: November 18, 2026

#Global variable for passing grade
PASSING_GRADE = 75


#Function to enter grades
def enter_grades():
    grades = []

    while True:
        try:
            number_of_grades = int(input("How many grades will you enter? "))

            if number_of_grades > 0:
                break
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    for number in range(number_of_grades):
        while True:
            try:
                grade = float(input(f"Enter grade {number + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    return grades


#Function to calculate average
def calculate_average(grades):
    return sum(grades) / len(grades)


#Function for getting the highest grade
def get_highest_grade(grades):
    return max(grades)


#Function for getting the lowest grade
def get_lowest_grade(grades):
    return min(grades)

#Function for determining if the student passed or failed based on the average grade
def determine_status(grades):
    average = calculate_average(grades)

    if average >= PASSING_GRADE:
        return "PASSED"
    else:
        return "FAILED"

#Function to display the results
def display_results(grades):
    if not grades:
        print("\nNo grades available. Please enter grades first.")
        return
    
    average = calculate_average(grades)
    highest_grade = get_highest_grade(grades)
    lowest_grade = get_lowest_grade(grades)
    status = determine_status(grades)

    print("\n========== STUDENT GRADE RESULTS ==========)")
    print("Grades:", grades)
    print(f"Average Grade: {average:.2f}")
    print(f"Highest Grade: {highest_grade:.2f}")
    print(f"Lowest Grade: {lowest_grade:.2f}")
    print(f"Status: {status}")
    print("============================================")

#Function to display the menu
def display_menu():
    print("\n========== STUDENT GRADE CALCULATOR ==========")
    print("1. Enter Grades")
    print("2. Display Results")
    print("3. Exit")
    print("==============================================")

#Main function to run the program
def main():
    grades = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            grades = enter_grades()
            print("\nGrades successfully entered!")

        elif choice == "2":
            display_results(grades)

        elif choice == "3":
            print("\nThank you for using the Student Grade Calculator!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


main()


# Local and Global Variables:
# A global variable is declared outside functions and can be accessed
# by different functions in the program. In this program, PASSING_GRADE
# is a global variable because it is declared outside the functions.
# A local variable is declared inside a function and is only accessible
# within that function. For example, grades inside main() is a local variable.