

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


# def adu(year):
#     if af > 18:
#         return f' Your are Adult and your age is: {year}'
#     else:
#         return f"you are Minor and your age is {year}"


# af = int(input('Enter a Birth Day '))
# ad = adu({af})
# print(ad)


# def alpha(a, b):
#     return (a+b, a-b, a*b)


# multy = alpha(3, 3)
# add, sub, mul = multy
# print(add, sub, mul)  # ye list me show ho gaya
# print(f'{add}, {sub}, {mul}')  # ye list me show ho gaya
# print(multy)  # ye tuple me show ho ga ya


def read(names, age):
    return (f'My Name is {names}, My age is {age}')


red = read(names="Ariz", age=24)  # Ye best Taarka he
red1 = read("Ariz", 24)  # Ye bhe atrkeqa he ye best nahe he
print(red)
print(red1)

'''Agar hum function ke ander  gobal value ko used karna cahe tu {global} ka keyword used kare gae'''

# count = 0


# def global_Count():
#     global count
#     count = +1


# global_Count()
# print(count)


# def prime(nump):
#     for i in range(2, nump):
#         if nump % i == 0:
#             return f' Number is not prime number {nump}'

#         else:
#             return f' The Prime number is {nump}'


# nur = int(input("Enter your number "))
# pN = prime(nur)
# print(pN)


def primes(nums):
    if nums < 2:
        return f'Prime Number is Greater than {nums} '
    for i in range(2, (int(nums**0.5)+1)):
        if nums % i == 0:
            return f' Not a Prime Number : {nums}'
    return f' Your number is a Prime number {nums}'


nus = int(input('Enter your number and see its a prime number is not '))
p_N = primes(nus)
print(p_N)
