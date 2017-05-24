# 20171676 이정우

'''
list = []

x = int(input('1번 변의 길이를 입력해주세요. : '))
y = int(input('2번 변의 길이를 입력해주세요. : '))
z = int(input('3번 변의 길이를 입력해주세요. : '))

while x < 1 or y < 1 or z < 1:
    print("양수만 입력 가능합니다.")
    x = int(input('1번 변의 길이를 입력해주세요. : '))
    y = int(input('2번 변의 길이를 입력해주세요. : '))
    z = int(input('3번 변의 길이를 입력해주세요. : '))

list.append(x)
list.append(y)
list.append(z)

list.sort()

if list[2] < list[0] + list[1]:
    if list[2] ** 2 == list[0] ** 2 + list[1] ** 2:
        print('1. \n직각삼각형 입니다.')

    elif list[2] ** 2 < list[0] ** 2 + list[1] ** 2:
        print('0. \n예각삼각형 입니다.')

    elif list[2] ** 2 > list[0] ** 2 + list[1] ** 2:
        print('2. \n둔각삼각형 입니다.')

elif list[2] >= list[0] + list[1]:
    print('3. \n삼각형이 성립되지 않습니다.')
'''

x = int(input('1번 변의 길이를 입력해주세요. : '))
y = int(input('2번 변의 길이를 입력해주세요. : '))
z = int(input('3번 변의 길이를 입력해주세요. : '))

while x < 1 or y < 1 or z < 1:
    print("양수만 입력 가능합니다.")
    x = int(input('1번 변의 길이를 입력해주세요. : '))
    y = int(input('2번 변의 길이를 입력해주세요. : '))
    z = int(input('3번 변의 길이를 입력해주세요. : '))


# x y z 크기 순으로 정렬

if y > x and y > z:
    x, y = y, x

if z > x and z > y:
    x, z = z, x

if z > y:
    y, z = z, y
    

if x < y + z:
    if x ** 2 == y ** 2 + z ** 2:
        print('1. \n직각삼각형 입니다.')

    elif x ** 2 < y ** 2 + z ** 2:
        print('0. \n예각삼각형 입니다.')

    elif x ** 2 > y ** 2 + z ** 2:
        print('2. \n둔각삼각형 입니다.')

# elif x >= y + z:
else:
    print('3. \n삼각형이 성립되지 않습니다.')
