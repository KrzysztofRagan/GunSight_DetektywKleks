from numpy import disp
import pygame
from pygame.locals import *



class Player(pygame.sprite.Sprite):
  '''
  Player. Player can move from left to right. He starts from the middle of the screen.
  '''
  def __init__(self, x, y):
    super(Player, self).__init__()
    self.x = x
    self.y = y
    self.surf = pygame.Surface((75,50))
    self.surf.fill((0, 0, 0))
    self.rect = self.surf.get_rect(center = (x/2, y-50))


  def update(self, pressed_keys):
    #----- MOVEMENT --------------
    if pressed_keys[K_a]:         # move to the left if 'a' pressed
      self.rect.move_ip(-10, 0)
    if pressed_keys[K_d]:         # # move to the right if 'd' pressed
      self.rect.move_ip(10, 0)
    #------ LIMITATIONS -------------
    if self.rect.right > self.x:
      self.rect.right = self.x
    if self.rect.left < 0:
      self.rect.left = 0

    #------- PLAYER APPEARANCE CHANGE BEACAUSE OF MOUSE POSITION --------
    if pygame.mouse.get_pos()[0] < self.rect.centerx - 25:
      self.surf.fill((0,0,255))
    if pygame.mouse.get_pos()[0] >= self.rect.centerx - 25 and pygame.mouse.get_pos()[0] <= self.rect.centerx + 25:
      self.surf.fill((0,0,0))
    if pygame.mouse.get_pos()[0] > self.rect.centerx + 25:
      self.surf.fill((255,255,0))
    

    

