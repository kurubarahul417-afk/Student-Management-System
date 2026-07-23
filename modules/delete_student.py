def delete_student(students):
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