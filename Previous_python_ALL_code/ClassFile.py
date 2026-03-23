class ClassFile ( object ):

    def__init__(self, name , id):
       self.name = name
       self.id = id

    def display ( self):
        print (self.name)
        print(self.id)

    def details ( self ):

        print("My name is : {}".format(self.name))
        print("Id is : {}".format(self.id))
        
