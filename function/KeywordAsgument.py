# """📌 **kwargs kyon zaroori hai?

# Jab hume pata nahi hota kitne arguments aayenge.

# Jab function ko flexible aur reusable banana ho.

# Machine Learning, Django, Flask jaise frameworks me functions ko flexible banane ke liye use hota hai."""


# def key_Word(**kwargu):
#     for k, v in kwargu.items():
#         print(f'{k}:{v}')


# key_Word(name="Ariz", age=22, culification="Zero")
# key_Word(name="Ariz", age=22, culification="Zero")
# key_Word(name="Ali", age=22, culification="Good")
# key_Word(name="Ariz", age=22, culification="Zero")
# key_Word(name="Ariz", age=22, culification="Zero")


# """Ye Dictionary ke form me aeiii ga """


# def key_Word1(**kwargu):
#     return kwargu


# print(key_Word1(name="Ariz", age=22, culification="Zero"))


# def ran(limit):
#     limit = 10
#     for i in range(2, limit+1,  -2):
#         print(i)


# re = ran(10)
# print(re)


# def ran(limit):
#     limit = 10
#     for i in range(20, 2,  -4):
#         print(i)


# re = ran(10)
# print(re)


# def ran(limit):
#     limit = 10
#     for i in range(2, limit+1,  2):
#         return i


# re = ran(10)
# print(re)


# def ren(limits):
#     limits = 10
#     number = []
#     for i in range(2, limits+2, 2):
#         number.append(i)
#         print(number)
#     return number


# res = ren(10)
# print(res)


"""🔎 Kyun aisa hua?

Jab function me yield hota hai, wo normal function nahi banta.

Wo ek generator object return karta hai.

Is generator ko use karne ke liye tumhe loop lagana padta hai (for loop ya next()), warna wo values show nahi karega."""
# ye value show nahe kar ga jab tak hum return ke baher loop nahe cahle ge
# for num in ran(10):


def ran(limit):
    limit = 10
    for i in range(2, limit+1,  2):
        yield i


# re = ran(10)
# for num in re:
#   print(num) 
""" ye dono tareqo se cahle ga """

for num in ran(10):
    print(num)
