# What is List operations
# A List operations are the operation that can be performed on data in the list structure.

# 🔹 ✅ Most Used Python List Methods (with Examples)
# Method	Description	Example
# append(x)	End me ek value add karta hai	list.append(10)
# extend([x, y])	Multiple values add karta hai	list.extend([2, 3])
# insert(i, x)	Specific index pe value add karta hai	list.insert(1, 99)
# remove(x)	Pehli matching value ko remove karta hai	list.remove(2)
# pop()	Last value ko hata kar return karta hai	list.pop()
# pop(i)	Specific index wali value hata kar return karta hai	list.pop(0)
#  clear()	Saari values remove kar deta hai	list.clear()
#  index(x)	Pehli baar x kaha mila uska index batata hai	list.index(10)
#  count(x)	x kitni baar aya uski count	list.count(3)
#  reverse()	List ko ulta kar deta hai	list.reverse()
#  sort()	List ko ascending order me arrange karta hai	list.sort()
#  len(list)	List ka size batata hai	len([1,2,3]) → 3
#  min(list)	Sabse chhoti value	min([1,2,3]) → 1
#  max(list)	Sabse badi value	max([1,2,3]) → 3

# # Append Method ye last me add karta he
# name = ["ariz", 'ali']
# name.append("salman")
# print(name)
# print(name[0:2])
# name.remove('salman')
# # remove me list ke ilava kye or value ho ge tu error de ga
# print(name)

# number = [1, 2, 3]
# number.append(5)
# print(number)
# number.remove(2)
# print(number)
# print(number[0:3])


# # Reverse string
# Alfh = str(input("Enter your Nonu"))
# listA = sorted(Alfh, reverse=True)
# listB = sorted(Alfh, reverse=False)
# print(f'Your Name is Reverse  True ;{listA}')
# print(f'Your Name is Reverse False ;{listB}')


faimly = ['Ariz', 'Salman']
faimly.append('Ali')
print(faimly)

faimly.clear()  # is ne list []clear kar de

print(faimly)


num = [0, 1, 1, 1, 2, 3,  4, 5, 6, 7, 8, 9]
print(num)
print(num.pop(1))  # ye pop ne minus kya
print(num)  # or answer deya
print(num.count(1))  # 1 ko count kar raha he


Myname = ['Ariz', 'Salman']
brother = ['Ali', 'Salman']
Myname.extend(brother)
print(Myname)
Myname.reverse()
print(Myname)
Myname.sort()
print(Myname)
