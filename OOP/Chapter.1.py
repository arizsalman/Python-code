# class Chapter:
#     def __init__(self, ChpName, Topic):
#         self.chpName = ChpName
#         self.Topic = Topic


# myChapter = Chapter("Python", "OOP")
# print(myChapter.chpName)
# print(myChapter.Topic)

# myNewChapter = Chapter('React', 'Function')
# print(myNewChapter.Topic)


# class Car:
#     def __init__(self, Name, Modal):
#         self.Name = Name
#         self.Modal = Modal


# myCar = Car('Toyota', 'Carolla')
# print(myCar.Name)
# print(myCar.Modal)


# class Family:
#     def __init__(self, fullName, FaName):
#         self.fuName = fullName
#         self.FaName = FaName

#     def Full_Family(self):
#         return f'{self.fuName} {self.FaName}'


# myFamily = Family('Ariz', 'Salman')
# print(myFamily.fuName)
# print(myFamily.FaName)
# print(myFamily.Full_Family())


# class OurColor:
#     def __init__(self, color1, color2):
#         self.color1 = color1
#         self.color2 = color2

#     def Newcolor(self):
#         return f'{self.color1}  {self.color2}'


# OwnColor = OurColor('Bule', 'Yellow')
# print(OwnColor.color1)
# print(OwnColor.color2)
# print(OwnColor.Newcolor())


# class Myform:
#     def __init__(self, form1, form2, form3):
#         self.form1 = form1
#         self.form2 = form2
#         self.form3 = form3

#     def MargeForm(self):
#         return f'{self.form1} {self.form3} {self.form2}'


# NewFrom = Myform('Hello Wrold', 'Hi there', 'Bye there')
# print(NewFrom.form1)
# print(NewFrom.form2)
# print(NewFrom.form3)
# print(NewFrom.MargeForm())


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def Display_info(self):
        return f' {self.brand} {self.model}'


class Eletric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def Display_info(self):
        return f'{super().Display_info()}with Battery_size .{self.battery_size}'


MyElectircCar = Eletric_Car('Tesla', 'Js17Sa', '100KHV')
print(MyElectircCar.Display_info())


MyCar = Car('Ferarri', 'E_Class')
print(MyCar.brand)
print(MyCar.model)
print(MyCar.Display_info())
