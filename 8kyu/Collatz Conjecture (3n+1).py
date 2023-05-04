#Task
#
# Your task is to make a function hotpo that takes a positive n as input and
# returns the number of times you need to perform this algorithm to get n = 1.


def hotpo(n):
    i = 1
    b = 0
    while n != i:
        if n % 2 == 0:
            n = n // 2
            b += 1
        else:
            n = n * 3 + 1
            b += 1
    return b
