# Name: [Castillo, Airish Dhyn D.]
# Section: [A]
# Activity: ELEC 4 - Set 1 - P2
# File: student_utils.py
# Date: [Date Completed]

#Function 1 - Calculate Average
def calculate_average(grades):
    return sum(grades) / len(grades)

#Function 2 - Determine if the student passed or failed
def determine_status(grades):
    average = calculate_average(grades)
    if average >= 75:
        return "Passed"
    else:
        return "Failed"

#Function 3 - Get the highest grade
def get_highest_grade(grades):
    return max(grades)

#Function 4 - Get the lowest grade
def get_lowest_grade(grades):
    return min(grades)