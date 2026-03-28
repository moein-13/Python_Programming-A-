from Turf import TurfManager
from Booking_manager import BookingManager


def get_valid_menu_choice(prompt):
            while True :
                user_input = input(prompt).strip()
                if user_input == "":
                    print("Input can not be blank . Please enter a valid input.")
                elif not user_input.isdigit():
                    print("Input must be a number . Please enter a valid number .") 
                else:
                    choice = int(user_input)
                    if 1 <= choice <= 8:
                        return choice
                    else:
                        print("Invalid choice . Please enter a number between 1 and 8.")
def main() :
    
    my_turf_manager = TurfManager()
    my_booking_manager = BookingManager()
    
    print ("Loading Systeem data .!!!")
    my_turf_manager.load_turfs()
    my_booking_manager.load_bookings()
    print ("Data loaded successfully.!!!")
    
    
    while True:
        print("\n--- T U R F    M A N A G E M E N T   S Y S T E M --- ")
        
        print ()
        print("1. Add a new turf ")
        print("2. View all turfs")
        print("3. Update Turf Information")
        print("4. Delete a turf")
        print("5. Create a new booking ")
        print("6. View all bookings ")
        print("7. Search booking by Phone number ")
        print("8. Exit Program")
        
        choice = get_valid_menu_choice("Enter your choice (1-8) : ")    
        
        if choice == 1 :
            my_turf_manager.add_turf()
        elif choice == 2 :
            my_turf_manager.view_all_turfs()
        elif choice == 3 :
            my_turf_manager.update_turf()
        elif choice == 4 :
            my_turf_manager.delete_turf()
        elif choice == 5 :
            my_booking_manager.add_booking(my_turf_manager)
        elif choice == 6 :
            my_booking_manager.view_all_bookings()
        elif choice == 7 :
            my_booking_manager.search_booking_by_phone_number()
        elif choice == 8 :
            print("SAVING YOUR DATA")
            my_turf_manager.save_turfs()
            my_booking_manager.save_bookings()
            
            print("Exiting the program . Goodbye !")
            break
        else:
            print("Invalid choice . Please enter a number between 1 and 8.")
        
        
if __name__ == "__main__":
    main()