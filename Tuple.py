# fruits = ("ariz") # is ke type str he because hum ne ,nahe lagaye ("ariz",)ye tuple he (, )lage ge tu tuple bene ga
# print(type(fruits))

# fruits = ("ariz",) #hum ye , lagen ge  tu tuple type ho ge
# print(type(fruits))


# color = ("red", "white", "snow", "green", "yellow")
# print(type(color))
# print(color.count('green'))
# print(color.index('green'))
# print(len(color))
# print(sorted(color))


# # hum srif integer ko is tareqe se kar sakhte hr magar ye bad practice  he
# num = 1, 2, 2, 3, 45, 5, 6,
# print(type(num))


# data = ("Ariz", 24, True, 33.3, "Ariz", "Ali", "Salman")
# print(type(data))
# print(data)
# print(f' first element {data[0]}')
# print(f' Last element {data[-1]}')
# print(f'Ariz Are {data.count("Ariz")} time count')  # ye bhe tareqa he
# item = 'Ariz'
# print(f'Ariz Are {data.count(item)} time count')  # or ye bhe
# print(len(data))


# # Pair Method
# a, b = 1, 2
# print(a)
# print(b)

# a, *b, c = [1, 2, 3, 4, 5, 6, 8, 7, 9, 0,]
# print(a)
# print(b) # ye *1 or last variable kr cor ke sari leye ga value
# print(c)


# Write a Python program that:
# 1.Lets the user enter city temperatures (in °C) until they type "done".
#  2.Stores the temperatures in a tuple.
#  3.Displays:
# •Total number of temperature readings (len()).
# •Highest temperature (max()) and lowest temperature (min()).
# 4.Asks the user for a temperature value and shows:
# •How many times it appears (.count()).
# •Its first occurrence position (.index()), if it exists.
# 5.Creates another tuple with new temperatures and concatenates it with the original.
#  6.Displays a slice of the combined tuple based on user-provided start and end indexes.
#  7.Checks if a specific temperature exists in the tuple using in.

# Short key
# = → value assign karna
# .append() → list me ek naya element add karna
# tuple() → list ko tuple me badalna

# Code Sahe nahe hai


favourite_Friut = []
while True:
    friut = input("Enter your five favourite friuts ")
    try:
        favourite_Friut.append(friut)
    except ValueError:
        print(f'Please Invalaid Fruit Name')
    if len(favourite_Friut) >= 5:
        break
print(type(friut))
print(type(favourite_Friut))
if "Mango" in favourite_Friut:
    print(f" Fruit me mango itne par he :{favourite_Friut.count('Mango')}")
else:
    print(" The is No Mango in Your  list ")

print(f" Fruit me Apple itne par he :{favourite_Friut.count('Apple')}")

if 'Banana' in favourite_Friut:
    print(f" Fruit me Banana Index :{favourite_Friut.index('Banana')}")
else:
    print('Not found')


print(f' Fruit me mango itne par he :{favourite_Friut}')
print(f' Fruit me mango itne par he :{len(favourite_Friut)}')
