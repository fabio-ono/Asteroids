from bullet import Bullet

from game_object import GameObject

from pygame.math import Vector2
from pygame.transform import rotozoom

from utils import *


class Spaceship(GameObject):
  ACCELERATION = 0.1
  BULLET_SPEED = ROTATION = 3

  def __init__(self, position, bullet_callback):
    super().__init__(position, load_sprite("spaceship"), Vector2(0))

    self.direction = Vector2(Vector2(0, -1))

    self.bullet_callback = bullet_callback
    self.laser_sound = load_sound('laser')

  def rotate(self, clockwise=True):
    sign = 1 if clockwise else -1
    self.direction.rotate_ip(self.ROTATION * sign)

  def draw(self, surface):
    angle = self.direction.angle_to(Vector2(0, -1))

    rotated_surface = rotozoom(self.sprite, angle, 1)
    rotated_surface_size = Vector2(rotated_surface.get_size())

    surface.blit(rotated_surface, self.position - rotated_surface_size / 2)

  def accelerate(self):
    self.velocity += self.direction * self.ACCELERATION

  def shoot(self):
    bullet = Bullet(self.position, self.direction * self.BULLET_SPEED + self.velocity)
    self.bullet_callback(bullet)
    self.laser_sound.play()
