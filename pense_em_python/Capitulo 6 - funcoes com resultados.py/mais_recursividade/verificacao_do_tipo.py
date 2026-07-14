def factorial1(n12):
    if n12 == 0:
        return 1
    else:
        recurse1 = factorial1(n12-1)
        result4 = n12 * recurse1
        return result4

print(factorial1(11))
print(factorial1(12))
print(factorial1(13))
print(factorial1(14))
print(factorial1(21))