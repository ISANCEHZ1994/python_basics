#zip()

my_list = [ 1, 2 ,3 ];
your_list = [ 10, 20, 30 ];
your_list2 = ( 10, 20, 30 );

def multiply_by2(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

print(list(zip(my_list, your_list)))  # [(1, 10), (2, 20), (3, 30)]
print(list(zip(my_list, your_list2))) # should look the same as above! even with paraenthesis 
