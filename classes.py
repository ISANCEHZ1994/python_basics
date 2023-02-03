# OOP in PYTHON
# note: since Python is similar to Ruby/Rails - functions are called methods

# self represents the instance of the class. 
# By using the “self”  we can access the attributes and methods of the class in python. 
# It binds the attributes with the given arguments - we need them for the methods to work
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    # __init__ is the CONSTRUCTOR!!
    # we can already have default setting inside the arguments - in case there are no changes to the name
    def __init__(self, name = "anonymous", age = 0):
        # in Python below is called ATTRIBUTES
        # if( self.membership ):
        if( age > 18 ):
            self.name = name
            self.age = age
    
    def run(self):
        print('run')
        print("something else here!")
        ### note: if there is no 'return' it'll return `None` 
        # check what happens below when you use shout()
        return 'done'
         
    def shout(self):
        ## I believe the f represents that something needs to be added and thus we add whatever is passed thru the methods
        print(f'my name is {self.name}')

    # when using classmethod we must pass cls like how we pass self for previous methods
    # we can use this WITHOUT INSTANTIATING a class
    @classmethod
    def adding_things( cls, num1,num2 ):
        # return  cls('Teddy', num1 + num2) # here is how we can still instantiate if we would need to using cls() - print shows the class in memory
        return num1 + num2

    #  does about the same as classmethod however we CANNOT use cls() nor pass it thru
    @staticmethod
    def addingThings(num1, num2):
        return num1 + num2

player1 = PlayerCharacter("israel", 28)
player2 = PlayerCharacter("Valeria", 21)

# print(player1.shout())
# print("  ")
# print(player1.name, player1.age)
# print(player2.name, player2.age)
# print("  ")
# print(player1.run())
# print("  ")
# print(player1.membership)
# print(player2.membership) 
print("  ")
# since we created a classmethod we dont need to instantiate we can just use it!

print(player1.adding_things(2,3) )
print(PlayerCharacter.adding_things(2,3)) # see here..
# note that we are now using the staticmethod NOT classmethod
player3 = PlayerCharacter.addingThings(2,3)
print(player3)
# player.run
