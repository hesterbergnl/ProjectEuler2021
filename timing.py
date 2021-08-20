import timeit
from problem6 import difference_squares

start = timeit.default_timer()

# Solution

print(difference_squares(100))

#End

stop = timeit.default_timer()
print('Time: ', stop - start)