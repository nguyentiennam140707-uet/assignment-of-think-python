list0 = [1, 2, 3]
list1 = [4, 5]
t = (list0, list1)

d = {t, 0}
print(d) #TypeError: cannot use 'tuple' as a set element (unhashable type: 'list')