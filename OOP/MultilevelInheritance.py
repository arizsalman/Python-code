class A:
    def who(self):
        print('AZ')


class B(A):
    def who(self):
        print(f'B->', end="")
        super().who()


class C(B):
    pass


C().who()


class Father:
    def gift(self):
        print("This is my Car ")


class Fchild(Father):
    def gift(self):
        print('This is my dad Car ')
        super().gift()


class Husyar(Fchild):
    print("This is my car Only")
    pass


Husyar().gift()
