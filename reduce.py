# reduce - all items in array will be added/combined

from functools import reduce

my_list = [ 1, 2 ,3 ];
your_list = [ 10, 20, 30 ];
your_list2 = ( 10, 20, 30 );
their_list = [ 5, 6, 7 ];

def accumulator( acc, item ):
    print( acc, item )
    # first  time thru: acc = 0, item = 1  (0 + 1 = 1) 
    # second time thru: acc = 1, item = 2 (1 + 2 = 3)
    # third  time thru: acc = 3, item = 3  (3 + 3 = 6)
    return acc + item

print( reduce( accumulator, my_list, 0 )) 


