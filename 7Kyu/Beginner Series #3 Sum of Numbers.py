# Given two integers a and b, which can be positive or negative, find the sum of all the integers between
# and including them and return it. If the two numbers are equal return a or b.
#
# Note: a and b are not ordered!

def get_sum(a, b):
    summ = 0
    if a < b:
        for i in range(a, b + 1):
            summ += i
        return summ
    elif a == b:
        return a
    else:
        for i in range(b, a + 1):
            summ += i
        return summ
