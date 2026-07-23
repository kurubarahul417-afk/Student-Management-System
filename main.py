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
        print("\n----- Add Student -----")
        student_id = input("Enter Student ID: ")
        student_name = input("Enter Student Name: ")
        student_age = input("Enter Student Age: ")
        student_department = input("Enter Student Department: ")

        print("\nStudent Details")
        print("Student ID:", student_id)
        print("Student Name:", student_name)
        print("Student Age:", student_age)
        print("Student Department:", student_department)

        students.append({
            "id": student_id,
            "name": student_name,
            "age": student_age,
            "department": student_department
        })
        print("Students added successfully!")
        with open("students.json", "w") as file:
         json.dump(students, file, indent=4)


    elif choice == "2":
        print("\n----- Student List -----")

        if len(students) == 0:
            print("No students found.")

        else:
            for student in students:
                print("-----------------------")
                print("Student ID:", student["id"])
                print("Student Name:", student["name"])
                print("Student Age:", student["age"])
                print("Student Department:", student["department"])

    elif choice == "3":

        search_id = input("Enter Student ID to search: ")

        found = False

        for student in students:

            if student["id"] == search_id:

                print("\nStudent Found")
                print("Student ID:", student["id"])
                print("Student Name:", student["name"])
                print("Student Age:", student["age"])
                print("Student Department:", student["department"])

                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == "4":

        update_id = input("Enter Student ID to update: ")

        found = False

        for student in students:

            if student["id"] == update_id:

                print("\nEnter New Details")

                student["name"] = input("Enter New Name: ")
                student["age"] = input("Enter New Age: ")
                student["department"] = input("Enter New Department: ")

                print("Student updated successfully!")

                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == "5":

        delete_id = input("Enter Student ID to delete: ")

        found = False

        for student in students:

            if student["id"] == delete_id:

                students.remove(student)

                print("Student deleted successfully!")

                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == "6":
        print("Thank you")
        break

    else:
        print("Invalid Choice")