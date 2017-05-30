from random import random

inside = 0

f = open("1.zip", "rb")

data = f.read()

n = len(data) // 2

for i in range(0, n*2, 2):
    x = data[i]/255
    y = data[i+1]/255

    if x**2 + y**2 <= 1:
        inside += 1

pi = 4*inside/n
f.close()

print(pi)
