row = int(input("How many rows??"))
col = int(input("How many col??"))

symbol = input("enter a symbol that U want to use :")

for i in range(row):
    for j in range(col):
        print(symbol, end=" ")
    print()