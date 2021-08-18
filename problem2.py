def fib(x, y, z):
    fib_sum = 0
    if x % 2 == 0:
        fib_sum += x
    if y % 2 == 0:
        fib_sum += y

    while y < z:
        x_temp = y
        y = x + y
        x = x_temp
        if y % 2 == 0:
            fib_sum += y

    return fib_sum


#print(fib(1, 2, 4000000))
