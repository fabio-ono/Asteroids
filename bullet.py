from game_object import GameObject

from utils import *


class Bullet(GameObject):
  def __init__(self, position, velocity):
    super().__init__(position, load_sprite('bullet'), velocity)

  def move(self, surface):
    self.position += self.velocity
