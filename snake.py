class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 1

    def move(self):
        self.x += self.speed
        