import pygame
from pygame import Vector2


class Ray():

    def __init__(self, x3, y3, dir):
        self.x3 = x3
        self.y3 = y3
        self.dirx = dir[0]
        self.diry = dir[1]
        self.x4 = self.x3 + self.dirx *10
        self.y4 = self.y3 + self.diry *10

    def show(self, display):
        pygame.draw.circle(display, (255, 255, 255), (self.x3, self.y3), 5)
        pygame.draw.line(display, (255, 255, 255), (self.x3, self.y3), (self.x4, self.y4))



    def cast(self, wall, display):
        x1 = wall.x1
        y1 = wall.y1
        x2 = wall.x2
        y2 = wall.y2
        x3 = self.x3
        y3 = self.y3
        x4 = self.x4
        y4 = self.y4

        den = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)

        if den == 0:
            return

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den

        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if 0 < t < 1 and u > 0:
            px = x1 + t * (x2 -x1)
            py = y1 + t * (y2 - y1)

            return px, py





