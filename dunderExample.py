class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        } 

    ## In general you don't want to manipulate the Dunder Methods UNLESS you want the method to work a certian way
    def __str__(self):
        return f"{self.color}"
    
    def __len__(self):
        return 5
    
    # def __del__(self):
    #     print('deleted!') 
    
    # call gives toy class some superpower
    def __call__(self):
        return('yess??')

    def __getitem__(self, i):
        return self.my_dict[i]

# to view the difference: once with __str__(self) and one without
action_figure = Toy( 'red', 0 )

print( action_figure.__str__() )
print( str(action_figure) )
# print( str('action_figure') )
print( len(action_figure) )
# to display __del__(self)  uncomment both below and above __del__
# del action_figure
print( action_figure['name'] )
