import time

# def cashe(func):
#     cashe_value = {}
#     print(cashe_value)
#     print('Start Function')

#     def wrapper(*args):
#         if args in cashe_value:
#             return cashe_value[args]
#         result = func(*args)
#         cashe_value[args] = result
#         return result
#     return wrapper


# @cashe
# def long_runing_func(a, b):
#     time.sleep(4)
#     return a+b


# print(long_runing_func(2, 3))
# print(long_runing_func(2, 3))


"""Ek decorator banao jo function chalne se pehle "Function start" aur baad me "Function end" print kare.
"""


def deco(func):

    def wrapper(*args, **kwargs):
        print(f'Start Function')
        results = func(*args, **kwargs)
        print(f'End Function')
        return results

    return wrapper


@deco
def end():
    time.sleep(2)
    print(f'Runinng inside the Function')


end()


def square_decorator(func):
    def warpper(*args, **kwargs):
        resultin = func(*args, **kwargs)
        return resultin ** 2

    return warpper


@square_decorator
def get_number():
    return 5


print(get_number())
