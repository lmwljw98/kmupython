delta = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
x = 10

for i in delta:
    dx = ((x + i)**2 - x**2) / i
    print(dx)

