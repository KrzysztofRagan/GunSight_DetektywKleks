from os import kill
import pygame
from pygame.locals import *

class Crosshair(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super(Crosshair, self).__init__()
    self.x = x
    self.y = y
    self.surf = pygame.image.load("/Users/krzysztofragan/Desktop/vscode/DetektywKleks_gra/images/celownik.png").convert_alpha()
    self.surf = pygame.transform.scale(self.surf, (30,30))
    self.rect = self.surf.get_rect()