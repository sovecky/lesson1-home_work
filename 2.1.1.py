s1 = ["яблоко", "банан", "киви", "арбуз"]
name = len(s1)
for i in range(name):
    print(str(i + 1) + '.' + '{}'.format(s1[i]))