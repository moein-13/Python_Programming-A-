class Student:
    def __init__(self,student_id , name , department , cgpa):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.cgpa = cgpa


    def __str__(self):
        return f"{self.student_id},{self.name},{self.department} , {self.cgpa}"
