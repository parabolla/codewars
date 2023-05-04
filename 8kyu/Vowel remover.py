# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

def shortcut(s):
    a = "aeiou"
    b = []
    for i in s:
        if i in a:
            continue
        else:
            b.append(i)
    return "".join(b)
