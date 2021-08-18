def reverse(num):
    rev = 0
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev


def palindrome(num):
    """Palindrome takes a number of digits in a number and finds the largest palindrome"""
    """that is a multiple of two numbers of that size"""
    max_num = pow(10, num)
    max_palindrome = 0;
    x = y = max_num - 1
    for i in range(x, 1, -1):
        for j in range(y, 1, -1):
            val = i * j
            if val == reverse(val):
                if(max_palindrome < val):
                    max_palindrome = val

    return max_palindrome


print(palindrome(3))