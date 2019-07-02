def fibonacci(n, m):
    pass

    a = 1
    b = 1
    f_list = [1, ]

    for i in range(m):
        a, b = b, a + b
        f_list.append(a)
    return f_list[n - 1:m]

print(fibonacci(1, 10))

