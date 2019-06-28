import math;

list = [2, -5, 8, 9, -25, 25, 4]
list2 = []
for item in list:
    if item > 0 and math.sqrt(item) % 1 == 0:
        list2.append(int(math.sqrt(item)))
print(list2)

