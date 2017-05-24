dic = {1: "Alice", 2:"Bob", "KMU" : "JJ"}
dic[3] = "Carole"
dic.update({213:"David"})
'''
print(dic)
print(dic["KMU"])
print(dic[1])
'''

for key in dic:
    print(key, "'s value is", dic[key])

for a, value in dic.items():
    print(a,"'s value is", value)
