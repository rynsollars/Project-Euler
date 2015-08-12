__author__ = 'ryansollars'

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# This program will take about 6 to 8 minutes to run.
import math
import time

num = 2000000
new_list = []
answer = 0


t0 = time.time()
for num in range(2, num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            break
    else:
        new_list.append(num)
        answer = sum(new_list)

t1 = time.time()
total_t = t1 - t0
print answer
print "This program ran in %f seconds" % total_t
