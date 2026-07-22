####Condição aninhadas

x7 = int(input("Digite qualquer número: "))
y7 = int(input("Digite qualquer número: "))

if x7 == y7:
  print("x and y are equal")
else:
  if x7 < y7:
    print("x is less than y")
  else:
    print("x is greater than y")

x8 = int(input("Digite qualquer número: "))

if 0 < x8:
  if x8 < 10:
    print("x is a positive single-digit number")

x9 = int(input("Digite qualquer número: "))

if 0 < x9 and x9 < 10:
  print("x is a positive single-digit number")

x10 = int(input("Digite qualquer número: "))

if 0 < x10 < 10:
  print("x is a positive single-digit number")