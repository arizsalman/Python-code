# import time


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__}ran in {end-start}time ")
#         return result
#     return wrapper


# @timer
# def example_function(n):
#     time.sleep(n)
#     print(f"function executed")


# example_function(2)


# Example two

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in  args)
        return func(*args, *kwargs)

    return wrapper


def greet(name, greeting="Hello"):
    print(f'{name} ,{greeting}')


greet('Ariz')
