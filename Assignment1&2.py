# print(" Hello Ariz ") agar ap ne english me kuch bhe lekna ho "Is ke ader add karo ge " e.g ===>

print(" Hello Ariz ")

# kio number lekhna ho Normal leky ge
print(10)

# or kese bhe value ko Double jetni par add  karna ke lekvana ho ====>
print("Ariz"*8)

# Variable This are premated type
any_words = "ariz"  # this are string
any_number = 122  # this are number type
any_decimalnumber = 0.2, 0.4, 5.5  # this are float type
# ture or false are boolean type

# Agar ap ko kese bhe charcater  pata karne he Apply kare :len() or ye speces bhe genta he

your_name = 'Muhammad Ariz Salman  '
print(len(your_name))
print(your_name[0])

# [-4]  ye [4 ]index(a)he or (a)nahi ay ga ye return kare ga(h) ye is ka behavier  he  or ye minus pe akar  se bata he -1 = (n).-me 0 se nahe hoga
print(your_name[-4])
# ana chaeye  [muha]
print(your_name[0:4])

print(your_name[:])  # or [:]ya pe  kuch defauit value [ pure ai gae]r

# ye {\  is me bhe special charter de sakte ho } ye tool bohat kam ka he agar code me ap ne "ye used karna ho / " tu ase kare ge other wese ye error de de ga "
special_letter = "HELLO WORLD \ { \ @#%^&} Hi Ariz  "
print(special_letter)

anther_line = "Hello \n Hi Ariz "  # hume next line me  value de ho tu ye karo
print(anther_line)

name1 = '  ariz'
name2 = ' salman'
# Is kam karne ke 2 tareke he [1 sample '+'or 1+""+2  or f"{1}{2}"ye pro tareka he  ]
full_1 = name1 + name2
full_2 = name1+" "+name2
full_3 = f"{name1} {name2}"  # ye pro taareka  hi
print(full_1.title())
print(full_2)
print(full_3.upper())
print(full_3.strip())
print(full_3.rstrip())
print(full_3.lstrip())
print(full_3.replace("a", "A"))


x = input("Enter a number: ")
y = int(x) + 1
print(f" The value of X is :{x}, The value of  Y is :{y}")
print(type(x))
#  { 0, "" None }ye value boolen me  false and anthing are ture

# if ,elif eles condition ke last me {collon : lagna zarore he }
num = int(input("Do you have any experiance:"))
learning = num
if learning <= 20:
    print("You are not a  Beginner, intermedates, advance You are the loser ")
elif learning >= 20 and learning < 60:
    print("You are Beginner")
elif learning >= 60 and learning < 80:
    print(" You are intermediate ")
if learning >= 80:
    print("Your skill is the advance levels ")

if 10 == "10":
    print("a")
elif "bag" > "apple " and "bag" > "cat":
    print("B")
else:
    print("c")

for number in range(2):
    print("Muhammad Ariz ", number)
    print("Muhammad Ariz ", number+1, (number+1)*".")

# Range me hum sirf 3 argument de sakte hn (one is kaha se start karna  he , or second is kaha tak ke jalana he , or third is Last ketna add karna he )
for number1 in range(2, 7, 3):
    print("Attempt", number1, number1*".")


# Loops ;repeated work ke leye hote he
successful1 = False
for number9 in range(3):
    print("Attmept ")
    if successful1:
        print("Successful")
        break
else:
    print("Attmept in 3 time and failed ")

# Loop second
# for X in Y: ka matlab hota hai:
# Y me jitne elements hain, unko ek ek karke X me store karo
friuts_a = ["apple", 'banana', 'graps']
for friut in friuts_a:
    print(friut)

name = ['ariz', 'salman', "ali"]
for English in name:
    print(English)

for x in range(5):
    print(x)

# Outer loop ek baar chalta hai → uske andar inner loop poora chalta hai
# Outer loop ek baar chalta hai -> uske andar inner loop poora chalta hai
for x in range(5):
    for y in range(3):
        print(f'{x} , {y}')
