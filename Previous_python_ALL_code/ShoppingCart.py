class ShoppingCart:
    def __init__ ( self , customer_name):
        self.customer_name = customer_name
        self.items = []
        self.total = 0

    def add_item(self , item_name , price , quantity= 1):
        item = {
            'name' : item_name,
            'price' : price,
            'quantity' : quantity
        }
        
        self.items.append(item)
        self.update_total()

        print(f"Added {quantity}x {item_name} to {self.customer_name}'s cart")

    def remove_item(self, item_name):
        for item in self.items:
            if item['name'] == item_name:
                self.items.remove(item)
                self.update_total()
                print(f"Removed {item_name} from cart.")
                return
            print(f"{item_name} not found in cart.")

    def update_total(self):

        self.total = sum(item['price'] * item['quantity'] for item in self.items)
    def show_cart(self):
        print(f"\n{self.customer_name}'s shopping cart.")
        if not self.items:
            print("Cart is empty.")

        else:
            for item in self.items:
                print(f"-->{item['name']} : ${item['price']} and quantity is {item['quantity']}x")

            print(f"Total : ${self.total : .2f}")

cart = ShoppingCart("Moein")
cart.add_item('Laptop' , 1000.10)
cart.add_item('Mouse', 70.00)
cart.add_item("Keyboard", 80.50)
cart.add_item('Bag' ,30.70)
#cart.show_cart()
cart.remove_item('Bag')
cart.show_cart()