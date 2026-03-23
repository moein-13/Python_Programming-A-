from manager import StudentManager

manager = StudentManager()

while True:
    print("\n---Student Management System ---")
    print("1. Add student.")
    print("2. Show all students.")
    print("3. Update student.")
    print("4. Delete student")
    print("5. Exit.")

    choice = input("\nEnter your choice: ")
    if choice == "1" :
        student_id = int(input("Enter your id : "))
        name = input("Enter your name : ")
        department = input("Enter your department : ")
        cgpa = float(input("Enter your cgpa : "))

        manager.add_student(student_id,name,department,cgpa)

    elif choice == "2":
        print("Student Id   Name   Department  CGPA")
        manager.show_all_student()
    elif choice == "3":
        student_id = int(input("Enter a Student_id to update : "))
        print("Leave blank if you dont want to change.")

        name = input("Enter a new_name to update :")
        department = input("Enter new department :")
        cgpa = float(input("Enter new cgpa :"))

        manager.update_student(student_id ,
                               new_name= name if name else None,
                               new_department= department if department else None,
                               new_cgpa= float(cgpa) if cgpa else None
                               )
    elif choice == "4":
        student_id = int(input("Enter student id to delete :"))
        manager.delete_student(student_id)

    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice , Try again.")