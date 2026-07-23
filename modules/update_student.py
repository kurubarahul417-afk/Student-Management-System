def update_students(students):
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