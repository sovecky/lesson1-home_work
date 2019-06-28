list = [1, 2, 4, 5, 6, 2, 5, 2]
list2 = set(list)
list3 = []
for item in list:
    if list.count(item) == 1:
        list3.append(item)

print(list2)
print(list3)