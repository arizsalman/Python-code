import math


def circle_stats(radius):
    area = math.pi*radius ** 2
    circumference = 2*math.pi*radius
    return area, circumference


a, c = circle_stats(3)
print("area:", round(a, 2), " circumference:", round(c, 4))
"""Round Ka karta he ke jab value .ke bad pare a jate  he tu vo jota ker de taa he """


"""lambda ye basicly used libary me hota he jab hum gango or dosre libary me hota he """

# cube =lambda x:x**3
# print(cube(3))

'''* Jab tum function me *args likhte ho, iska matlab hai ki jitne bhi extra arguments pass karoge wo tuple me collect ho jayenge
or sum ()kya he  : ye ak method he jo value ko add karta he 
'''
"""* args jo he vo argument ko handle karta he """

def sum_all(*args):
    print(args) # ye tuple return karta he
    print(*args)
    return sum(args)


print(sum_all(1, 2,  6, 0))
print(sum_all(1, 2, 3, 4, 5, 6, 23, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 34, 5, 67, 75, 100))
