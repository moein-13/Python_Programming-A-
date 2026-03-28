import csv
from tabulate import tabulate
class Turf:
    
    def __init__(self, turf_id , name , location , price_per_hour):
        
        self.turf_id = turf_id 
        self.name = name 
        self.location = location 
        self.price_per_hour = price_per_hour
        
    def display_info(self):
        
        print(f"Turf Id : {self.turf_id}")
        print(f"Name : {self.name}.")
        print(f"Location : {self.location}.")
        print(f"Price per hour : {self.price_per_hour} Tk.")
        
class TurfManager:
    
    def __init__(self):
        self.turf_list = []
        
    
    def get_valid_text_input(self,prompt):
        
        while True :
            user_input = input(prompt ).strip()
            
            if user_input == "":
                print("Input can not be blank . please enter a valid input.")
                
            elif user_input.isdigit():
                print("Input can not be a number . Please enter a valid String input.")
                
            else:
                return user_input
    
    def get_valid_number_input(self , prompt):
        
        while True :
            
            user_input = input (prompt).strip()
            
            if user_input == "":
                print("Input can not be blank . Please enter a valid input.")
            elif not user_input.isdigit():
                print("Input must be a number . Please enter a valid number .")
                
            else:
                return int(user_input)
            
    
    # Add a turf 
    
    def add_turf(self):
        
        print("---> Add a new turf <---")
        
        t_id = self.get_valid_text_input("Enter a unique turf id :")
        t_name = self.get_valid_text_input("Enter a turf name :")
        t_location = self.get_valid_text_input("Enter a turf location :")
        t_price = self.get_valid_number_input("Enter a turf price per hour :")
        
        
        new_turf = Turf(t_id , t_name , t_location , t_price )
        self.turf_list.append(new_turf)
        
        print(f"Successfully added turf : {t_name} with unique id : {t_id}.")
        
    # view all turfs
    
    def view_all_turfs(self):
        
        print( "---> View all Turfs <---")
        
        if len(self.turf_list) == 0 :
            
            print("No turfs have been added yet.")
        else:
            
            table_data = []
            
            for turf in self.turf_list:
                table_data.append([turf.turf_id , turf.name , turf.location ,f"{turf.price_per_hour} Tk."])
                
            Header = ["Turf ID", "Name", "Location", "Price per Hour"]
            
            print(tabulate(table_data, headers=Header, tablefmt="grid"))
    
    # Update a turf 
        
    def update_turf(self):
        
        print("---> Update a turf <---")
        
        if len(self.turf_list) == 0 :
            print ("Turf is empty . You can not update it.")
            return
        
        search_turf = self.get_valid_text_input("Enter the unique id of the turf you want to update :")
        
        for turf in self.turf_list:
            
            if turf.turf_id == search_turf:
                
                print(f"Turf found . You can update the details now.")
                
                t_name = self.get_valid_text_input("Enter a new turf name :")
                t_location = self.get_valid_text_input("Enter a new turf location :")
                t_price = self.get_valid_number_input("Enter a new turf price per hour :")
                
                turf.name = t_name
                turf.location = t_location
                turf.price_per_hour = t_price
                
                print(f"Successfully updated turf with id : {search_turf}.")
                return
            
            else:
                print(f"No turf found with this id : {search_turf}. Please try again.")
                
    # delete turf
    
    def delete_turf(self):
        print ("---> Delete a turf <---")
        
        if len(self.turf_list) == 0 :
            
            print( "Turf is empty . You can not delete anything .")
            return
        
        search_turf = self.get_valid_text_input("Enter the unique id of the turf you want to delete :") 
        
        for turf in self.turf_list:
            
            if turf.turf_id == search_turf:
                self.turf_list.remove(turf)
                
                print(f"Succesfully deleted a turf with id : {search_turf}.")
                return
            
            else:
                print(f"No turf found with this id : {search_turf}. Please try again.")          
            


    def save_turfs(self):
    
        with open("Turfs.csv" , mode = "w" , newline = "") as file :
        
            writer = csv.writer(file)
            for turf in self.turf_list:
                writer.writerow([turf.turf_id , turf.name , turf.location , turf.price_per_hour])

    def load_turfs(self):
    
        try:
            with open("Turfs.csv" , mode = "r") as file :
                reader = csv.reader(file)
                for row in reader :
                    if len(row) == 4 :
                        t_id = row[0]
                        t_name = row[1]
                        t_location = row[2]
                        t_price = int(row[3])
                    
                        loaded_turf = Turf(t_id , t_name , t_location , t_price)
                        self.turf_list.append(loaded_turf)
                    
        except FileNotFoundError:
            pass
        
        