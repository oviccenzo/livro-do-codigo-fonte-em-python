def factorial2(n13):
    if not isinstance(n13, int):
        print("Factorial is only defined for positive integers.")
        return None
    elif n13 < 0:
        print("Factorial is not defined for negative integers")
        return None
    elif n13 == 0:
        return 1
    else:
        return n13 * factorial2(n13-1)

print(factorial2("Fred"))
print(factorial2(21))
print(factorial2(-21)) 