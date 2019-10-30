from random import randint
import pygame
from math import sin, cos, radians, degrees, atan2, ceil


def rotate_center(surface, angle, pos):
    to_draw = pygame.transform.rotate(surface, angle)
    new_rect = to_draw.get_rect(center=surface.get_rect(topleft=(pos[0], pos[1])).center)
    return to_draw, new_rect


class Drop:
    def __init__(self, pos=(None, None), angle=0, vel=80, color=(255, 255, 255)):
        self.x, self.y = pos

        self.width = randint(2, 5)
        self.height = self.width * 20

        if self.x is None:
            self.x = randint(-500, 1780)
        if self.y is None:
            self.y = -self.height
        self.x_vel, self.y_vel = 0, 0
        self.vel = vel * (self.width / 5)
        self.angle = angle

        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.surface.fill(color)
        self.color = color
        self.ticks = 0

        self.dead = False

        self.gravity = 2.5

    def move(self):
        self.x_vel = cos(radians(self.angle)) * self.vel
        self.y_vel = sin(radians(self.angle)) * self.vel

        self.x += self.x_vel
        self.y -= self.y_vel

        self.y_vel -= 2.5
        self.angle = degrees(atan2(self.y_vel, self.x_vel))

        if self.y > 800:
            self.dead = True

        self.ticks += 1

    def set_vel(self, vel):
        self.vel = vel * (self.width / 5)
        self.x_vel = cos(radians(self.angle)) * self.vel
        self.y_vel = sin(radians(self.angle)) * self.vel

    def draw(self, surface):
        to_draw, new_rect = rotate_center(self.surface, self.angle + 90, (self.x, self.y))
        surface.blit(to_draw, new_rect)

