class Ball:
    direction = 'default'

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

myBall = Ball()

myBall.direction = "down"
myBall.bounce()

yourBall = Ball()
myBall.size = 10

myBall.__class__.direction = 'stop'
print(myBall.direction, myBall.size, myBall.__class__.direction)
