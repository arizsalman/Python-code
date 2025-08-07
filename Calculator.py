# opar = ('!', "@", '$')
# print(type(opar))

# Numb1 = int(input("please Write The   Number Only: "))
# Numb2 = int(input("please Write The   Number Only: "))
# ch_operation = input("please Choose The  operation (+, -, *, /): ")
# a_num = Numb1+Numb2
# s_num = Numb1-Numb2
# m_num = Numb1*Numb2
# d_num = Numb1/Numb2


# def add(Num1, Num2):
#     return (Num1+Num2)


# def sub(Num1, Num2):
#     return (Num1-Num2)


# def div(Num1, Num2):
#     return (Num1/Num2)


# def multy(Num1, Num2):
#     return (Num1*Num2)


# if ch_operation == "+":
#     add(Numb1, Numb2)
#     print(a_num)
# elif ch_operation == "-":
#     sub(Numb1, Numb2)
#     print(s_num)
# elif ch_operation == "*":
#     div(Numb1, Numb2)
#     print(m_num)

# elif ch_operation == "/":
#     multy(Numb1, Numb2)
#     print(d_num)


Numb1 = int(input("please Write The   Number Only: "))
Numb2 = int(input("please Write The   Number Only: "))
ch_operation = input("please Choose The  operation (+, -, *, /): ")


def add(Numb1, Numb2):
    return (Numb1+Numb2)

# print(add(Numb1, Numb2))

def sub(Numb1, Numb2):
    return (Numb1-Numb2)

# print(sub(Numb1, Numb2))

def div(Numb1, Numb2):
    return (Numb1/Numb2)

# print(div(Numb1, Numb2))

def multy(Numb1, Numb2):
    return (Numb1*Numb2)

# print(multy(Numb1, Numb2))  # Agar hum is ko an comment kaer ge  not best Beavier

if ch_operation == "+":
    print('Result ', add(Numb1, Numb2))

elif ch_operation == "-":
    print('Result ', sub(Numb1, Numb2))

elif ch_operation == "*":
    print('Result ', multy(Numb1, Numb2))

elif ch_operation == "/":
    print('Result ', div(Numb1, Numb2))
else:
    print("Invalid operation.")
