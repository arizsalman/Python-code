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

Temperature = []
while True:
    temp = input(
        "Please enter Your city Temparature And You are exit so type done ")
    if temp.lower() == "done":
        break
    try:
        Temperature.append(float(temp))

    except ValueError:
        print(f" Please Vailad Number")

    Temperature_tuple = tuple(Temperature)

    print(f"your temperature list is {Temperature_tuple}")
    print(f"your temperature length is {len(Temperature_tuple)}")
    print(f"your temperature length is {min(Temperature_tuple)}")
    print(f"your temperature length is {max(Temperature_tuple)}")

    search_value = float(input("Enter the Temperature for show you "))
    if search_value in Temperature_tuple:
        print(
            f"This Temperature appears{Temperature_tuple.count(search_value)}")
        print(
            f" First occurrence index{Temperature_tuple.index(search_value)}")

    else:
        print(F'This Temperature is not Exist in Tuple ')

    Temperature_Sum = (search_value,)+Temperature_tuple
    print(f'The total Concatenate Value is {Temperature_Sum}')
    print(f'Slice first and end Number is {Temperature_tuple[0:-1]}')

    for search_value in Temperature_tuple:
        print(f"{search_value}'C is exist ")

    else:
        print(f"{search_value}'C is not exist ")
