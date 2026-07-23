def view_students(students):
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