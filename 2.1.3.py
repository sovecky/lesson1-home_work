lst = [1, 4, 3, 42, 48, 34, 16, 5, 10, 7, 8, 9]
lst2 = []
print(lst)
for i in lst:
    if i % 2 == 0:
        lst2.append(int(i / 4))
    else:
        lst2.append(int(i * 2))
print(lst2)

