def exp(g, m):
    return(g(m))

f1 = lambda x: x**2

f2 = lambda x: x**3

n = 5

print(n, f1(n))
print(n, f2(n))
print(n, exp(f1, n))
print(n, exp(f2, n))
