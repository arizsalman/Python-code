import random


# # #practice
# # Example in Even
# for even_num in range(1, 10):
#     if even_num % 2 == 0:
#         print("we have  even number ", even_num)

# # Example in odd number
# for odd_number in range(1, 15):
#     if odd_number % 3 == 0:
#         print("We have odd number ", odd_number)

# # count = 0
# for nume in range(1, 12):
#     if nume % 2 == 0:
#         count += 1
#         print(nume)
# print(f"We have {count} even Numbers ")

# # . Print numbers from 1 to 10 using range().

# for ten in range(1, 11):
#     print(ten)
# #  Print numbers from 10 to 1 in reverse order.
# # range(10, 0, -1) ka matlab hai:
# #Start from 10
# #Stop before 0 (matlab 1 tak chalega)
# # Step size -1 (har baar 1 kam hoga)

# for revrese in range(10, 0, -1):
#     print(revrese)


# #Print square of each number from 1 to 5.(Like: 1×1=1, 2×2=4, ...)

# for i in range(1, 6):
#     print(f"{i} x {i} = {i}")


# for x in range(5):
#     print(x)


# for number in range(2):
#     print("Muhammad Ariz ", number)
#     print("Muhammad Ariz ", number+1, (number+1)*".")

# # Range me hum sirf 3 argument de sakte hn (one is kaha se start karna  he , or second is kaha tak ke jalana he , or third is Last ketna add karna he )
# for number1 in range(2, 7, 3):
#     print("Attempt", number1, number1*".")


# Table Gentrator
t_num = int(input("Enter the number"))
for i in range(1, 11):
    print(f" {t_num} X {i} = {t_num*i}")

r_num = int(input('Guess  the Number '))
i = random.randint(1, 20)
print(f"{i},{r_num}")

# TRY AND EXCEPT >>>>
try:
    num = int("hello")
except:
    print("I will never run Because integer is not convert to string .!")
