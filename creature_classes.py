import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super(Player, self).__init__()
    self.surf = pygame.Surface((75,50))
    self.surf.fill((0, 0, 0))
    self.rect = self.surf.get_rect()


  def update(self, pressed_keys):
    if pressed_keys[K_a]:
      self.rect.move_ip(-20, 0)
    if pressed_keys[K_d]:
      self.rect.move_ip(20, 0)