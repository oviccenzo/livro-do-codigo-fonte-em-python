###operacoes com strings

# '2'-'1'
# ----> 1 '2'-'1'
# TypeError: unsupported operand type(s) for -: 'str' and 'str'

# 'eggs'/'easy'
# ----> 1 'eggs'/'easy'
# # TypeError: unsupported operand type(s) for /: 'str' and 'str'

# "third" * "a charm"
# ----> 1 "third" * "a charm"
# TypeError: can't multiply sequence by non-int of type 'str'

print(str('2 - 1'))
print(str('eggs / easy'))
print(str('"thir" * "a charm"'))