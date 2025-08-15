class Shapes:
    def squre(self):
        print(' This is my onw sqare')


class Cirule(Shapes):
    def squre(self):
        print('There is Box')


class SC(Cirule):
    def squre(self):
        print('Two in one')


Cirule().squre()
SC().squre()
