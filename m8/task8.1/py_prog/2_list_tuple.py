list = []
num = ''
while len(list) < 5:
    num = input("Please, enter only number: ")
    list.append (num)

print(list, type (list))
tuple = tuple (list)
print (tuple, type(tuple))
