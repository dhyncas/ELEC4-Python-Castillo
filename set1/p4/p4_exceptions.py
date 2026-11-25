
#Name: Castillo, Airish Dhyn D.
#Section: IV-BSIT A
#Activity: ELEC 4 - Set 1 - P4
#Date: November 24, 2026


#Function to divide two numbers entered by the user
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    else:
        print(f"The result of {num1} divided by {num2} is: {result}")

    finally:
        print("Execution of divide_numbers function completed.\n")


#Function to open and display the contents of a file
def read_file():
    try:
        filename = input("Enter the filename to read: ")

        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except OSError:
        print(f"Error: Unable to read the file '{filename}'.")

    else:
        print(f"\nContents of '{filename}':")
        print(content)

    finally:
        print("Execution of file operation completed.\n")


#Function to display the main menu
def main_menu():
    while True:
        print("====== Main Menu ======")
        print("1. Divide Two Numbers")
        print("2. Read a File")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            read_file()

        elif choice == "3":
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")


#Main function to run the program
if __name__ == "__main__":
    main_menu()
