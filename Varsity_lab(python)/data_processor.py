'''
This module contains the data processing functions for the student result management system.
'''

from __future__ import annotations
from re import sub

from student_result_cli import compute_total_and_average
from utils import prompt_non_empty , prompt_int , prompt_float , clean_name , grade_from_mark   


def print_student_report(student : dict) -> None:
    print ("\n" + "-"* 50)
    print(f"Student ID : {student['id']}")
    print(f"Name : {student['name']}")
    print(f"Subjects : {', '.join(student['subjects'])}")
    print(f"Marks : {', '.join(str(m) for m in student['marks'])}")
    print(f"Total : {student['total']}")
    print(f"Percentage : {student['percentage']:.2f}%")
    print(f"Grade : {student['grade']}")
    print(f"Status : {student['status']}")

    
    
def list_students(students : list[dict]) -> None:
    if not students :
        print("No students found.")
        return
    for student in students :
        print_student_report(student)
        

def add_students(students : list[dict]) -> None:

        sid : str = prompt_non_empty("Enter a student id :").strip()
        name = clean_name(prompt_non_empty("Enter student name : "))
        
        
        n = prompt_int("Enter number of subjects : " , min_value = 1)
        subjects : list[dict] = []
        marks : list[float] = []

        for i in range (n):
            sub = prompt_non_empty(f"Enter name of subject {i+1} : ")
            sub = sub.strip().title()
            subjects.append(sub)
            mark = prompt_float(f"Enter marks for {sub} : " , min_value = 0.0 , max_value = 100.0)
            marks.append(mark) 
    
    
            total , pct = compute_total_and_average(marks)
            grade = grade_from_mark(pct)
            status = "Pass" if grade != "F" else "Fail"
        
        student = {
            "id" : sid ,
            "name" : name ,
            "subjects" : subjects ,
            "marks" : marks ,
            "total" : total ,
            "percentage" : pct ,
            "grade" : grade ,
            "status" : status
            }
        students.append(student)