a = int(input('a : '))
b = int(input('b : '))

if a < b:
    a,b = b,a
    
if b == 0:
    print(a)

else:
    while b > 0:
        
        '''
        x = a
        a = b
        b = x % b
        '''
        
        a, b = b, a%b
        
    print('최대공약수 :',a)
    
