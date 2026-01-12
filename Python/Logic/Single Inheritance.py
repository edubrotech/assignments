##Single Inheritance
class A:
    def son(self):
        print('Rakesh')

class B:
    def son(self):
        print('shivansh')

class C(B,A):
    pass


d=C()

d.son()

