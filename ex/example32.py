def divide(m,n):
    try:
        result = m/n
    except ZeroDivisionError:
        print("0 나누기 X")

    except:
        print("다른 오류")

    else:
        return result

    finally:
        print("나눗셈")

if __name__ == '__main__':
    res = divide(3,2)
    print(res)
    res = divide(10,0)
    print(res)
    print(divide(200,3))
