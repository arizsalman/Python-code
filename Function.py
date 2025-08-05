
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


def add(a, b):
    return (a+b)


def subt(e, r):
    return (e-r)


def mul(x, y):
    return (x*y)


print(add(20, 10))

print(subt(10, 5))
print(mul(2, 20))

