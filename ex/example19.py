n = 10
sum = 0
for i in range(1,n+1):
    sum += i

print(n, sum)


def sigma(a):
    if a == 1:
        return a
    else:
        return a + sigma(a-1)

a = 10
print(a, sigma(a))
