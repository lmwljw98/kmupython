import datetime

list = ['월','화','수','목','금','토','일']

def week(y,m,d):
    
    try:
        a = datetime.date(int(y), int(m), int(d))

    except:
        print("Error. Try Again.")
        y = input('몇 년? : ')
        m = input('몇 월? : ')
        d = input('몇 일? : ')
    
        week(y,m,d)

        return 0

    print(y + '년 ' + m + '월 ' + d + '일은 ' + list[a.weekday()] + '요일입니다')
    return 0


print('Start Program')

y = input('몇 년? : ')
m = input('몇 월? : ')
d = input('몇 일? : ')
    
week(y,m,d)
