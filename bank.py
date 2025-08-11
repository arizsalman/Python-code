import time
# Total Expesence & income
# while True:
#     b_num = input('Enter a Total Income Or tpye exit to quite ')
#     if b_num.strip().lower() == "exit":
#         print(f' Exit  Program ')
#         break
#     if b_num.strip() == "":
#         print(' Pleasse Enter the  Number .')
#         continue
#     try:
#         b_numb = int(b_num)
#     except ValueError:
#         print("Enter the Valaid number .")
#         continue
#     e_num = input('Plaese Enter the Total Expense ')
#     if e_num.strip() == "":
#         print("Please Enter the Number ")
#         continue
#     try:
#         e_numb = int(e_num)
#     except ValueError:
#         print(f'Enter the Valaid Number ')
#         continue

#     to_num = b_numb-e_numb
#     if to_num <= 0:
#         print(
#             f'Your  Total Income is {b_numb}.\n and YOur Expenesce is {e_num}.\n  and Your not save  Money is {abs(to_num)} ')
#     else:
#         print(
#             f"Your Total Income is {b_numb}, Your Expense is {e_num}, and Your Savings are {to_num}.")


# Question no 2
# Account detail

blance = 1000

while True:
    print(f'\n ATM Main Menu ..')
    print(f'1 Check Blance  ..')
    print(f'2 Cash Withdraw Money ..')
    print(f'2 Deposite Money')
    print(f'4 Exit  ..')

    choice = input('Enter your Your requirement  (1,4 )')

    if choice == '1':
        print(f' Your blance is {blance} PKR')
        time.sleep(2)

    elif choice == '2':
        while True:
            amount = input("Enter your amount ")

            if not amount.isdigit():
                print(f' Invaid Amount : Enter the Valiad amount')
                time.sleep(2)
                continue
            amount = int(amount)
            if amount > blance:
                print(f"Insufficent  Blance ")
                time.sleep(2)
            elif amount <= 0:
                print(f"Amount must be greater then zero")
                time.sleep(2)
                break

            else:
                blance -= amount
                print(f"Withdraw Secessful . new Blance is :{blance}")
                time.sleep(2)
                break
    elif choice == '3':
        while True:
            amount = input('enter your deposite amount')

            if not amount.isdigit():
                print(f'Invaid Amount :Enter the Valiad Amount ')
                time.sleep(2)
                continue
            amount = int(amount)
            if amount <= 0:
                print(f'Amount must be greater then zero ')

            else:
                blance += amount
                print(f"Your update Amount is {blance}")
                time.sleep(2)
                break
    elif choice == '4':
        print(f' Thank You for using my ATM ...')
        time.sleep(2)
        break

    else:
        print(f" Invaliad Choice .Please select between (1,4)")
        time.sleep(2)
