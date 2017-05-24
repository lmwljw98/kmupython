a = "Kookmin Univ. is leading computer science".split()

print(a)
a.sort()
print(a)
a.sort(key=str.upper)
print(a)
a.sort(key=str.upper, reverse=True)
print(a)
