from pygame.math import Vector2
from pygame.transform import rotozoom

from utils import *


class GameObject:
  def __init__(self, position, sprite, velocity):

    self.sprite = sprite
    self.radius = sprite.get_width() / 2  # image radius used to check collision
    
    self.position = Vector2(position)
    self.velocity = Vector2(velocity)

  def draw(self, surface):
    surface.blit(self.sprite, self.position - Vector2(self.radius))

  def move(self, surface):
    self.position = wrap_position(self.position + self.velocity, surface)

  def check_collision(self, other):
    return self.position.distance_to(other.position) < self.radius + other.radius
