__author__ = 'ryansollars'
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import time

t1 = time.time()

prod = 1

for a in xrange(1000):
    for b in xrange(1000):
        if a < b:
            c = 1000 - a - b
            if a < b < c:
                if a+b+c == 1000:
                    if a**2 + b**2 == c**2:
                        prod = a * b * c
                        print prod
t2 = time.time()
total_t = t2 - t1
print "This program took %f seconds to run" % total_t