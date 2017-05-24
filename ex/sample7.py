import math
import time

input_num = int(input('Your Number : '))

num_list = []

start = time.time()

for i in range(2, input_num+1):
    num_list.append(i)  # 2 ~ input_num 까지의 숫자 리스트 생성

for prime_num in num_list:
    for j in range (2, int(math.sqrt(prime_num))+1):

        if prime_num % j == 0:
            break   # 소수가 아니면 루프 탈출 -------------↑ 맨 위의 for로 이동
                    # break를 만나면 else문 수행 X
        
    else:
        for k in range(2, input_num):

            if prime_num * k > input_num:   # input_num보다 
                break                       # 계산한 수가 크면 루프 탈출
            
            try:    # 일단 소수의 배수들 지워본다.
                num_list.remove(prime_num * k)
                
            except: # 에러나면 (이미 지워진 수를 지우려 할 때) 다시 위로 올라가서 시도
                continue
            
end = time.time()

print(input_num, '이하의 소수 :', num_list)
print('\nElapsed Time : ', end - start, 'Seconds')
