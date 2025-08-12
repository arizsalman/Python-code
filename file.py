import os

path = 'record.txt'
if os.path.exists(path):
    with open(path, 'r')as file:
        file.read()
        print('File is here .')
else:
    with open(path, "w") as file:
        file.write("Hello, World! I am Lost the time ")
        print('done')


# Ek Python program banao jo:

# Pehle check kare ke records.txt file exist karta hai ya nahi.

# Agar exist karta hai → uska content read karke print kare.

# Agar exist nahi karta → "No file found. Creating new file..." print kare
# aur naya file bana ke "Hello, World!" likhe


file = open('myfile.txt', "w")
file.write("Hello My Name Is Ariz ")
file.close

file = open('myfile.txt', 'r')
content = file.read()
file.close
print(content)


with open('myfiles', "w")as upfile:
    upfile.write("Helloo There My Name Is Ariz Salman  ")

with open('myfiles', 'r')as upfile:
    conect = upfile.read()
    print(conect)


with open("text.txt", "w") as files:
    files.write('hello My first file handling porgram')
file.close
with open('text.txt', "r") as files:
    reads = files.read()
    print(reads)


# Ek Python program banao jo:

# User se koi bhi sentence input le.

# Us sentence ko note.txt file me save kare.

# Phir file ko read karke output print kare.

# user_input = input('Please some sentence..only alpha. .bats')
# user_input = user_input.replace('\\n', '\n')
# with open('text.txt', 'w') as sfile:
#     sfile.write(user_input)
#     print(f'Sentence save as text.txt file ')


# Ek Python program banao jo:

# data.txt file me 5 alag-alag lines likhe (har line me koi phrase ya naam ho).

# Phir file ko read karke har line ko number ke saath print kare.(Example: 1: Ariz Salman)
list_name = [
    {
        'Name': 'Ariz Salman',
        'Age': "22", }, {
        'Name': 'Ali  Salman',
        'Age': "22", }, {
        'Name': 'Salman My father',
        'Age': "22"
    }
]
with open('data.txt', 'w') as file:
    for person in list_name:
        file.write(f"{person['Name']} {person['Age']} \n")
        print(f' seggesful print in datafile ')

with open('data.txt', "r") as file:
    file.readlines()
    print(f'done ')


#  With Enumrate

myfamily = [
    {
        'FName': "Muhammad Salman",
        'inrole': "Important in my family",
    },
    {
        'FName': "Muhammad Ariz",
        'inrole': "First Child"
    },
    {
        'FName': "Muhammad Ali",
        'inrole': "Second  Child"
    }
]

with open('data.txt', 'w') as file:
    for i, family in enumerate(myfamily, start=1):
        file.write(f'{i} :{family['FName']}-{family['inrole']}\n')
        print(f"done Upgrade Data overwrite hoo gaya {i} ")

with open('data.txt', 'r') as file:
    lines = file.readlines()
