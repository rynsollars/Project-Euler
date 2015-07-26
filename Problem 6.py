__athor__ = 'ryansollars'
# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import time
range1 = xrange(101)
new_range = []

t0 = time.time()
for i in range1:
    num1 = i**2
    new_range.append(num1)

for x in range1:
    num2 = (sum(range1))**2

answer = num2 - (sum(new_range))

t1 = time.time()
total_n = t1-t0

print answer
print ("The program took %s seconds to run!" % total_n)