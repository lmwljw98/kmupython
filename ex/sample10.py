def xyz(first, second, third):
    
    list.append(first)
    list.append(second)
    list.append(third)

    list.sort()
    return list

def Triangle():
    if list[2] < list[0] + list[1]:
        
        if list[2] ** 2 == list[0] ** 2 + list[1] ** 2:
            return 1

        elif list[2] ** 2 < list[0] ** 2 + list[1] ** 2:
            return 0

        elif list[2] ** 2 > list[0] ** 2 + list[1] ** 2:
            return 2

    elif list[2] >= list[0] + list[1]:
        return 3

list = []    

x = int(input("첫 번쨰 값 : "))
y = int(input("두 번쨰 값 : "))
z = int(input("세 번쨰 값 : "))

xyz(x, y, z)
print(Triangle())
