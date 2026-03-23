"""
def say_hi():     # this is called def function
    print("Hey mate")

say_hi()          # in the main function we call the function then we can find the output.


def user(name):
    print("Hi "+name)

user("Moein")
user("DM")
user("Xarif")

def cube (num):

    return num * num + num
##print(cube(3))
result = cube (3)

print(result)



def Mk():
    print("kya re",n," chilke ?")

n = "rakib"

Mk()
print("kaisa chal raha hai re",n)

def f():
    global s

    s+="Moein"
    print(s)

    s = "Hope we never be meet again"



s = "This is really soute on U "

f()
print(s)





a = 1
def f():
    global a
    a= 2

    print("Inside f() : ", a)
def g():
    global a
    a = 3
    print("Inside g() : ",a)
def h():
    global a
    a = 4
    print("Inside h() : " ,a)
def i():
    global a
    a = 5
    print("Inside i() : ", a)



print("global : ",a)
f()
print("global : ",a)
g()
print("global : ",a)
h()
print("global : ",a)
i()



def add(a , b):
    return a + b
def is_true (a):
    return bool(a)


result = add(2,3)
print("the result is {}".format(result))
res = is_true(6<5)
print("\nthe result of is_true is {}".format(is_true(res)))


def fun ():
    str = "hey its moein"
    x = 21
    return  str , x
str , x = fun()
print(str)
print(x)




for i in range(100 , 0 , -5):
    print(i,end=" ")
print()

"""













