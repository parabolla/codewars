# Complete the function which get an input number n such that n >= 10 and n < 10000, then:
#
# Sum all the digits of n.
# Subtract the sum from n, and it is your new n.
# If the new n is in the list below return the associated fruit, otherwise return back to task 1.


def subtract_sum(numbers):
    fruits = {1: "kiwi", 2: "pear", 10: "apple"}
    i = ""
    for number in str(numbers):
        i += str(number)

    return fruits[int(i)] if int(i) <= 100 else "apple"
