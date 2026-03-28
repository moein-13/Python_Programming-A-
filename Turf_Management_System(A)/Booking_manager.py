from Booking import Booking
import csv
class BookingManager:
    
    def __init__(self):
        self.booking_list = []
        
        
    def get_valid_text_input(self , prompt) :
        while True :
            
            user_input = input(prompt).strip()
            
            if user_input == "":
                print("Input can not be blank . Please enter a valid input.")
                
            elif user_input.isdigit():
                print("Input can not be a number . Please enter a valid String input.")
                
            else:
                return user_input
            
            
    # use for user input for time slot if user want to play 1 hour 30 min then also it will be valid input.        
    def get_valid_time_input(self , prompt):
        while True:
            
            user_input = input(prompt).strip()
            
            parts = user_input.split(".")
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                return user_input
            
            elif len(parts) == 1 and parts[0].isdigit():
                return user_input + ".00"
            else:
                print("Invalid time format . Please enter a valid time (e.g., 10:00 or 10:00 AM).")
                

            
    def add_booking(self, turf_manager) :
        
        print("\n---> Add a new booking <---")
        
        if len(turf_manager.turf_list) == 0 :
            print("No turf is available . Please add a turf first.")
            
            return
        
        print("\nAvailable Turfs :")
        
        for turf in turf_manager.turf_list :
            
            print(f"Turf Id : {turf.turf_id}")
            print(f"Turf Name : {turf.name}")
            print(f"Turf Location : {turf.location}")
            print(f"Turf Price per hour : {turf.price_per_hour} Tk.") 
            
        b_id = self.get_valid_text_input("Enter a unique booking id :")
        t_id = self.get_valid_text_input("Enter the turf id for booking : ")
            
            
        turf_exits = False 
            
        for turf in turf_manager.turf_list :
            if str(turf.turf_id) == str(t_id):
                    turf_exits = True
                    break
                
        if not turf_exits:
            print("Turf id does not exist . Please enter a valid turf id .")
            return
        
        c_name = self.get_valid_text_input("Enter customer name :")
        phone_number = self.get_valid_text_input("Enter phone number :")
        date = self.get_valid_text_input("Enter booking date (DD-MM-YYYY) :")
        
                
            
        start_time = self.get_valid_time_input("Enter start time (e.g., 10.00 AM or 10.30) :")
        end_time = self.get_valid_time_input("Enter end time (e.g., 11.30  or 11.30 AM) :")  
        
        start_parts = start_time.split(".")
        start_total_minutes = (int(start_parts[0]) * 60) + int(start_parts[1])
        
        end_parts = end_time.split(".")
        end_total_minutes = (int(end_parts[0]) * 60) + int(end_parts[1])
        
        duration_hour = (end_total_minutes - start_total_minutes) / 60 
        
        if duration_hour <= 0:
            print("Error : End time must be after the start time. Please enter valid time slot.")
            return
        
        total_price = duration_hour * turf.price_per_hour
        
        print(f"\nBooking Duration : {duration_hour} hours")
        print(f"Total amount due : {total_price} Tk.")
        
        final_time_slot = f"{start_time} - {end_time}"
        
        new_booking = Booking(b_id , t_id , c_name , phone_number , date , final_time_slot, total_price)
        self.booking_list.append(new_booking)
        
        print("\nBooking added successfully !!!")
        
        
    def view_all_bookings(self):
        
        print("\n---> All Bookings <---")
        
        if len(self.booking_list) == 0:
            print("No bookings found.")
            return
        
        for booking in self.booking_list:
            booking.display_info()
            
            
    def search_booking_by_phone_number(self):
        
        print("\n---> Search Booking by phone number <---")
        
        if len(self.booking_list) == 0:
            print("No bookings found.")
            return
        
        phone_search = self.get_valid_text_input("Enter phone number to search :")
        
        found = False 
        
        for book in self.booking_list:
            if book.phone_number == phone_search:
                print("\nBooking found :")
                book.display_info()
                found = True
                return
        if not found:
            print("No booking found with this phone number.")
        



    def save_bookings(self):
        
        with open ("Booking.csv" , mode = "w" , newline = "") as file :
            
            writer = csv.writer(file)
            
            for booking in self.booking_list:
                writer.writerow([booking.booking_id , booking.turf_id , booking.customer_name , booking.phone_number , booking.date , booking.time_slot, booking.total_price])
                
    def load_bookings(self):
        try :
            with open ("Booking.csv" , mode = "r") as file :
                reader = csv.reader(file)
                
                for row in reader :
                    if len(row) == 7:
                        booking_id = row[0]
                        turf_id = row[1]
                        customer_name = row[2]  
                        phone_number = row[3]
                        date = row[4]
                        time_slot = row[5]
                        total_price = float(row[6])

                        loaded_booking = Booking(booking_id , turf_id , customer_name , phone_number , date , time_slot, total_price)
                        self.booking_list.append(loaded_booking)
                        
        except FileNotFoundError:
            pass
