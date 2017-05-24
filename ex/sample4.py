import math

sum = 0     # 실제값

n = int(input('n의 값? : '))

for i in range(1, n+1):
    sum = sum + 1.0 / i

    print('n =', i, ', 오차율 =', (math.log(i+1) - sum) / sum)

'''
for n in range(1,101):
    sum = 0
    for i in range(1, n+1):
        sum += 1.0/i

    print((math.log(n+1) - sum) / sum)
'''
    
