#Name: Castillo, Airish Dhyn D.
#Section: A
#Activity: ELEC 4 - Set 1 - P2
#Date: November 19, 2026

import student_utils  #This imports the custom module.
from datetime import datetime

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


#Function to display the results
def display_results(grades):    
    average = student_utils.calculate_average(grades)
    status = student_utils.determine_status(grades)
    highest_grade = student_utils.get_highest_grade(grades)
    lowest_grade = student_utils.get_lowest_grade(grades)

    print("\nResults:")
    print("Report Generated:", report_date)
    print(f"Average Grade: {average:.2f}")
    print(f"Status: {status}")
    print(f"Highest Grade: {highest_grade}")
    print(f"Lowest Grade: {lowest_grade}")

report_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#Main function to run the program
def main():
    grades = enter_grades()
    display_results(grades)

#Main program
if __name__ == "__main__":
    main()