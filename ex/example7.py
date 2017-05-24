'''
score = int(input('Your Score : '))

if 90 <= score <= 100 : print("your score is", score, ", grade is A")

elif 80 <= score < 90 : print("your score is", score, ", grade is B")

elif 70 <= score < 80 : print("your score is", score, ", grade is C")

elif 60 <= score < 70 : print("your score is", score, ", grade is D")

else: print("your score is", score, ", grade is F")
'''

'''

age = int(input("age : "))
score = float(input("score : "))

if age > 19 and score > 90.0:

    print("success")

else:
    print("end")

'''

a = int(input('몇 년? : '))

#   if a % 4 == 0 or a % 400 == 0 and not(a % 100 == 0):

if a % 4 == 0 or a % 400 == 0 and a % 100 != 0:
    print("%d년은 윤년입니다." %a)

else:
    print("%d년은 윤년이 아닙니다." %a)
