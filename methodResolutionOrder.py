# MRO - Method Resolution Order
class A:
    num = 10

class B( A ):
    pass

class C( A ):
    num = 1

class D( B, C ):
    pass

print(D.num) # would still show 1
print(D.mro()) # will reveil the ORDER of classes 
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
D.__str__
