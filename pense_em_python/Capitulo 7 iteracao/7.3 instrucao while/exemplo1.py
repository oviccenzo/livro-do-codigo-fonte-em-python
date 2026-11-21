def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Blastoff!")

print(countdown)

def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:        # n é par
            n = n / 2
        else:                 # n é ímpar
            n = n * 3 + 1

print(sequence(20))