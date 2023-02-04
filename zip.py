#zip()

my_list = [ 1, 2 ,3 ];
your_list = [ 10, 20, 30 ];
your_list2 = ( 10, 20, 30 );
their_list = [ 5, 6, 7 ]

def multiply_by2(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

# it all depends on ORDER
print(list(zip(their_list, my_list, your_list)))  # [(1, 10), (2, 20), (3, 30)] => now changed to [(5, 1, 10), (6, 2, 20), (7, 3, 30)]
print(list(zip(my_list, your_list2, their_list))) # should look the same as above! even with paraenthesis 
# might not look important now - think about - two collections of data and we need to combine them into a temple