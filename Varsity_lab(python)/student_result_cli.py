'''
A simple command line application to calculate student results , and also export them to a .csv file.
'''
def prompt_non_empty(prompt : str) -> str:
    while True:
        s:str = input(prompt).strip()
        if s :
            return s
        else:
            print("Empty input is not allowed , try again.")
            
            
def clean_name(name : str) -> str:
    return name.strip().title()


def prompt_int (prompt : str , min_value : int = 0 , max_value : int = int) | None = None) -> int :
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        if val < min_value :
            print(f"Value must be at least {min_value}. Try again.")
            continue
        if max_value is not None and val > max_value :
            print(f"Value must be at most {max_value}. Try again.")
            continue
        return val
        
def prompt_float (prompt : str , min_value : float = 0.0 , max_value : float = None) -> float :
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
        except ValueError:
            print("Invalid input. Please enter a valid float.")
            continue
        if val < min_value :
            print(f"Value must be at least {min_value}. Try again.")
            continue
        if max_value is not None and val > max_value :
            print(f"Value must be at most {max_value}. Try again.")
            continue
        return val

def grade_from_mark(mark : float) -> str:
    if mark >= 90.0 :
        return "A"
    elif mark >= 80.0 :
        return "B"
    elif mark >= 70.0 :
        return "C"
    elif mark >= 60.0 :
        return "D"
    else:
        return "F"
    
def compute_total_and_average(marks : list[float]) -> tuple[float , float]:
    total = sum(marks)
    total = 0.0
    for m in marks:
        total += m
    percentage = total / len(marks) * 100.0
    return total , percentage







def print_menu() -> None:
    #pass
    print("------> Student Results Calculator <------")
    print("1. Add Student + computer results" , end =",")
    print("2. List students and results")
    print("3.Search student by ID")
    print("4. Delete student by ID")
    print("5. Export results to CSV")
    print("6. Exit")


def main() -> None:
    students : list[dict] = [] #List to contain student data
    while True:

        print_menu()
        choice : str = input("Choose an option ( 1  - 6 ) : ").strip()
            # match - case is only available after python 3.10
        match choice :
            case "1":
                add_students(students)
            case "2":
                print("Listing students and results...")
            case "3":
                print("Searching Students by id ...")
            case "4":
                print("Deleting student by id ... ")
            case "5":
                print("Exporting results to CSV ...")
            case "6":
                print("Exiting the application...")
                return
            case _:
                print("Invalid choice. Try a valid option.!!!")


#print(__name__)             # without calling main function we can run like this on another file.

if __name__ == "__main__":
    main()
