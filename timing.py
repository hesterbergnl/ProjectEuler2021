import timeit
from problem5 import smallest_multiple

start = timeit.default_timer()

# Solution

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(smallest_multiple(vals))

#End

stop = timeit.default_timer()
print('Time: ', stop - start)