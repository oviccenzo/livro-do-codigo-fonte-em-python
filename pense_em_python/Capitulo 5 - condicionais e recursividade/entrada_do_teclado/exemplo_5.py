prompt1 = "what...is the airspeed velocity of an unladen swallow?\n"
speed1 = input(prompt1)
int(speed1)
# 1 prompt1 = "what...is the airspeed velocity of an unladen swallow?\n"
#       2 speed1 = input(prompt1)
# ----> 3 int(speed1)

# ValueError: invalid literal for int() with base 10: 'What do you mean, an African or a European swallow?'
# mostra esse sinal de erro  prompt1 = "what...is the airspeed velocity of an unladen swallow?\n"
#       2 speed1 = input(prompt1)
# ----> 3 int(speed1)
#       4 # 1 prompt1 = "what...is the airspeed velocity of an unladen swallow?\n"
#       5       # 2 speed1 = input(prompt1)
#
# ValueError: invalid literal for int() with base 10: 'int(speed1)'