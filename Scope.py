""" 🔹 Python Closure
Jab outer function khatam ho jata hai aur inner function uske variable ko zinda rakhta hai, usi ko Closure kehte hain.
def outer():
    x = 10
    def inner():
        print(x)  \\\\is  ko  closure kete he 
    return inner
"""


"""🔹 Python me Scope ke types

Python me ek famous rule hai LEGB (Local → Enclosing → Global → Built-in)"""
""" Local jo function ke ander call ho rahe ko 
e.g ==--> def num() ==> n=2 ye he local scope  jo function ke annder call ho raha hu 
"""
"""Enclosing scope 
 --> ak function ke ander ak varaible bana ke value de or us function ke ander ak or function banaya phir first function ke varaible ko dusree function me call kya us call karne ko Enclosing scope kehte hi .
 e.g def fun() => i=2  def func2() print(i) ye he Enlosing  function ...
"""

"""Global scope
Function ke bahar banaye gaye variables, poore file me accessible hote hain.
name="Ariz"    ---> Ye he global Function 
def new_Func()

"""
"""Built-in scope
Python ke andar jo predefined names hain (jaise len, print, range) unka apna built-in scope hota hai.
"""


def f1():
    x = 88

    def f2():
        print(x)
    return f2


my_result = f1()
my_result()
