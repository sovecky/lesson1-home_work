def filter_func(f, m):
    return (item for item in m if f(item))


print(list(filter_func(lambda x: True if x > 3  else False,
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
