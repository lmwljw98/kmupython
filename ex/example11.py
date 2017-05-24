'''
for a in range (4,7):
    for i in range (1,10):
        print(a, "x", i ,"=", a * i)
    print("\n")
'''

'''
for i in range (10):
    for j in range(10):
        print('*', end='')
    print()
'''

i = 0

while(i < 10):
    j = 0
    while(j < 10):
        print('*', end='')
        j+=1
    print()
    i+=1
