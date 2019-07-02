def mySort(user_function, arg_list):
    result = list()
    for item in arg_list:
        if user_function(item):
            result.append(item)
    return result



number_list = range(-10, 10)
less_than_zero = list(mySort(lambda x: x < 0, number_list))
print(less_than_zero)