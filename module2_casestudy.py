# Name: Kaylee Wirtjes
# File: module2_casestudy.py
# Description: This program checks student GPAs to determine if the qualify for the Dean's List or Honor Roll.

while True:
    last_name = input("Enter the student's last name (ZZZ to quit): ")
    if last_name.upper() == 'ZZZ':
        break
    
    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List.")
    elif gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll.")
    else:
        print(first_name, last_name, "did not qualify for the Dean's List or Honor Roll.")



