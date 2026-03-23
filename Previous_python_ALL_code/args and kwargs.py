

            # using of *args in function :

"""
def fun (arg1,*argv):
    print("First element is :",arg1)
    for i in argv:
        print("Next elements are :",argv)

fun('hello','moein','do','you','agree','or','not')


def myfun (arg):
    print("\nthe print is :",arg)

args = ('hello', 'Moein')

myfun(*args)





           # using of **kwargs in function

def fine(**kwargs):

    for key , values in kwargs.items():
        print("%s == %s" % (key,values))

fine(first = 'Mominul', mid = 'islam', last ='Moein')

"""

def mifan(*args , **kwargs):
    print("Args = ", args)
    print("Kwargs =", kwargs)

mifan('geeks','for','geeks',first = "Geeks",mid = "For",last ="Geeks")



