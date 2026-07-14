def factorial3(n14):
    space = '  ' * (4 * n14)
    print(space, 'factorial',n14)
    if n14 == 0:
        print(space ,"returning 1")
        return 1
    else:
        recurse2 = factorial3(n14-1)
        result5 = n14 * recurse2
        print(space ,"returning", result5)
        return result5

print(factorial3(8))