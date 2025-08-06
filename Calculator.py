# opar = ('!', "@", '$')
# print(type(opar))

Numb1 = int(input("please Write The   Number Only: "))
Numb2 = int(input("please Write The   Number Only: "))
ch_operation = input("please Choose The  operation (+, -, *, /): ")
a_num = Numb1+Numb2
m_num = Numb1-Numb2
s_num = Numb1*Numb2
d_num = Numb1/Numb2


def add(Num1, Num2):
    return (Num1+Num2)


def sub(Num1, Num2):
    return (Num1-Num2)


def div(Num1, Num2):
    return (Num1/Num2)


def multy(Num1, Num2):
    return (Num1*Num2)


if ch_operation == "+":
    add(Numb1, Numb2)
    print(a_num)
elif ch_operation == "-":
    sub(Numb1, Numb2)
    print(a_num)
elif ch_operation == "*":
    div(Numb1, Numb2)
    print(m_num)

elif ch_operation == "/":
    multy(Numb1, Numb2)
    print(d_num)
