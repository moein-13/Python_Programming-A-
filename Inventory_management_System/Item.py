class Item:

    def __init__(self, item_id , name , category , price , quantity):
        self.item_id = item_id
        self.name = name
        self.category = category

        self.__price = price
        self.__quantity = quantity

    # get method to read our safe private data

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    # setter method to update price with the safe way .

    def update_price(self , new_price):
        if new_price >= 0 :
            self.__price = new_price

            print(f"Price for {self.name} updated to {self.__price}")
        else:
            print("Error : Price cannot be negative.")

    def add_stock(self , item):
        if item > 0 :
            self.__quantity += item
            print(f"Added {item} units. New total : {self.__quantity}.")

    def sell_item(self, item):
        if item > 0 and item <= self.__quantity:
            self.__quantity -= item
            print (f"Sold {item} units. Remaining {self.__quantity}.")
        else :
            print("Error: Invalid sale item and not enough stock.")

    def display_info(self):
        print(f"ID : {self.item_id} | Name : {self.name} | Category : {self.category} | Price : {self.__price} TK | Stock : {self.__quantity} kg.")