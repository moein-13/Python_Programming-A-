from Item import Item

class AgroInventorySystem:

    def __init__(self):
        self.inventory_list = []  # create an empty inventory list to store item objects
        self.load_data()
        
        
    # load data...
    
    def load_data(self):
        try:
            with open("inventory_data.txt" , "r") as file:
                
                for line in file:
                    data = line.strip().split(",")
                    
                    if len(data) == 5 :
                        item_id = data[0].strip()
                        name = data[1].strip()
                        category = data[2].strip()
                        price = float(data[3].strip())
                        quantity = float(data[4].strip())
                        
                        load_item = Item(item_id , name , category , price , quantity)
                        self.inventory_list.append(load_item)
                        
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No existing data found. Starting with an empty inventory.")
    
    
    
    # save data here..
    def save_data(self):
        with open ("inventory_data.txt" , "w") as file:
            for item in self.inventory_list:
                line = f"{item.item_id} , {item.name} , {item.category},{item.get_price()} , {item.get_quantity()}\n"
                file.write(line)
                print("\n All the data saved successfully.")
                
                
    # prompt user for valid input.. 
    # for text input validation.
    def get_valid_text(self , prompt):
        while True:
            user_input = input(prompt).strip()

            if user_input == "":
                print(">> Error : you can not leave this blank.Please try again.")
            elif user_input.isdigit():
                print("Error : we need text here , not just number . Try again.")
            else:
                return user_input
            
# for number input validaton 
    def get_valid_number(self, prompt):

        while True:
            user_input = input(prompt).strip()

            if user_input == "":
                print(">>Error : you can not leave it blank. Try valid input .")
                continue

            try:
                value = float(user_input)
                if value < 0 :
                    print("value can not be negative.Try valid input.")
                else:
                    return value
            except ValueError:
                print(">> Error: Please enter a vlaid digits , not text or anything else.")
    
    # ADD new item to inventory method
    def add_new_item(self):

        print("\n --- ADD a New Product ---")

        new_id = self.get_valid_text("Enter Item id (e.g. , CROP-01): ")
        new_name = self.get_valid_text("Enter Item name (e.g. , Tomato) : ")
        new_category = self.get_valid_text("Enter a category :")
        new_price = self.get_valid_number("Enter a price for item (in TK) :")
        new_quantity = self.get_valid_number("Enter initial quantiry (in kg) :")

        new_item = Item(item_id = new_id,
                        name = new_name,
                        category = new_category,
                        price = new_price,
                        quantity = new_quantity
                        )
        self.inventory_list.append(new_item)
        print(f"\nSuccess : {new_name} has been added to the inventory.")
        

    # Viwe inventory item details
    def view_inventory(self):
        print("\n --- Current Inventory ---")
        
        if len(self.inventory_list) == 0:
            print("The inventory is currently empty . Please add item.")
        else:
            for item in self.inventory_list:
                item.display_info()
                
                
    # finder item by id method 
    def find_item_by_id (self, target_item_id : str):
        
        for item in self.inventory_list:
            if item.item_id == target_item_id:
                return item
        return None
    
    
    # Update item price
    def update_item(self):
        print("-- Update item information -- ")
        
        target_id = self.get_valid_text("Enter the item Id to update : ")
        # found_item is the search engine to find the item by id .
        found_item = self.find_item_by_id(target_id)
        
        if found_item:
            print(f"\nItem found : {found_item.name} | Current Price : {found_item.get_price()} TK")
            
            print("1. Update Price")
            print("2. Update Stock")
            print("3. Back to Main Menu")
            
            choice = input("Enter your choice (1-3) : ").strip()
            
            if choice == '1':
                new_price = self.get_valid_number(f"Enter new price (current price is {found_item.get_price()} TK) ")
                found_item.update_price(new_price)
            elif choice == '2':
                extra_stock = self.get_valid_number(f"Enter stock to add ( current stock is {found_item.get_quantity()} kg)")
                found_item.add_stock(extra_stock)
                
            elif choice == '3':
                print("Returning to main menu.")
                
            else:
                print("Invalid choice. Returning to main menu.")
        else:
            print(f"Error : No item found with ID {target_id}. Please try again.")
            
    # Remove an item from inventory
    def remove_item(self):
        
        print("-- Remove an Item from Inventory -- ")
        
        target_id = self.get_valid_text("Enter the item Id to remove : ")
        found_item = self.find_item_by_id(target_id)
        
        if found_item:
            self.inventory_list.remove(found_item)
            print(f"Success : {found_item.name} has been removed from the inventory.")
        else:
            print(f"Error : No item found with ID {target_id}. Please try again.")
            

                
    # --- The main menu engine ---
    
    def main_menu(self):
        
        while True:
            print("\n" + "="* 30 )
            print("--Agro Inventory System Menu--")
            print("="* 30)
            print("1. Add a new Item ")
            print("2. View Inventory ")
            print("3. Update Item Price ")
            print("4. Remove an Item ")
            print("0. Exit ")
            print("="* 30)
            
            choice = input ("Enter your choice (0-4) : ").strip()
            
            if choice == '1':
                self.add_new_item()
            elif choice =='2':
                self.view_inventory()
            elif choice == '3':
                self.update_item()
            elif choice =='4':
                self.remove_item()
            elif choice == '0':
                self.save_data()
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 0 and 4.")

if __name__ == "__main__":
    my_agro_system = AgroInventorySystem()
    my_agro_system.main_menu()
    
