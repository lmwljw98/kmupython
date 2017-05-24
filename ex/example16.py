'''
def myFunction():
    print("Function")
    print("OK")

print("Start")
myFunction()
print("End")
'''


'''
def f1():
    print("f1 starts")
    f2()
    print("f1 ends")

def f2():
    print("f2 starts")
    f3()
    print("f2 ends")

def f3():
    print("f3 starts")
    print("f3 ends")

print("Starts")
f1()
print("Ends")
'''


'''
def myAdd(f, l ,r):
    print(f, l)
    print("Room #", r)
    print("Function Ends")

myAdd("JW", "Lee", 909)
myAdd("M", "Yo", 9009)
'''


def mutable(names):
    names.append("Bob")
    names.sort()
    return names
    
pNames = ["Dave", "Alice"]
print("Before :", pNames)
print("In :", mutable(pNames))
print("After :", pNames)

