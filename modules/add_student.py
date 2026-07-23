def add_student(students):

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