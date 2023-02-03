# list - is something built-in
class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList();


print(" ")
print( len(super_list1) )
# if we did not pass in list thru SuperList - it would throw error
super_list1.append(5)
print( super_list1[0] )
print( issubclass( list, object ) )
