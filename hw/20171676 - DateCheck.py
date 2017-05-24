# 20171676 이정우


# function -------------------------

def total_day(y, m, d, plus): # 당일의 요일이 알고싶다면 plus = 0
    year_to_day = 0
    month_to_day = 0

    for a in range(1, y):
        if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0 :
            year_to_day += 366 

        else:
            year_to_day += 365

    for b in range(1, m):
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 :
            month_to_day += yoon_list[b]

        else:
            month_to_day += no_list[b]

    result = (year_to_day + month_to_day + d + plus) - 1

    return result


def later_check(years, months, days, l_day):

    while l_day - yoon_list[months] > 0 or l_day - no_list[months] > 0:
    
        if (years % 4 == 0 and years % 100 != 0) or years % 400 == 0 :
            l_day -= yoon_list[months]
            months += 1
            if months > 12:
                years += 1
                months = 1
    
        else:
            l_day -= no_list[months]
            months += 1
            if months > 12:
                years += 1
                months = 1
            
    days += l_day

    if no_list[months] == 31 and days > 31:
        days -= 31
        months += 1
        if months > 12:
            years += 1
            months = 1

    elif no_list[months] == 30 and days > 30:
        days -= 30
        months += 1

    elif months == 2 and ((years % 4 == 0 and years % 100 != 0) or years % 400 == 0) and days > 29:
        days -= 29
        months += 1

    elif months == 2 and not(((years % 4 == 0 and years % 100 != 0) or years % 400 == 0)) and days > 28:
        days -= 28
        months += 1
        
    '''    
    index.append(years)
    index.append(months)
    index.append(days)
    '''
    
    return [years, months, days]    # 여러 값 리턴


# variable ---------------------------

no_list = ['null', 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoon_list = ['null', 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

week_day = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

# index = []


# main --------------------------

year = int(input('몇 년? : '))
month = int(input('몇 월? : '))
day = int(input('몇 일? : '))

later_day = int(input('몇 일 뒤? : '))

total = total_day(year, month, day, later_day)

total_y, total_m, total_d = later_check(year, month, day, later_day)

print('\n%d년 %d월 %d일로부터 %d일 후는' %(year, month, day, later_day))
# print('%d년 %d월 %d일' %(index[0], index[1], index[2]), week_day[total % 7] + '입니다.')
print('%d년 %d월 %d일' %(total_y, total_m, total_d), week_day[total % 7] + '입니다.')
