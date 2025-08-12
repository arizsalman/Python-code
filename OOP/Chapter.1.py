class Chapter:
    def __init__(self, ChpName, Topic):
        self.chpName = ChpName
        self.Topic = Topic


myChapter = Chapter("Python", "OOP")
print(myChapter.chpName)
print(myChapter.Topic)

myNewChapter = Chapter('React', 'Function')
print(myNewChapter.Topic)


class Car:
    def __init__(self, Name, Modal):
        self.Name = Name
        self.Modal = Modal


myCar = Car('Toyota', 'Carolla')
print(myCar.Name)
print(myCar.Modal)
