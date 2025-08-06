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

# Append Method ye last me add karta he
name = ["ariz", 'ali']
name.append("salman")
print(name)
print(name[0:2])
name.remove('salman')
# remove me list ke ilava kye or value ho ge tu error de ga
print(name)

number = [1, 2, 3]
number.append(5)
print(number)
number.remove(2)
print(number)
print(number[0:3])
