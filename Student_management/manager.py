from Student import Student
FILE_NAME = "data.txt"
class StudentManager:
    def __init__ (self):
        self.students = []
        self.load_from_file()
## Add student feature
    def add_student(self , student_id , name , department, cgpa):
        student = Student(student_id , name, department, cgpa)
        self.students.append(student)
        self.save_to_file()
## Show students feature
    def show_all_student(self):
        if not self.students:
            print("No Students Found.!!!")
            return

        for student in self.students:
            print(student)

    ## Update feature

    def update_student(self , student_id ,
                       new_name = None ,
                       new_department= None ,
                       new_cgpa = None):
        self.save_to_file()
        for student in self.students:
            if student.student_id == student_id:

                if new_name is not None:
                    student.name = new_name
                if new_department is not None:
                    student.department = new_department

                if new_cgpa is not None:
                    student.cgpa = new_cgpa

                print("Student update successfully.")
                return

        print("Student not found")

        ## Delete feature
    def delete_student(self,student_id):
        self.save_to_file()
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")

## save file
    def save_to_file(self):
        with open(FILE_NAME, "w") as file:
            for student in self.students:
                file.write(str(student) + "\n")

    ## load from file
    def load_from_file(self):
        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    student_id , name , department , cgpa = line.strip().split(",")
                    student = Student(int(student_id),name , department , float(cgpa))
                    self.students.append(student)
        except FileNotFoundError:
            pass



