

# Kese kam ko bar bar repeat kerne ke leyge used kerte he
# num = 100
# while num > 0:
#     print(num)
#     num //= 2

# Example no 2  while loop
# name = ""
# while name != "ariz":
#     # print("Wrong Name", name)
#     name = input(">")
#     if name != 'ariz':
#         print("Wrong Name")
# print("Right Name")


# Infinite loop
#  Jab tak is ke value true se false nahe ho jate jab tak ye jalta rahe ga
# Example infinite loop
# while True:
#     name1 = input("Enter your name ")
#     if name1 == "ariz":
#         print('Welcome ariz')
#         break    # ye loop ko ruta he
#     else:
#         print("try again")


#  # Use while loop to print numbers from 1 to 5.

# num = 1
# while num <= 5:
#     print(num)
#     num += 1

# # Use while loop to keep asking user's name until they type "ariz".
# # # ( Hint: while name != "ariz")
# Nam =" "
# while Nam != "ariz":
#     Nam = input("Enter your name ")
#     if Nam !="ariz":
#        print(f'Wrong{Nam}')

# print(f"Right {Nam}")


# i = 0
# while i <= 10:
#     print(f"{i}times Ariz ")
#     i += 1  # i= i+1 ye be tareka hi


# num = int(input('what is number'))
# i = 0
# while i <= 10:
#     print(f'{num} X {i}= {num*i}')
#     i = i+1


while True:
    str1 = input('Enter your First number or "exit" to quit :')
    if str1 == 'exit':
        break

    str2 = input('Enter your Second number  :')
    Operator = input('*,+,-,/ :')

    try:

        num1 = int(str1)
        num2 = int(str2)

        if Operator == '+':
            print("Result:", num1 + num2)
        elif Operator == '-':
            print("Result ", num1-num2)
        elif Operator == '*':
            print("Result ", num1*num2)
        elif Operator == '/':
            print("Result ", num1/num2)
        else:
            print("Invalid operator.")
    except ValueError:
        print("Invalid number. Please enter numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
