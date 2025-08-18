# Dictionary ka kabh bhe Original  structure  kabhe bhe change nahe hota
# agar ap ko change karna he tu ap   formating string  se kar shate ho .[Magar vo at the time he ho ga dictionary me change nah ho ga bas vo reqiurment pure karne ke leye formating string me kar raha he]
#  items () ye dictionary ke key or value ko tuple form me deta he or  kio argument accept nahe karta
# Main key .join()
# join() sirf string iterables ke sath kaam karta hai.
# Join () sirf key pe kam karta he value pe nahe
# Iterable vo python ka vo object he jis me hum loop chala sakte he
# repr() ye object ko string ke from me concert karta he ye developer-oriented hota he
# detail = {
#     'name': 'Ariz',
#     'age': 23
# }
# print(" ,".join(f" {repr(k)}:{repr(v)}" for k, v in detail.items()))

""" is ka ouput yehe  name,age...why because ye samjta he jab hum dictionary ko direct pass karte he tu python key ko iterable samjta he..
# or jab  hum dictionary ko directly  iterate ya acces karte he tu python  ye samjta he ke key as a iterable he is ko he show kara do""" "ye multi line  commit ky=hlata he"
# print(','.join(detail))
# # print(detail)
# print(list(detail))
# print(len(detail))
# print(detail)
# detail['name'] = 'Ariz Salman'
# print(detail)

# detail.update([("'name", 'ARIZ')]) # or us function key assces he nahe
# kar rahe ho tu vo new [key create ker de ge ]
# detail.update([("name", 'ARIZ')])
# detail.update([("age", 24)])


# sub = {
#     'name': 'Python',
#     'codaeter': 'Vs'
# }

# print(sub.items())
# print(f'{repr(k)}:{repr(v)}'for k, v in sub.items())
# print(",".join(f"{repr(k)}:{repr(v)}"for k, v in sub.items()))


# student = {
#     102: 'Ali',
#     103: 'Muhammad Ariz',
#     104: 'Umer'
# }
# student.update([(102, 'MuhammadALI')])
# student[104] = 'MuhammadUmer'
# print(student[104])
# print(student)
# print(','.join(f'{repr(k)}:{repr(v)}' for k, v in student.items()))
# print(student)
# print(student[102])


# student2 = {
#     'name': 'Ali',
#     'fname': 'Muhammad Ariz',
#     'sname': 'Umer'
# }
# student2.pop('name')
# print(student2)
# for key in student2:
#     print(key)

# for value in student2:
#     print(f'This is {value}')

# for key, value in student2.items():
#     print(f' This is key {key} and This value  is : {value} ')


# student3 = {"name": "Ariz", "age": 20}
# print(student3.keys())      # dict_keys(['name', 'age'])
# print(student3.values())    # dict_values(['Ariz', 20])
# print(student3.items())     # (key, value) pairs return karta hai
# print(student3.pop("age"))#dict_pop Key delete karke value return karta hi
# print(student3.get("age")) #Safe value return (error nahi deta)

# nested dictionary
# student7 = {
#     101: {'name': "Ali", "age": 23},
#     102: {'name': "Areesh", "age": 25},
#     103: {'name': "Aashir", "age": 29}
# }

# for data in student7.values():
#     data.update([("coures", 'Python')])
# for roll, detail in student7.items():
#     detail_i = ",".join(f"{repr(k)}:{repr(v)}" for k, v in detail.items())
#     print(f"{roll}->{detail_i}")
# print(','.join(f"{repr(k)}:{repr(v)}"for k, v in student7.items()))
# print(student7)
# print(list(student7))


# numi = {x: x**2 for x in range(1, 6)}
# print(numi)


# # Ek dictionary banao jisme roll numbers keys ho aur names values. Fir user se roll number lo aur uska naam print karo.
# studentr = {
#     101: 'Ariz',
#     102: 'Areesh',
#     103: 'Babar',
#     104: 'Farhan',
#     105: 'Furkan'
# }

# for roll, namest in studentr.items():

#     print(f'{roll}=> {namest}')


# user = int(input("Please Enter your Roll Number "))
# if user in studentr:
#     print(f'your Roll Number id {user} and your Name is {studentr[user]}')
# else:
#     print(f'Please enter the Valaid roll number Roll Number is Not found ')

# student_Ins = {
#     101: {"name": "Ariz", "age": 24},
#     102: 'Areesh',
#     103: {"name": 'Babar', "age": 12},
#     104: 'Farhan',

# }

# for roll, str in student_Ins.items():
#     if isinstance(str, dict):
#         student_Detail = ",".join(
#             f"{repr(k)}:{repr(v)}" for k, v in str.items())
#         print(f'{roll} => {student_Detail}')
#     else:
#         print(f" {roll} => {str}")


studentsn = {
    101: {"name": "Ariz", "age": 20},
    "102": "Babar",
    103: 25,
    "104": 3.14,
    "105": True,
    "106":  [1, 2, 3],
    "107":  [(1, 2), (2, 8)]
}

for roll, value in studentsn.items():
    if isinstance(roll, int):
        print(f'your key  Roll number is: {roll}')
    elif isinstance(roll, str):
        print(f'Your Value is  string :{roll}')
    if isinstance(value, dict):
        stu_de = ",".join(f"{repr(k)}:{repr(v)}"for k, v in studentsn.items())
        print(f'Value is Dictionary is : {stu_de}')
    elif isinstance(value, str):
        print(f'Value in Dictionary is {value}')
    elif isinstance(value, int):
        print(f' Value in Dictionary is {value}')
    elif isinstance(value, float):
        print(f'Value is Dictionary is {value}')
    else:
        print(f'Your Dictionary value is Unkown->{value}')
