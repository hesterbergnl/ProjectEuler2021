def sum_of_squares(num):
    """Receives number of natural numbers to sum and returns sum of squares (x^2 + y^2"""
    """Uses theorem for finite series to calculate"""
    return (num * (num + 1) * (2 * num + 1)) / 6


def square_of_sum(num):
    """Receives number of natural numbers to sum and returns square of sum (x+y)^^2"""
    """Uses theorem for finite series to calculate base"""
    return (num * (num + 1) / 2) ** 2


def difference_squares(num):
    """Receives number of natural numbers and returns the difference of squares"""
    """ (x^2 + y^2) - (x + y)^2 """
    return square_of_sum(num) - sum_of_squares(num)
