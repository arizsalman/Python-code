import random
#  Is Code Me Mistake he
# while True:
#     try:
#         g_num = int(input('Guess the Number '))
#         secret = random.randint(1, 10)
#         if secret == g_num:
#             print(
#                 f'Your Guess  Number is {g_num} : Genrator Numberd is {secret}')
#             break
#         else:
#             print(f'Your Number is{g_num} : Genrator Number is {secret}')
#     except TypeError:
#         print(f"You will not anwser for my Question So Plz Answer me")


# while True:
#     R_num = input("Enter the number ")
#     if R_num.strip() == "":
#         print(f"Please Enter the number And Cleck the Genrator number ")
#         continue  # baaki code skip → dobara input poochta hai
#     try:
#         R_numb = int(R_num)
#     except ValueError:
#         print("Please Enter the Valid Number ")
#         continue

#     secerat = random.randint(1, 10)

#     if R_numb == secerat:
#         print(f"Your Lucky number  is {R_numb} and Randan Number is {secerat}")
#         print("Thank you Ispent some Time see you again")
#         break
#     else:
#         print(f'Your Bad number is {R_numb}  and random number is {secerat}')

# while True:
#     P_num = input('Enter the Correct  pasword ')
#     if P_num == "A$123":
#         print("ThankYou For Right pasword ")
#         break
#     else:
#         print("Wrong Answer Please Right Anwser")

#  Second Vala best he
# while True:
#     P_num = input('Enter the Correct  pasword ')
#     if P_num != "A$123":
#         print("Wrong Answer Please Right Anwser ")

#     else:
#         print("ThankYou For Right pasword ")
#         break

# //Best Prictice
Correct_pasword = 'Ali$123'
attempts = 3
while attempts > 0:
    pa_num = input('Enter the correct pasword ')
    if pa_num != Correct_pasword:
        attempts -= 1
        print(f"Your pasword is Wrong .Attempt Left:{attempts}")
    else:
        print(f'Your pasword is Correct Welcome ')
        break
if attempts == 0:
    print(f'Access Deined . TOo many more time .')
