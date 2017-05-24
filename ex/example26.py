import os

path = "/home/leejungwoo/"

dir = []
files = []

for a in os.listdir(path):
    full_name = path + a
    if os.path.isdir(full_name):
        dir.append(full_name + "/")
    else:
        files.append(full_name)
print(dir)
print(files)

