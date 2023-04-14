class Enemy():
    
    def __init__(self,health, speed, x, y, size, displayWidth, displayHeight, score, image, facing, patternStep):
        self.health = health
        self.speed = speed
        self.x = x
        self.y = y
        self.size = size
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.score = score
        self.image = image
        self.facing = facing
        self.patternStep = patternStep

    def move(self, veloX, veloY):
        self.x = self.x + veloX * self.speed
        self.y = self.y + veloY * self.speed

    def takeDmg(self, dmg):
        self.health -= dmg
