__author__ = 'ryansollars'

range1 = range(100, 1000)
range2 = range(100, 1000)

new_values = []

def palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

for x in range1:
    for y in range2:
        num = x * y

        if palindrome(num):
            new_values.append(num)
print max(new_values)




