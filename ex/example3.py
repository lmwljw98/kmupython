#   print("1<<3 :", 1<<3)
#   print("8>>3 :", 8>>3)

x = input('숫자를 입력하세요 : ')

n = input('몇 번째 ? : ')

print(n + "th bit of", x, ":", 1 & (int(x)>>int(n)-1))




