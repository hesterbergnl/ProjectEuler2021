import math


def isPrime(num):
    max_range = round(math.sqrt(num))

    for i in range(2, max_range):
        if(num % i == 0):
            return False
    return True


def factor(num):
    max_range = num // 2

    for i in range(2, max_range):
        if num % i == 0:
            if isPrime(i):
                print(i)

#factor(600851475143)
