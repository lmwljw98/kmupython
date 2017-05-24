from urllib.request import urlopen

f = urlopen('http://www.naver.com/')
print(f.headers)

html = f.read()
print(html)
