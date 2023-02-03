def multiply_by2( li ):
    new_list = []
    for item in li:
        new_list.append( item * 2 )
    return new_list

print(multiply_by2([ 1, 2, 3 ]))
print(map(multiply_by2, [1, 2, 3])) # you will only see where it is in memory

# map(action, data)
# map(multiply_by2, [1,2,3])
my_list = [1, 2, 3]
def better_multiply(item):
    return item * 2
# with map we no longer need to do what multiply_by2 - create an array [] - then loop
# list() function creates a list object.
print(list(map(better_multiply, my_list)))

