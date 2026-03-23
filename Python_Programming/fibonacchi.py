
'''   # Fibonacci number
a , b = 0 ,  1

while a < 100:
    print(a)
    a , b = b , a+b

    '''

                         #  ---  if else practice.   ---
'''                practice - 1 

words = ['cat', 'window', 'situations']

for w in words:
    print(w , "& length is -", len(w))
'''
'''
                   # Practice - 2

a = ['Mary', 'had', 'a', 'little', 'lamp']

for i in range(len(a)):
    print(i , a[i])  
'''
'''                   # Practice - 3
                  # break and continue statements

for n in range(2 , 10):
    for x in range(2 , n ):
        if n % x == 0:
            print(f"{n} equals to {x}*{n // x}")
            break
             # without using break output we see 6 equals to 2 * 3 
             #   and 6 equals to 3 * 2 . But with break we only see
             #   6 equals to 2 * 3 .
'''

'''           # for Continue

for i in range(-2, 10):
if i % 2 == 0 :
print(f"Found an even number {i}")
continue
else:
print(f"Found an odd number{i}")

'''
'''    with prime number.
for n in range ( 2 , 10 ):
    for x in range (2 , n ):
        if n% x == 0 :
            print(f"{n} equals to {x}*{n//x}")
            break
    else:
        print(f"{n} is a prime number.")

'''

'''         # --->  match statements  <---
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I am a teapot"
        case _:
            return "Something worng with the internet."

print(http_error(404))

from dataclasses import dataclass
@dataclass
class Point:
    x : int
    y : int

def where_is(P):
    match P:
        case Point(x = 0 , y = 0):
            print("Origin")
        case Point(x = 0 , y = y):
            print(f"Y = {y}")
        case Point(x = x , y = 0):
            print(f"X= {x}")
        case Point():
            print("Somewhere else.")
        case _:
            print("Not a point")

where_is(( 0, 0))

 
 


##print("Mominul Islam Moein")

def fib(n):
    result = []
    a , b = 0 , 1
    while a < n:
        result.append(a)
        a , b = b , a+b
    return result
fibonacci = fib(100)
print(fibonacci)
'''

def ask_ok( prompt , retries = 4 , reminder = "Please try again!"):

    while True:
        
        reply = input(prompt).lower().strip()

        if reply in {'y', "ye", "yes"}:
            return True
        if reply in {"n", "no", "nop", "nope"}:
            return False
        retries -= 1
        if retries < 0 :
            raise ValueError("invalid user response")
        print(reminder)
try:

    results = ask_ok("Do you really want to quit ?(y/n) : ")
    print(results)
    
except ValueError:
    print("You have exhausted all your tries.!!!")







