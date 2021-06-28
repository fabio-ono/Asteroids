from bullet import Bullet

from game_object import GameObject

import random
from pygame.transform import rotozoom

from utils import *


class Alien(GameObject):
    ACCELERATION = 1
    BULLET_SPEED = 3
    ROTATION = 3
    TIME_SHOOT = 100
    BULLET_DIRECTION = Vector2(Vector2(-1, 1))

    def __init__(self, position, bullet_callback, spaceship):
        position = self.generate_position()
        super().__init__(position, load_sprite("alien_ship-sprite"), Vector2(0))
        self.direction = Vector2(Vector2(1, 0))
        self.spaceship = spaceship
        self.bullet_callback = bullet_callback
        self.laser_sound = load_sound('laser')

    def draw(self, surface):
        self.accelerate()

        self.TIME_SHOOT = self.TIME_SHOOT - 1
        if self.TIME_SHOOT == 0:
            self.shoot()

        rotated_surface = rotozoom(self.sprite, 2, 1)
        rotated_surface_size = Vector2(rotated_surface.get_size())

        surface.blit(rotated_surface, self.position - rotated_surface_size / 2)

    def accelerate(self):
        self.velocity = self.direction * self.ACCELERATION

    def shoot(self):
        self.BULLET_DIRECTION = self.generate_bullet_direction()
        self.TIME_SHOOT = 100
        bullet = Bullet(self.position, self.BULLET_DIRECTION * self.BULLET_SPEED + self.velocity)
        self.bullet_callback(bullet)
        self.laser_sound.play()

    def generate_bullet_direction(self):
        if self.spaceship.position[0] > self.position[0] and self.spaceship.position[1] > self.position[1]:
            # 4
            return Vector2(Vector2(1, 1))
        elif self.spaceship.position[0] > self.position[0] and self.spaceship.position[1] < self.position[1]:
            # 2
            return Vector2(Vector2(1, -1))
        elif self.spaceship.position[0] < self.position[0] and self.spaceship.position[1] > self.position[1]:
            # 3
            return Vector2(Vector2(-1, 1))
        elif self.spaceship.position[0] < self.position[0] and self.spaceship.position[1] < self.position[1]:
            # 1
            return Vector2(Vector2(-1 -1))
        else:
            return Vector2(Vector2(0, -1))

    def generate_position(self):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        return Vector2(Vector2(x, y))
