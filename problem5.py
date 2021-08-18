def product(nums = []):
    prod = 1
    for i in nums:
        prod *= i
    return prod


def smallest_multiple(nums = []):
    prod = product(nums)
    lowest_multiple = prod

    for i in range(max(vals), prod, max(vals)):
        flag = True
        for j in nums:
            if i % j != 0:
                flag = False
                break

        if flag:
            return i


vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#print(smallest_multiple(vals))