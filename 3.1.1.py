def my_round(number, ndigits):
    pass

def my_round(number, ndigits):
    number = number * (10 ** ndigits)
    if float(number) - int(number) > 0.5:
         number = number // 1 + 1
    else:
         number = number // 1
    return number / (10 ** ndigits)

print(my_round(2.1234567, 4))