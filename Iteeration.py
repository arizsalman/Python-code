# f = open('Iteeration.py')
# iter(f) is f
# print(f)
"""Important Point:

File object iterator isiliye hai kyunki uske andar __iter__() aur __next__() methods defined hote hain."""


# print(iter(f) is f)
# print(f.__iter__() is f)


"""Iterable kya hai?

Iterable wo object hai jisko hum loop (for loop) me use kar sakte hain.

Example: list, tuple, str, dict, set, file object etc."""
# nums = [1, 2, 3]
# print(dir(nums))  # isme __iter__ method hoga

"""Iterator kya hai?

Iterator wo object hai jo __next__() method support karta hai.

Har __next__() call par ye agli value deta hai.

Jab values khatam ho jati hain, to StopIteration error deta hai."""

# nums = [1, 2, 3]
# it = iter(nums)
# print(iter)
# print(iter is nums)

"""👉 Summary

Iterable: jispe iter() chal sakta hai (list, str, dict …)

Iterator: jo __next__() support kare (aur khatam hone par StopIteration raise kare).

Iteration Tools: ye hi combination hai iter(), next(), aur StopIteration ka."""


"""🔹 1. iter() ka kaam

Kisi iterable (list, tuple, string …) ko iterator object banata hai."""

nums = [10, 20, 30]
it = iter(nums)   # ab ye iterator hai
print(it)         # <list_iterator object>

"""<list_iterator object at 0x0000016DE02FB700>
<list_iterator object at 0x00000129D866B730>
yar  interview me ye question puja jata ke object ke value ko change ho rahe he ____---->
----->  tu is ka anwser he ke sir ye object nahe he palke  0x00000129D866B730 ye jo number he ye as a memory adress he jo change hota he  or object jo he co as a <list_iterator he ye change nahe hota 
"""
"""next() ka kaam

next(it) se iterator ki agli value milti hai.

Jab values khatam ho jati hain → StopIteration error aata hai."""

# nums = [10, 20, 30]
# it = iter(nums)

# print(next(it))  # 10
# print(next(it))  # 20
# print(next(it))  # 30
# print(next(it))  # StopIteration (yaha values khatam ho gayi)


"""3. StopIteration handle karna

Agar tum chaho to try-except use karke StopIteration ko handle kar sakte ho:"""

nume = [1, 2]
its = iter(nume)
while True:
    try:
        val = next(its)
        print(val)
    except StopIteration:
        print('Sab Value kathum ho ke (stopIteration )')
        break
