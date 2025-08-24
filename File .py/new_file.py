file = open('chai.txt', 'w')
try:
    file.write('My Name is Ariz')
finally:
    file.close()

with open('chai.txt', 'a') as file:
    file.write('My name is Ariz Salman')
