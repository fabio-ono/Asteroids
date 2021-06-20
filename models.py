from pygame.math import Vector2
from pygame.transform import rotozoom

from utils import load_sound, load_sprite, random_velocity, wrap_position

UP = Vector2(0, -1)

class GameObject:
  def __init__(self, position, sprite, velocity):
    self.position = Vector2(position)
    self.sprite = sprite
    self.radius = sprite.get_width() / 2
    self.velocity = Vector2(velocity)

  def draw(self, surface):
    surface.blit(self.sprite, self.position - Vector2(self.radius))

  def move(self, surface):
    self.position = wrap_position(self.position + self.velocity, surface)

  def check_collision(self, other):
    return self.position.distance_to(other.position) < self.radius + other.radius

class Spaceship(GameObject):
  ACCELERATION = 0.1
  BULLET_SPEED = ROTATION = 3

  def __init__(self, position, bullet_callback):
    super().__init__(position, load_sprite("spaceship"), Vector2(0))
    self.bullet_callback = bullet_callback
    self.direction = Vector2(UP)
    self.laser_sound = load_sound("laser")

  def rotate(self, clockwise=True):
    sign = 1 if clockwise else -1
    self.direction.rotate_ip(self.ROTATION * sign)

  def draw(self, surface):
    angle = self.direction.angle_to(UP)
    rotated_surface = rotozoom(self.sprite, angle, 1)
    rotated_surface_size = Vector2(rotated_surface.get_size())
    surface.blit(rotated_surface, self.position - rotated_surface_size / 2)

  def accelerate(self):
    self.velocity += self.direction * self.ACCELERATION

  def shoot(self):
    bullet = Bullet(self.position, self.direction * self.BULLET_SPEED + self.velocity)
    self.bullet_callback(bullet)
    self.laser_sound.play()

class Asteroid(GameObject):
  def __init__(self, position, asteroid_callback, size=3):
    scale = 0.5 ** (3 - size)
    sprite = rotozoom(load_sprite("asteroid"), 0, scale)
    super().__init__(
      position, sprite, random_velocity(1, 3)
    )
    self.asteroid_callback = asteroid_callback
    self.size = size

  def split(self):
    if self.size > 1:
      for i in range(2):
        asteroid = Asteroid(self.position, self.asteroid_callback, self.size - 1)
        self.asteroid_callback(asteroid)

class Bullet(GameObject):
  def __init__(self, position, velocity):
    super().__init__(position, load_sprite("bullet"), velocity)

  def move(self, surface):
    self.position += self.velocity