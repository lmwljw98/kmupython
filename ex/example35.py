import pickle

'''
my_list = ["Lee", "20171676", 95]
f = open('testfile.dat', 'wb')
pickle.dump(my_list, f)
f.close()
'''

f = open('testfile.dat', 'rb')
my_list = pickle.load(f)
print(my_list)
f.close()
