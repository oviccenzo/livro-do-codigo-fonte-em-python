##Funções booleanos

####Retornando a funções booleanos

def is_divisible(x19, y19):
  if x19 % y19 == 0:
    return True
  else:
    return False

print(is_divisible(6,4))
print(is_divisible(6,3))

def is_divisible1(x20, y20):
  return x20 % y20 == 0
print(is_divisible1(6,4))
print(is_divisible1(6,3))

###Funções booleanos incondicionais

def is_divisible2(x21,y21):
  print("x is divisible by y")
  return x21 % y21 == 0

print(is_divisible2(6,4))
print(is_divisible2(6,3))

def is_divisible3(x22,y22):
  if x22 % y22 == True:
    print("x is divisible by y")

def is_between(x,y,z):
  return x <= y <= z

print(is_between(8,9,11))