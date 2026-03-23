                # Doubled of the numbers using for loops.

numbers = [12,13,14]
doubled = [x * 2 for x in numbers]
print(doubled)
                # Square of the numbers using for loops

numbers = [2,3,4,5,6]
sqr = [x ** 2 for x in numbers]
print(sqr)

                 # Even list usig list comprehensiion

list = [i for i in range(20) if i % 2 == 0]
print("\nThe even number list is :" , list)


