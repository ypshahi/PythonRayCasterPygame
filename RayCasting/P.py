from R import *
from pygame import Vector2

class Particle:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.FOV = 360
        self.Sensors = []
        self.offsetVar = Vector2()
        self.offset = 90
        for i in range(1, self.FOV + 1):
            vector = Vector2()
            vector.from_polar((20, -i + self.offset))
            ray = Ray(self.posX, self.posY, (0, -1) + vector)
            self.Sensors.append(ray)

    def turn(self, angle):
        self.offset += angle
        self.offsetVar.from_polar((20, self.offset))
        self.Sensors = []
        for i in range(1, self.FOV + 1):
            vector = Vector2()
            vector.from_polar((20, i))
            ray = Ray(self.posX, self.posY, (self.offsetVar) + vector)
            self.Sensors.append(ray)

    def Cast(self, walls, display):

        for ray in self.Sensors:
            closest = ()
            record = 5454544844
            for wall in walls:
                pt = ray.cast(wall, display)
                if pt:
                    d = (pt[0] - ray.x3)**2 + (pt[1] - ray.y4)**2
                    if d < record:
                        record = d
                        closest = pt
            if len(closest) > 1:
                pygame.draw.line(display, (255, 255, 0), (ray.x3, ray.y3), (closest[0], closest[1]), 1)
