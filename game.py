import pygame

from asteroid import Asteroid
from spaceship import Spaceship

from utils import *


class Game:
  MIN_DISTANCE = 250

  def __init__(self):
    self.init_window()

    self.clock = pygame.time.Clock()

    self.screen = pygame.display.set_mode((800, 600))
    self.background = load_sprite("space", False)

    self.font = pygame.font.Font("assets/fonts/press_start.ttf", 40)
    self.message = ""
    
    self.asteroids = list()
    self.bullets = list()
    self.spaceship = Spaceship((400, 300), self.bullets.append)

    for i in range(6):
      while True:
        position = random_position(self.screen)

        if position.distance_to(self.spaceship.position) > self.MIN_DISTANCE:
          break

      self.asteroids.append(Asteroid(position, self.asteroids.append))

  def init_window(self):
    pygame.init()
    pygame.display.set_caption('Asteroids')

  def handle_input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          quit()

        if event.key == pygame.K_SPACE and self.spaceship:
          self.spaceship.shoot()

    is_pressed = pygame.key.get_pressed()

    if self.spaceship:
      if is_pressed[pygame.K_LEFT]:
        self.spaceship.rotate(clockwise=False)

      if is_pressed[pygame.K_RIGHT]:
        self.spaceship.rotate(clockwise=True)

      if is_pressed[pygame.K_UP]:
        self.spaceship.accelerate()

  def game_logic(self):
    for game_object in self.get_game_objects():
      game_object.move(self.screen)

    if self.spaceship:
      for asteroid in self.asteroids:
        if asteroid.check_collision(self.spaceship):
          self.spaceship = None
          self.message = 'GAME OVER ;-;'
          break
    
    for bullet in self.bullets.copy():
      for asteroid in self.asteroids.copy():
        if asteroid.check_collision(bullet):
          self.asteroids.remove(asteroid)
          self.bullets.remove(bullet)
          asteroid.split()
          break

    for bullet in self.bullets.copy():
      if not self.screen.get_rect().collidepoint(bullet.position):
        self.bullets.remove(bullet)

    if self.spaceship and not self.asteroids:
      self.message = 'VICTORY :)'

  def draw(self):
    self.screen.blit(self.background, (0, 0))

    for game_object in self.get_game_objects():
      game_object.draw(self.screen)

    if self.message:
      print_text(self.screen, self.message, self.font)

    pygame.display.flip()
    self.clock.tick(60)

  def get_game_objects(self):
    game_objects = [*self.asteroids, *self.bullets]

    if self.spaceship:
      game_objects.append(self.spaceship)

    return game_objects

  def game_loop(self):
    while True:
      self.handle_input()
      self.game_logic()
      self.draw()

Game().game_loop()
