"""🔹 Recursive Function kya hota hai?

Ek function jo apne aap ko call karta hai usse recursive function kehte hain.
Ye ek problem ko chhote-chhote parts me todh deta hai jab tak ki ek base case na mil jaye."""

"""🔹 Base Case ka matlab:

Stopping condition jo recursion ko rokta hai.

Agar base case na ho to function infinite bar apne aap ko call karega aur infinite loop / error (RecursionError) ho jayega."""


"""Chhoti si baat yaad rakhna ✅

Loop aur recursion dono se repeat kaam ho jata hai.

Bas recursion me function apne aap ko call karta hai."""


def factorial(i):
    if i == 0:
        return 1
    else:
        return (i * factorial(i-1))


print(factorial(5))
