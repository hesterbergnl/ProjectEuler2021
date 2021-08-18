def multiples (a, b, x):
    summ = 0
    for i in range(1, x):
        if i % a == 0 or i % b == 0:
            summ += i
    return summ


print(multiples(3, 5, 1000))
