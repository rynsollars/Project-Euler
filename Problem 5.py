__author__ = 'ryansollars'

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#

divisor_range = range(1, 21)
count = 1
answer = []

# def number_is_divisible_by_range(num):
#     if num % 2 == 0 and num % 3 == 0 and num % 4 == 0 and num % 5 == 0 and num % 6 == 0 and num % 7 == 0 and num % 8 == 0 and num % 9 == 0 and num % 10 == 0 and num % 11 == 0 and num % 12 == 0 and num % 13 == 0 and num % 14 == 0 and num % 15 == 0 and num % 16 == 0 and num % 17 == 0 and num % 18 == 0 and num % 19 == 0 and num % 20 == 0:
#         return True
#     return False
# Above was my answer before I optimized it.

import time
t0 = time.time()
def number_is_divisible_by_range(num):
    for i in divisor_range:
        if num % i == 0:
            continue
        else:
            return False
    return True

while count < 2000000000:
    for i in divisor_range:
        num = count / i
        count += 2520
        if number_is_divisible_by_range(num):
            answer.append(num)

t1 = time.time()
total_n = t1-t0


print ('Answer found: %s in %s seconds!' % (min(answer), total_n))