class Flyer:
    def action(self):
        print('Flying')


class Swimmer:
    def action(self):
        print('Swimming')


class Duck(Flyer, Swimmer):
    pass


d = Duck()
d.action()  # is me phela vala call ho Flyer kun ke Duck(1.phele ,2 bad me)
print(Duck.mro())


class Duck2(Flyer, Swimmer):
    def action(self):
        Flyer.action(self)
        Swimmer.action(self)


d2 = Duck2()
d2.action() # ye bhe tareqa he Call kar vane ka 
Duck2().action() # ye bhe tareqa he Call kar vane ka
