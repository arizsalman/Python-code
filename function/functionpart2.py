

# def my_func(value):
#     return value

# print(my_func("Python"))


# def my_func(value):
#     return "Hello World"


# print(my_func("Python"))


# def double(num):
#     return num**2


# do = double(10)
# print(do)


# def atob(a, b):
#     return (a + b)


# ab = atob(7, 3)
# print(ab)


# def check_even(number):
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"


# ch = check_even(3)
# print(ch)


# def adu(year):
#     if af > 18:
#         return f' Your are Adult and your age is: {year}'
#     else:
#         return f"you are Minor and your age is {year}"


# af = int(input('Enter a Birth Day '))
# ad = adu({af})
# print(ad)


# def alpha(a, b):
#     return (a+b, a-b, a*b)


# multy = alpha(3, 3)
# add, sub, mul = multy
# print(add, sub, mul)  # ye list me show ho gaya
# print(f'{add}, {sub}, {mul}')  # ye list me show ho gaya
# print(multy)  # ye tuple me show ho ga ya


# def read(names, age):
#     return (f'My Name is {names}, My age is {age}')


# red = read(names="Ariz", age=24)  # Ye best Taarka he
# red1 = read("Ariz", 24)  # Ye bhe atrkeqa he ye best nahe he
# print(red)
# print(red1)

'''Agar hum function ke ander  gobal value ko used karna cahe tu {global} ka keyword used kare gae'''

# count = 0


# def global_Count():
#     global count
#     count = +1


# global_Count()
# print(count)


# def prime(nump):
#     for i in range(2, nump):
#         if nump % i == 0:
#             return f' Number is not prime number {nump}'

#         else:
#             return f' The Prime number is {nump}'


# nur = int(input("Enter your number "))
# pN = prime(nur)
# print(pN)


# def primes(nums):
#     if nums < 2:
#         return f'Prime Number is Greater than {nums} '
#     for i in range(2, (int(nums**0.5)+1)):
#         if nums % i == 0:
#             return f' Not a Prime Number : {nums}'
#     return f' Your number is a Prime number {nums}'


# nus = int(input('Enter your number and see its a prime number is not '))
# p_N = primes(nus)
# print(p_N)

"""Function likho jo ek string le aur uska reverse return kare."""
""" {MAIN POINT Her kam karne ke buhat se point hote he see tarha reverse Kene ke 3 and zada terqe he }"""

''' AK Ye Tareka he '''

"""  [:: -1] 
first pe start  stop  step like kya karne he add etc
[start:stop:step ]
"""

# def reverseing(rev):
#     return rev[:: -1]

# res1 = reverseing("Ariz").upper()
# print(res1)

"""Ak ye tareka he """
""" .join() me jo bolo ge kar dee ga  agar ap space hatne ka kaho ge space ahta de ga agar ap kaho ge space hata ke {?>@#$$} koj be add kar do ye kar de ga or jane list,  string , tuple , any method ye mala deta he like this  words = ["Ariz", "Salman", "Python"]
      result = " ".join(words)
      print(result)
      Ariz Salman Pythonn  (ye result he )
 """


# def rever_se(re_v):
#     return " ? ".join(reversed(re_v))


# revd = rever_se("ARIZ")
# print(revd)

"""Function likho jo ek list me se maximum number return kare (without using max())."""


# def func(nums):
#     maximum = nums[0]
#     for num in nums:
#         if num > maximum:
#             maximum = num
#     return maximum


# print(f'{func([1, 2, 3, 4, 5, 6, 7, 7, 9])}')


"""Function likho jo ek list me se maximum number return kare (without using max()) is me hum ak chez add kare ge hum user se number le ge
us list me ham dekhe ge ke kon sa number bara bhe  ."""


# def func():
#     big_list = []
#     while True:
#         user_num = input('Enter your number end exit type "done"')
#         if user_num.lower().strip() == "done":
#             break
#         try:
#             num = int(user_num)  # ye string se integer pe kare ga
#             big_list.append(num)
#         except ValueError:
#             print(f'Please enter a valid number ')

#         print(big_list)

#     if not big_list:
#         return " No Number etered"

#     maximum = big_list[0]
#     for i in big_list:
#         if i > maximum:
#             maximum = i

#     return f" Maximum Number is : {maximum}"


# big_list = func()
# print(big_list)


# def func():
#     big_list = []
#     while True:
#         user_num = input('Enter your number end exit type "done"')
#         if user_num.lower().strip() == "done":
#             break
#         try:
#             num = int(user_num)  # ye string se integer pe kare ga
#             big_list.append(num)
#         except ValueError:
#             print(f'Please enter a valid number ')

#         print(big_list)
#     if not big_list:
#         return f'Number will Entered '
#     maximum = big_list[0]
#     for i in big_list:  # → list ke har number ko ek ek karke i me lo.
#         if i > maximum:  # → agar current number i ab tak ke maximum se bada hai, to:
#             maximum = i  # “maximum” ko update kar do.
#             """Left side = jis variable ko update karna hai
#             👉 Right side = jis value se update karna hai"""
#     return f"' YOu're Maximum value {maximum}"


# big_list = func()
# print(big_list)


''''Function likho jo ek string le aur count kare kitne vowels (a, e, i, 
o, u) hain'''


def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():  # lowercase kar liya taake 'A' bhi count ho
        if char in vowels:
            count += 1
    return count


print(count_vowels("Hello World"))   # output: 3 (e, o, o)
print(count_vowels("ARIZ"))


# def func():
#     vowels = 'a,e,i,o,u'
#     count = 0
#     user_name = input('Enter your Name ')
#     for i in user_name.lower():
#         if i in vowels:
#             count += 1  # count =count +1 dono same he
#     return count


# count_Vowels = func()
# print(f" this is your name Vowels Value  :{count_Vowels}")


"""Function likho jo ek list le aur sirf unique elements return kare (duplicate hata de)."""


def func(duplcate):
    uniqe = list(set(duplcate))
    """Set() ye Ek unordered collection hai → matlab order fix nahi hota.

     Duplicates allow nahi karta (automatic remove kar deta hai).
 
     Indexing nahi hoti (direct element access nahi kar sakte index se)."""
    return uniqe


duble = func([1, 2, 2, 3, 3, 4, 6, 5, 7, 8, 9, 0, 2, 3, 1, 2, 4])
print(duble)
