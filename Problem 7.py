__author__ = 'ryansollars'
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import time
num = 110000
new_list = []

t0 = time.time()
for num in range(2, num + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        new_list.append(num)
t1 = time.time()
total_n = t1-t0


print new_list
print len(new_list)
print new_list[10000:10001:]
print ("The program took %s seconds to run!" % total_n)