'''
myList = []
myList.append('Alice')
myList.append('Bob')
myList.append('Carole')
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[1:3])

numbers = [1,3,5,7]
print(numbers[-1])
print(numbers[1:3])

print(type(numbers[1]))
print(type(numbers[1:3]))
'''

'''
list = ['a', 'b', 'c', 'd']
list.append('e')
list.insert(1,'z')
list.extend(['f','g','h'])
print(list)
'''

'''
a = ['a','b','c','d','e']
a.remove('c')
del a[1]
x = a.pop()
print(a)
print(x)
'''

'''
a = ['a','b','c','d','e']
print('b' in a)
if 't' in a:
    print("True")
else:
    print("Nope")

if 'a' in a:
    print(a.index('a'))
'''

'''
a = [1,2,3,4]
result = []
for num in a:
    result.append(num *3)
print(result)

b = [1,2,3,4]
result2 = [num2 * 3 for num2 in b]
print(result2)

c = [1,2,3,4]
result3 = [num3 * 3 for num3 in c if num3 % 2 == 0]
print(result3)
'''

'''
alphabet = ['a','d','c','b']
print(alphabet)
alphabet.sort(reverse=True)
print(alphabet)
'''

BobScore = [80,70,90,60]
AliceScore = [90,60,80,75]
CaroleScore = [95,90,95,90]
AllScore = [BobScore, AliceScore, CaroleScore]
print(AliceScore[2])
print(AllScore[1][2])
