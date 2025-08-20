# lists = []

# todo = input("Enter your Gorcery list")

# lists.append(todo)
# list_todo = str(lists)
# print(f'Its your Todo list {list_todo}')

# list_Todo = []
# while True:
#     to_do = input(" Please Enter item List : and exit type (exit) ")
#     if to_do.lower() == "exit":
#         break

#     try:
#         list_Todo.append(str(to_do))

#     except ValueError:
#         print(f'Please The Valid item ')

# new_List = list(list_Todo)
# print(f'Its Your Grocery item :{new_List}')

numBer_List = []
while True:
    nums = input("Enter your number exit type ok")
    if nums.lower().strip() == "ok":
        break

    try:
        numBer_List.append(int(nums))

    except ValueError:
        print(f"Please Enter your valid number ")

    new_number_List = list(numBer_List)
    print(f' YOur Number list is : {new_number_List}')
