while True:
    b_num = input('Enter a Total Income Or tpye exit to quite ')
    if b_num.strip().lower() == "exit":
        print(f' Exit  Program ')
        break
    if b_num.strip() == "":
        print(' Pleasse Enter the  Number .')
        continue
    try:
        b_numb = int(b_num)
    except ValueError:
        print("Enter the Valaid number .")
        continue
    e_num = input('Plaese Enter the Total Expense ')
    if e_num.strip() == "":
        print("Please Enter the Number ")
        continue
    try:
        e_numb = int(e_num)
    except ValueError:
        print(f'Enter the Valaid Number ')
        continue

    to_num = b_numb-e_numb
    if to_num <= 0:
        print(
            f'Your  Total Income is {b_numb}.\n and YOur Expenesce is {e_num}.\n  and Your not save  Money is {abs(to_num)} ')
    else:
        print(
            f"Your Total Income is {b_numb}, Your Expense is {e_num}, and Your Savings are {to_num}.")
