# Inheritance 4 type ke he
# Single inheritance.(Ek child apne parent se  [inherit mean koe jes lena ] )
# Multiple inheritance.(Ek child multiple parent se inter kere.)
# Multilevel Inheritance → Parent → Child → Grandchild.
# Hierarchical Inheritance → Ek parent ke multiple children
# Hybrid Inheritance → Inka combination.

# Single Inheritance without consturcture


# class Animal:
#     kind = "generic"

#     def speak(self):
#         print('...(silence)')


# class Dog(Animal):
#     print('Bao')


# d = Dog()
# print(d.kind)
# d.speak()


# class Cat(Animal):
#     def speak(self):
#         print('Meow')


# c = Cat()
# c.speak()


# class Parrot(Animal):
#     def speak(self):
#         super().speak()
#         print("squawk")


# p = Parrot()
# p.speak()


class Myfather:
    def home(self):
        print('my Home')


class BigBro(Myfather):
    def home(self):
        super().home()
        print("My Father Home ")


class ElderBro(BigBro):
    def home(self):
        super().home()
        print('Elder brother home')


e = ElderBro()
e.home()
