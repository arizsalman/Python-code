
#  Function :A function is a  reusable block of code that performs a specific task. It can take inputs, process them, and return outputs.
# # chatGPT def :A function in Python is a block of reusable code that performs a specific task.

# # Functiion are two type
# {1 Type } Built-in Functions :ye Python ne already banaye hue hote hain ;
# Example : print(), len(), type(), input(), range()
#  name = input("Enter your name: ")  # built-in input function
# {2 Type}User-defined Functions (Hum khud banate hain)
# #  jo hum apni need ke mutabiq banate hain.


# def greet(name1):
#     print(f"Hello, {name1}!")


# greet("Ali")  # # # Output: Hello, Ali!


# def aname(fisrt_name, last_name):
#     print(f"hi{fisrt_name} {last_name}")
#     print('Welcome')


# aname(' Muhammad Ariz', 'Salman')


# def greet(name):
#     print(f' HI {name}')


# print(greet('Ariz'))  ## is tarqe se hum function ke value bata kerte he

# Function keyword arrgument


# def function(number, by):
#     return number+by


# print(function(15, by=5))  # {by is}Keyword arguments


# # ye {by jo value de rahe}is ko function ko default argument
# def function(number, by=5):
#     return number+by


# print(function(15))  # (15 ke bad value update kar sakte he )


# def function(num1, num2):
#     return (num1*num2)


# print(function(2, 5))

# def show(word):
#     print(len(word))


# show("GRADE JERNE OF CODE")


# def add(a, b):
#     return (a+b)


# def subt(e, r):
#     return (e-r)


# def mul(x, y):
#     return (x*y)


# print(add(20, 10))

# print(subt(10, 5))
# print(mul(2, 20))


# def add(num1):
#     return 20+30


# print(add(1))


# def add1(num1, num2):
#     return 10+100


# print(add1(2, 2))


# ni = int(input('enter your frist number'))
# nu = int(input('enter your second number'))


# def np(ni, nu):
#     return (ni+nu)


# print(np(ni, nu))


# numa = int(input("Enter the  First number"))
# numb = int(input("Enter the   Second number"))


# def sqr(numa, numb):
#     return (numa*numa, numb*numb)


# print(sqr(numa, numb))

# print(
#     f'The sum of Your  first number is {numa*numa}\n sum of second number is {numb*numb}')


# def great(name):
#     return ('Hello', name)


# print(great("Ariz"))


# def rev_Func():
#     print("Hello Ariz ! Welcome to python .")


# rev_Func()


# Function with Parameters
# def user_Name(name):

#     print(f'My name is {name}')


# user_Name(name="Ariz")
# """bohot sare parameter ho to ye best tareqa hi kam karne ka ."""
# user_Name('Babar')


# def add(a, b):
#     return (a+b)


# add(20, 30)
# """ ak ye bhe tareqa he kam karne ka """

# Function with Return Value


# def sum(a, b):
#     return (a + b)


# sumab = sum(20, 30)
# sum(20, 30)
# print("Sum is:", sumab)


# # Default Parameters
# def defualt(name="ariz"):
#     print(f'My Name is {name}')


# defualt()  # jab kyo function ko call kare without value to default method kam ata he
# defualt('Ali')  # Ye nromal condition he :


# Multiple Return Values
# def multi(a, b):
#     return a+b, a-b, a*b


# add_subt_multi = multi(10, 2)  # ye be tareqa he agar app ko tuple banahe
# add, sub, mul = add_subt_multi
# # multi(10, 2)  # ye be tareqa he
# # Dono ka same anwser he
# print(f' {add_subt_multi}')  # (12, 8, 20)
# print(f' {add},{sub},{mul}')  # 12,8,20
# print({add, sub, mul})
# print(*add_subt_multi, sep=", ")


# def calc(a, b):
#     return a+b, a-b, a*b


# sum_abc, diff, prod = calc(10, 5)
# print(sum_abc, diff, prod)


# def nam(name):
#     print(f"hi!{name}")


# b = nam('Ariz')
# print(b)


# def greet():
#     return "Hello Ariz!"


"""Agar tumhe function ka result sirf ek baar dikhana hai → direct print(greet()) use karo.
Agar tumhe function ka result baar-baar use karna hai (modify karna, store karna, condition lagana, etc.) → usse variable me save karo (msg = greet())."""

# ye best practice he function ko variable me save kar le na
# msg = greet()
# print(msg)
# print(msg.upper())
# # kam do nono karge best prctice uupper vale
# print(greet())  # ye practice galat he wrong term !
# print(greet().upper())


'''Ek function banao square(num) jo ek number lega aur uska square return karega.
👉 Tumhe bataana hai ke agar main print(square(5)) likhun to output kya hoga.'''


# def square(num):
#     return num**2


# squa = square(5)
# print(squa)


# def trip(e, f):
#     return (e*f)


# tr = trip(4, 6)
# print(tr)


# def trm(nus):
#     return nus**3


# tm = trm(3)
# print(tm)


# def great(nam='Ariz'):
#     print('hello', nam)

# great()


# def add(a, b):
#     print(a + b)


# x = add(3, 7)
# print(x)


# def add(a, b):
#     return a + b


# x = add(3, 7)
# print(x)

# nm = int(input("Enter your number "))

def check_even(nom):

    if nom % 2 == 0:
        return "Even"
    else:
        return "Odd"


nm = check_even(9)
print(nm)
