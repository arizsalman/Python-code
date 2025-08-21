# lists = []

# todo = input("Enter your Gorcery list")

# lists.append(todo)
# list_todo = str(lists)
# print(f'Its your Todo list {list_todo}')


# numBer_List = []
# while True:
#     nums = input("Enter your number exit type ok")
#     if nums.lower().strip() == "ok":
#         break

#     try:
#         numBer_List.append(int(nums))

#     except ValueError:
#         print(f"Please Enter your valid number ")

#     new_number_List = list(numBer_List)
#     print(f' YOur Number list is : {new_number_List}')


list_Todo = []
while True:
    to_do = input(" Please Enter item List : and exit type (exit) ")
    if to_do.lower().strip() == "exit":
        break

    try:
        if to_do.isdigit():
            raise ValueError('Number is not allow in groceory list ')
        # to_do.strip("") # ye sirf start me or end se space hata he
        to_do = to_do.replace(" ", "")  # remove all space start end midlle
        list_Todo.append(to_do)
    except ValueError:
        print(f'Please The Valid item ')

new_List = list(list_Todo)
print(f'Its Your Grocery item :{new_List}')
print(f'Its Your Grocery item :{len(new_List)}')
