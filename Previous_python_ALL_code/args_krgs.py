
def add_number(*args):

    print(f"the args is a tuple {args}")
    print(f"Type: {type(args)}")

    total = 0 
    for i in args:
        total += i
    return total

print(add_number(1,2,3)) 



    



