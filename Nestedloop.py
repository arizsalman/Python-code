# # # Outer loop ek baar chalta hai → uske andar inner loop poora chalta hai
# # # Outer loop ek baar chalta hai -> uske andar inner loop poora chalta hai
# # for x in range(5):
# #     for y in range(3):
# #         print(f'{x} , {y}')

# # for x in range(1):
# #     for y in range(2):
# #         for z in range(3):
# #             print(f"{x}{y}{z}")


# for i in range(3):
#     print(i)

# for y in range(1, 4):
#     print(y)


# for a in range(3):
#     for b in range(1, 4):
#         print(b, end=" ")
#     print()


# for i in range(3):
#     for j in range(1, 4):  # range(1, 4) so it prints 1 2 3
#         print(j, end=' ')
#     print()  # new line after inner loop
# # end=" " ka matlab:"nayi line me na jao, balki isi line me aage likho,aur beech me space do"
# star = "*"
# for s in range(1, 5):
#     # 3 baar chalega (2, 3, 4) — ye rows hain
#     for t in range(s):
#         # jitna s hoga, utne stars print karo
#         print(star, end=" ")
#         # 	star print karo, line change na karo, space de do
#     print()
#       # 	ek row complete hone ke baad line change karo


# Table banani hai (nested loop)Print all multiplication tables from 2 to 10
# x = 5
# for table in range(2, x):
#     for i in range(1, 11):
#         print(f"{table} X {i} = {table * i}")

# Lazme nahi he ke hum ak variable bane
# for h in range(2, 4):
#     for i in range(1, 11):
#         print(f"{h} x {i} = {h*i}")


# for o in range(1, 6):
#     for l in range(o):
#         print(o, end=" ")
#     print()


# #  Reverse Method
# for r in range(5, 0, -1):  # 5 se start karo 0 tak jaluo -1 karo
#     for e in range(r, 0, -1):  # r se start karo 0 tak chalao -1 karo
#         print(r, end=" ")
#     print()


for sn in range(5, 0, -1):
    for t in range(sn):
        print('*', end=" ")
    print()


# enumerate() 2 values return karta hai:

#   1 is index

#  2 is item


fruit = ["apple", "graps", "banana"]
for index, value in enumerate(fruit):
    print(index, value)

word = input("Enter your name")
for le in word:
    print(le, end="")
