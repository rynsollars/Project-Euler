__author__ = 'ryansollars'
# #The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

n = 6081534
i = 2
import math
while i <= math.sqrt(n):
    if n % i == 0:
        n = n / i
    i = i + 1
print n