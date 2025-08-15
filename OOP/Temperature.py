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

Temperature = []
while True:
    temp = input("Enter the temperature  Number You exit type done ")
    if temp.lower() == 'done':
        break
    try:
        Temperature.append(float(temp))
    except ValueError:
        print(f'Please enter a Invalaid number ')

Temperature_tuple = tuple(Temperature)
print(f'Your temperature list is this : {Temperature}')
print(f'Your temperature Length is this : {len(Temperature)}')
print(f'Your temperature Length is this : {max(Temperature)}')
print(f'Your temperature Length is this : {min(Temperature)}')

temp_value = float(input('Enter a temperature value '))
if temp_value in Temperature_tuple:
    print(f' YOur count Value is :{Temperature_tuple.count(temp_value)}')
    print(f' YOur Index Value is :{Temperature_tuple.index(temp_value)}')
else:
    print(f' If not exist')

final_Temp = (temp_value,)+Temperature_tuple
print(f'Sum of the Temperature is : {final_Temp}')
print(f'Sum of the Temperature is : {final_Temp[0:-1]}')

check_temp = input('Enter the temperature exists in the tuple ')
if check_temp in final_Temp:
    print(True)
else:
    print(False)
