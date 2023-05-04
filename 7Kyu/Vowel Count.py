# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    coll_count = 0
    letters = "aeiou"
    for i in sentence:
        for let in letters:
            if i == let:
                coll_count += 1

    return coll_count
