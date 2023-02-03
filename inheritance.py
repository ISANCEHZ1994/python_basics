# remember everything in Python is an object we can examine
class User:
    # def __init__(self, email):
    #     self.email = email
    def sign_in(self):
        print('logged in')
        return "so it doesnt return 'None'"

class Wizard(User):
    def __init__(self, name, power): #email):
        # User - passing the email - which is why we can use it all the way below
        # Instead of using User we can use super() which is the superClass above
        # super() is a new addition as of Python 2.2 and we also don't need (self)
        # User.__init__(self, email)
        # super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name        
        self.num_arrows = num_arrows
 
    def check_arrows(self):
        print(f"{self.num_arrows} remaining")
    
    def run(self):
        print('ran really fast')

# Muiltiple Inheritance
class HybridBorg(Wizard, Archer):    
        def __init__(self, name, power, arrows):
            Archer.__init__(self, name, arrows)
            Wizard.__init__(self, name, power)    

# Any time you instantiate - the __init__ will always run!
# wizard1 = Wizard()
# print(wizard1)
# print(wizard1.sign_in())

# wizard2 = Wizard('Merlin', 50)
# wizard2.attack()
# archer1 = Archer('Robin', 100)
# archer1.attack()

# <== [ Python gives a tool that checks if something is an INSTANCE of something ] ===>
# isinstance(<INSTANCE>, <CLASS>)
# wizard3 = Wizard("Harry", 51)
# print(isinstance(wizard3, User)) # <== User also works because Wizard is a SUBCLASS of User 

# <=== [ will return the length of string ] ===>
# for char in [ wizard2, archer1 ]:
#     char.attack()

# <=== [ Learning about self() ] ===>
# Introspection - the ability to determine the type of an object at runtime
# wizard1 = Wizard("Merlin", 60, "merlin@gamil.com")
# print(wizard1.email)
# dir() - will return all the methods and atrributes that the Wizard instant has - BEHOLD THE DUNDERS
# very useful when you're tyring to figure out what you have access to
# print(dir(wizard1))

# Since hb1 has muiltiple Inheritances you can use all methods from Wizard and Archer
# Note: had to remove some arguments and methods to make below work!
hb1 = HybridBorg('borgie', 50, 100)
print(hb1.run())
# so we inherit by position of arguments of that class so if wizard is first THEN Archer
# THIS will still be an error => AttributeError: 'HybridBorg' object has no attribute 'num_arrows'
# To make it work we need to init HybridBorg() as well as pass the other argument
print(hb1.check_arrows()) 
print(hb1.attack())
print(hb1.sign_in())

