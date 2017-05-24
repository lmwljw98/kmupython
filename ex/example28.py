class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def __str__(self):
        msg = self.size + " " + self.color + " " + self.direction
        return msg

myBall = Ball("red","small","down")
print(myBall)
