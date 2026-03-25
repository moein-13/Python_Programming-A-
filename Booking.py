class Booking :
    
    def __init__ (self , booking_id , turf_id , customer_name , phone_number , date , time_slot, total_price):
        
        self.booking_id = booking_id 
        self.turf_id = turf_id 
        self.customer_name = customer_name 
        self.phone_number = phone_number 
        self.date = date 
        self.time_slot = time_slot
        self.total_price = total_price
        
    def display_info(self):
        
        print(f"Booking Id : {self.booking_id} ")
        print(f"Turf Id : {self.turf_id} ")
        print(f"Customer : {self.customer_name} ")
        print(f"Phone Number : {self.phone_number} ")
        print(f"Date : {self.date} ")
        print(f"Time Slot : {self.time_slot} ")
        print(f"Total Price : {self.total_price} Tk. ")