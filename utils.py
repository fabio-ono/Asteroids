from pygame.image import load
from pygame.math import Vector2
from pygame.mixer import Sound
from random import randint, randrange

def load_sound(name):
  return Sound("assets/sounds/%s.wav" % name)

def load_sprite(name, with_alpha=True):
  sprite = load("assets/sprites/%s.png" % name)
  return sprite.convert_alpha() if with_alpha else sprite.convert()

def print_text(surface, text, font):
  text_surface = font.render(text, True, (255, 255, 255))
  rect = text_surface.get_rect()
  rect.center = Vector2(surface.get_size()) / 2
  surface.blit(text_surface, rect)

def wrap_position(position, surface):
  x, y = position
  w, h = surface.get_size()
  return Vector2(x % w, y % w)

def random_position(surface):
  return Vector2(randrange(surface.get_width()), randrange(surface.get_height()))

def random_velocity(min_speed, max_speed):
  return Vector2(randint(min_speed, max_speed), 0).rotate(randrange(0, 360))