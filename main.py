from modules.delete_student import delete_student
from modules.add_student import add_student
from modules.view_student import view_students
from modules.search_student import search_student
from modules.update_student import update_students
import json

try:
    with open("students.json", "r") as file:
        students = json.load(file)
except:
    students = []

while True:

    print("====================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("====================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        update_students(students)
        

    elif choice == "5":
        delete_student(students)

    elif choice == "6":
        print("Thank you")
        break

    else:
        print("Invalid Choice")