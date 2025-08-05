
# 🔸 1. ValueError
#  Ye tab aata hai jab kisi cheez ka galat value diya jaye.
# age = int("hello")  age = str("hello") hona ye caheye
# 🔸 2. TypeError
# Ye tab aata hai jab galat type ke data ko combine ya use karne ki koshish karte ho.
# print("Age: " + 25) print("Age: " + str(25))hona ye chahye


# 🔸 3. try / except
# Ye Python ka system hai errors ko handle karne ke liye
# Agar koi line error kare, to program crash na ho — except me uska solution likhte hain.

try:
    num = int(input("Enter a number: "))
    print("Your number is:", num)
except ValueError:
    print("Please enter a valid number!")


# ValueError	 Galat value diya ho	     int("hello")
# TypeError    Galat data types combine kiye ho   	"age" + 10
# try/except   Error handle karne ke liye      	try: int(input())


name = " Muhammad Ariz"
last_name = "Salman"
# Ye formated string kelate he print(f"ye he format tareka ")
print(f"my name is {name} or my father name is {last_name}")


book = int(input("Enter your book price like (1,1000)"))
bill = (book * 4)
print(f"You bought 4 Notebooks at Rs. {book} each.")
print(f"Your total bill is: Rs. {bill}")
