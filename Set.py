# set1 = {1, 2, 3, 4, }
# print = (set1)
# print = (type(set1))

# Sset = set([1, 0, 9, 7, 9, 8, 7, 1])
# print(Sset)
# print(type(Sset))


numa = {1, 2, 3, 6, 6}
numb = {1, 2, 5, 6, 9}
mer = numa.union(numb)
int = numa.intersection(numb)
der = numa.difference(numb)
sym = numa.symmetric_difference(numb)  # is me jo common ho ga vo nahi ag ga
# is me jo common ho ga vo nahi ag ga
symu = numa.symmetric_difference_update(numb)
print(numa)
print(numb)
print(mer)
print(int)
print(der)
print(sym)
print(symu)
