a = 23 # 16 + 4 + 2 + 1
b = 5 #       4 +     1
    
print("a & b=", a & b, "binary=", bin(a & b))   # 비트 논리곱 - (1, 1) 일때만 1

print("a | b=", a | b, "binary=", bin(a | b))   # 비트 논리합 - (0, 0) 일때만 0

print("a ^ b=", a ^ b, "binary=", bin(a ^ b))   # 비트 XOR - 다르면 1 같으면 0

print("~b=", ~b, "binary=", bin(~b & 0xFFFFFFFF))   # 비트 부정

#   0b = 앞의 0을 생략하고 뒤의 숫자가 2진수라는 의미
#   비트 논리 연산자는 각 자리마다 비교하여 나타냄
