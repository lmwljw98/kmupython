y = int(input('몇 년? : '))
m = int(input('몇 월? : '))
d = int(input('몇 일? : '))

year_to_day = -1
month_to_day = -1

no_list = ['null', 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
list = ['null', 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

week_day = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

for a in range(1, y):
    if a % 4 == 0 or a % 400 == 0 and a % 100 != 0:
        year_to_day += 366 

    else:
        year_to_day += 365 

for b in range(1, m):
    if y % 4 == 0 or y % 400 == 0 and y % 100 != 0:
        month_to_day += list[b]

    else:
        month_to_day += no_list[b]
        
month_to_day += d

print(week_day[(year_to_day + month_to_day) % 7] + '입니다.')
        
