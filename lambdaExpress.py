# Lambda Expressions are a one time anonymous functions that you don't need more than once
# Example: 
#       lambda <PARAM>: action(PARAM)

my_list = [ 1, 2,  3 ];

def multiply_by2(item):
    return item * 2

# remember that list() creates a list object - A list object is a collection which is ordered and changeable
print(list(map(multiply_by2, my_list)))
print('hello world');