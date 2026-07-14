def factorial(n11):
    if n11 == 0:
        return 1
    else:
        recurse = factorial(n11-1)
        result3 = n11 * recurse
        return result3


print(factorial(3))
print(factorial(4))
print(factorial(5))

print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(9))
print(factorial(10))