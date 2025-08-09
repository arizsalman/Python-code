
# # if ,elif eles condition ke last me {collon : lagna zarore he }
# num = int(input("Do you have any experiance:"))
# learning = num
# if learning <= 20:
#     print("You are not a  Beginner, intermedates, advance You are the loser ")
# elif learning >= 20 and learning < 60:
#     print("You are Beginner")
# elif learning >= 60 and learning < 80:
#     print(" You are intermediate ")
# if learning >= 80:
#     print("Your skill is the advance levels ")

# if 10 == "10":
#     print("a")
# elif "bag" > "apple " and "bag" > "cat":
#     print("B")
# else:
#     print("c")


# list = ["ariz", 21, 2, "apple", "graps", "ali"]
# user_input = int(str(input("Enter your Value")))
# if user_input in list:
#     print("your input value is exist in list")
# else:
#     print("your user are not exist in the list")


# a = int(input('Enter a First Number'))
# b = int(input('Enter a second number'))

# if a <= b:
#     print(f"{a} is Less Than or Equal to {b}")
# else:
#     print(f"{a} is NOT Less Than or Equal to {b}")
# if a >= b:
#     print(f"{a} is Greater Than or Equal to {b}")
# else:
#     print(f"{a} is NOT Greater Than or Equal to {b}")


# age = int(input("Enter your Age "))

# if age >= 18 and age <= 40:
#     print(f'your age is {age} are you Eligeble ')
# else:
#     print(f'Your age is {age} are not eligeble ')


# grade = int(input("what is your grade :"))

# if grade >= 20 and grade <= 49:
#     print(f'you are fail')

# elif grade >= 50 and grade <= 79:
#     print(f'your Grade is B')

# elif grade >= 79 and grade <= 89:
#     print(f'your Grade is A')

# elif grade >= 89 and grade <= 100:
#     print(f'your Grade is A+')

# print('Thank You')


# Question  Even or odd number check

# OE = int(input("Enter the  Even and Odd Number "))

# if OE % 2 == 0:
#     print(f'The number is {OE} this is Even number ')

# else:
#     print(f' This number is {OE} odd')


# inf = int(input("Enter number  "))
# if inf >= 20:
#     print(f' the number is greater then{inf}')
# else:
#     print(f"the number is lessthen 20 your number{inf} ")


# Prime  number Not true
# Prime number  1 se bara ho
# surf apne   number se divide ho  ye prime number hota he


# new_num = int(input("Enter your number "))
# if new_num > 1:
#     for i in range(2, new_num):
#         if new_num % i == 0:
#             print(f' the number is not prime number{new_num}')
#             break
#     else:
#         print(f'Your number is prime number {new_num}')

# else:
#     print(f'Prime number 1 se bara hota hai')


# new_num = int(input("Enter your number "))
# for i in range(2, new_num):
#     if new_num % i == 0:
#         print(f' the number is not prime number{new_num}')
#         break
#     else:
#         print(f'Your number is prime number {new_num}')

# else:
#     print(f'Prime number 1 se bara hota hai')


# # FactorialNumber
# Fa_num = int(input("Enter your number "))
# fact = 1
# for i in range(1, Fa_num + 1):
#     fact *= i
#     print(f'your Factorial number is {Fa_num} is {fact}')

a = ["Ariz", "Salman", "Ali"]
b = ["Ariz", "Salman", "Ali"]

print(a != b)

a1 = 2
b1 = 6
print(a1 <= b1)


# Fibonacci sequence

Fc_num = int(input("Enter your number "))
a, b = 0, 1
for _ in range(1, Fc_num-1):
    print(a, b)
    a, b = b, a+b
