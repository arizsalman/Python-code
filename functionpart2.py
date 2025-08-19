

# def my_func(value):
#     return value

# print(my_func("Python"))


# def my_func(value):
#     return "Hello World"


# print(my_func("Python"))


# def double(num):
#     return num**2


# do = double(10)
# print(do)


# def atob(a, b):
#     return (a + b)


# ab = atob(7, 3)
# print(ab)


# def check_even(number):
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"


# ch = check_even(3)
# print(ch)


def adu(year):
    if af > 18:
        return f' Your are Adult and your age is: {year}'
    else:
        return f"you are Minor and your age is {year}"


af = int(input('Enter a Birth Day '))
ad = adu({af})
print(ad)


def alpha(a, b):
    return (a+b, a-b, a*b)


multy = alpha(3, 3)
add, sub, mul = multy
print(add, sub, mul)  # ye list me show ho gaya
print(f'{add}, {sub}, {mul}')  # ye list me show ho gaya
print(multy)  # ye tuple me show ho ga ya


def read(names, age):
    return (f'My Name is {names}, My age is {age}')


red = read(names="Ariz", age=24)  # Ye best Taarka he
red1 = read("Ariz", 24)  # Ye bhe atrkeqa he ye best nahe he
print(red)
print(red1)
