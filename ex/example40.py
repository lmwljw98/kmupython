from random import random

n = 10000
inside = 0

for i in range(0,n):
    x = random()
    y = random()

    if x**2 + y**2 <= 1:
        inside += 1

pi = 4*inside/n

print(pi)
