foods = []
prices = []
total = 0

while True :
    food = input("Enter a food to buy (q to quite) :")

    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter a valid price of this {food} $"))

        foods.append(food)
        prices.append(price)

print("____Your Cart____")

for food in foods:

    print(food , end =" ")
for price in prices:

    total += price
print()
print(f"Your total is : ${total}")