# inherits via depth first then breadth, that is the order
# child <-- parent(s) <-- grandparent(s)
# all parents are searched first

class A(object):
    def do_this(self):
        print('doing this in A')


class B(A):
    pass


class C(A):
    def do_this(self):
        print('doing this in C')


class D(B, C):
    pass


# show inheritance order
# D <-- B and C <-- A <--- object
print(D.mro())
