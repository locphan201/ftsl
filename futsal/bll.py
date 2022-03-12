import pygame

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 0
        self.speed = 0
        self.vec = pygame.math.Vector3(0, 0, 0)

    def pos(self):
        return (self.x, self.y, self.z)

    def move(self):
        if self.speed > 0:
            self.x += self.vec.x
            self.y += self.vec.y
            self.z += self.vec.z
            self.vec.scale_to_length(self.speed)

    def change_pos(self, x, y):
        self.x = x
        self.y = y
        self.z = 0

    def change_vec(self, x, y, z):
        self.vec = pygame.math.Vector3(x, y, z)
        self.speed = (x**2 + y**2 + z**2)**0.5
    
    def slow_down(self):
        if self.speed > 0:
            self.speed -= 0.15
        else:
            self.speed = 0
            self.vec = pygame.math.Vector3(0, 0, 0)

    def change_speed(self, dist):
        if dist != 0:
            if dist >= 150:
                self.speed = 150
            else:
                self.speed = dist
            self.vec.scale_to_length(self.speed)