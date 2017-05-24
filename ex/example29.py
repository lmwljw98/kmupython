class NumBox:
    def __init__(self, num):
        self.Num = num

    def __add__(self, num):
        self.Num += num

n = NumBox(1)
print(n + 20)
