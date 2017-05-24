import math

n = int(input())

for i in range (2, int(math.sqrt(n))+1):

    if n % i == 0:
        print('not a prime num')
        break
    
else:
    print('prime num')
