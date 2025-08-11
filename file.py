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

user_input = input('Please some sentence..only alpha. .bats')
user_input = user_input.replace('\\n', '\n')
with open('text.txt', 'w') as sfile:
    sfile.write(user_input)
    print(f'Sentence save as text.txt file ')
