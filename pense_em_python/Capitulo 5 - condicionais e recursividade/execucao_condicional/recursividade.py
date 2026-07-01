#### Recursividade

def countdown(n):
  if n <= 0:
    print("Blastoff!")
  else:
    print(n)
    countdown(n-1)

countdown(3)

print("\n")

def countdown1(n1):
  return n1

countdown1(3)

def countdown2(n2):
  if n2 <= 0:
    print("Blastoff!")
  else:
    print(n2)
    countdown2(n-1)

if __name__ == '__main__':
  countdown(3)

def countdown3(n3):
  return n3

countdown3(3)

n3 = 2
n4 = 0
if n3  > n4:
  print(n3)
  countdown3(n3-1)
  countdown3(n4-2)

def countdown4(n5):
  return n5

countdown4(3)

def countdown5(n6):
  return n6

countdown5(2)

n6 = 1
n7 = 0
if n6  > n7:
  print(n6)
  countdown3(n7-1)
print(countdown5(n7))

def countdown6(n8):
  return n8

countdown6(2)

def countdown7(n9):
  return n9

countdown7(1)

n9 = 0
n10 = 1
if n9  > n10:
  print(n9)
  countdown(n9-1)
print(countdown7(n9))
print(countdown7(n10))