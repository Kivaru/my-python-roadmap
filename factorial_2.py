def factorial(n):
    return_value = 1
    for x in range(2, n + 1):
        return_value *= x
    return return_value


print(factorial(4))
