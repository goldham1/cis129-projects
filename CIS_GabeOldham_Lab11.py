# Module 11 Lab-11
# Gabe Oldham
# 11/26/2024
# This code displays an option for running different tasks. It will ask for the
# scores of grades and then give you an average, it will also store specific 
# students name and 3 exxam scores.



import csv

def write_grades_to_file():
    """Writes grades to a plain text file."""
    with open('grades.txt', 'w') as file:
        print("Enter grades one by one. Type 'done' to finish.")
        while True:
            grade = input("Enter a grade (or 'done'): ")
            if grade.lower() == 'done':
                break
            if grade.isdigit():
                file.write(f"{grade}\n")
            else:
                print("Please enter a valid grade.")

def read_grades_from_file():
    """Reads grades from a plain text file and calculates statistics."""
    try:
        with open('grades.txt', 'r') as file:
            grades = [int(line.strip()) for line in file]

        if grades:
            total = sum(grades)
            count = len(grades)
            average = total / count
            print("\nGrades from file:", grades)
            print("Total:", total)
            print("Count:", count)
            print("Average:", average)
        else:
            print("No grades found in the file.")
    except FileNotFoundError:
        print("No grades.txt file found. Please write grades first.")

def write_student_records_to_csv():
    """Writes student records with grades to a CSV file."""
    with open('grades.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['firstname', 'lastname', 'exam1grade', 'exam2grade', 'exam3grade'])
        
        print("Enter student records. Type 'done' as the first name to stop.")
        while True:
            first_name = input("Enter first name (or 'done' to finish): ")
            if first_name.lower() == 'done':
                break
            last_name = input("Enter last name: ")
            try:
                exam1 = int(input("Enter exam 1 grade: "))
                exam2 = int(input("Enter exam 2 grade: "))
                exam3 = int(input("Enter exam 3 grade: "))
                writer.writerow([first_name, last_name, exam1, exam2, exam3])
            except ValueError:
                print("Please enter valid integer grades.")

def main():
    """Main menu for interacting with the program."""
    while True:
        print("\nMenu:")
        print("1. Write grades to a file: ")
        print("2. Read grades from a file and calculate statistics: ")
        print("3. Write student records to a CSV file: ")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        if choice == '1':
            write_grades_to_file()
        elif choice == '2':
            read_grades_from_file()
        elif choice == '3':
            write_student_records_to_csv()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
