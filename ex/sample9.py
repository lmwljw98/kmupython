import time
import random

low = 0
high = 500

iter = 10

a = []

for i in range(iter):
    a.append(random.randint(low,high))

start = time.time()

# a.sort()

for j in range(0, len(a)-1):
    for k in range(0, len(a)-1):
        if a[k] > a[k+1]:
            a[k], a[k+1] = a[k+1], a[k]
            
end = time.time()

print(a)
print(end - start)
