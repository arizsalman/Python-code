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
    temp = input('Enter the temperature number and  exit is type done ')
    if temp.lower() == 'done':
        break
    try:
        Temperature.append(float(temp))
    except ValueError:
        print('Please Enter Invalaid number ')
Temperature_tule = tuple(Temperature)
print(f'Total  Temperature is :{Temperature} *C ')
print(f'Total Number Of Temperature is :{len(Temperature)}')
print(f'Minum Number Of Temperature is :{min(Temperature)}')
print(f'Maxium Number Of Temperature is :{max(Temperature)}')

temp_Value = input("Enter a temperature Number ")
if temp_Value in Temperature_tule:
    print(f'Total Count Temperature is {Temperature_tule.count(temp_Value)}')
    print(f'Total Index Temperature is {Temperature_tule.index(temp_Value)}')

SumTemp = (temp_Value,)+Temperature_tule
print(f'Total Temperature is :{SumTemp}')
print(f'Total first   temperature  is :{SumTemp[0]}')
print(f'Total  last  temperature  is :{SumTemp[-1]}')

check_temp = input('Check  the  temperature')

if check_temp in Temperature_tule:
    print(True)
else:
    print(False)
