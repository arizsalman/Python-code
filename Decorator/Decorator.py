"""🔹Decorator ka main matlab yehi hota hai ke hum ek function ke start aur end (ya uske beech me) extra kaam add kar saken bina uska asal code badle. Decorator = ek special syntax (@decorator_name) jo automatically ek function ko wrapper ke through wrap kar deta hai"""


# def my_wrapper(func):       # wrapper function
#     def inner():            # inner function me asal kaam + extra kaam
#         print("Extra kaam start")
#         func()              # asal function call
#         print("Extra kaam end")
#     return inner


# def a1():                   # asal function
#     print("Main kaam ho raha hai")


# # Ab a1 ko wrap karenge
# a1 = my_wrapper(a1)         # wrapper ke through a1 ko decorate kar diya
# a1()                        # call karenge


# @my_wrapper
# def a1():
#     print("Main kaam ho raha hai done ")


# a1()


"""Jo main function ho ga vo decorator kehlata he """


def login_user(username):
    # ye main function he or hum is ke ander kuch kam ko change karna he magar bena is code ko krab kare
    print(f"{username} login ho gaya!")


login_user("Ariz")


"""Wrapper create karte hain"""


def logger_wrapper(func):          # wrapper function
    def inner(username):           # inner = asli function ka wrapper
        print(f"[LOG] Login attempt start for {username}")  # pehle extra kaam
        func(username)             # asli login function call
        # baad me extra kaam
        print(f"[LOG] Login attempt end for {username}")
    return inner


lo = logger_wrapper(login_user)
lo("Ariz")
