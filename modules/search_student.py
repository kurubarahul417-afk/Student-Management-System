def search_student(students):
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