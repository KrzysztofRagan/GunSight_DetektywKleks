from numpy import disp
import pygame
from pygame.locals import *
import random
import os


class Player(pygame.sprite.Sprite):
  '''  A class used to represent player. Player can move from left to right. He starts from the middle of the screen. '''

  def __init__(self, x, y):
    '''
    inits sprite object, that is a Player. 
    :param x: x dimension of a Player
    '''
    super(Player, self).__init__()
    self.x = x
    self.y = y
    self.surf = pygame.image.load("/Users/krzysztofragan/Desktop/vscode/DetektywKleks_gra/images/kleks_middle.png").convert()
    self.surf = pygame.transform.scale(self.surf, (221, 300))
    self.rect = self.surf.get_rect(center = (x/2, y-100))



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
    if pygame.mouse.get_pos()[0] < self.rect.centerx - 150:
      # self.surf.fill((0,0,255))
      self.surf = pygame.image.load("/Users/krzysztofragan/Desktop/vscode/DetektywKleks_gra/images/kleks_left.png")
      self.surf = pygame.transform.scale(self.surf, (221,300))
    if pygame.mouse.get_pos()[0] >= self.rect.centerx - 150 and pygame.mouse.get_pos()[0] <= self.rect.centerx + 150:
      self.surf = pygame.image.load("/Users/krzysztofragan/Desktop/vscode/DetektywKleks_gra/images/kleks_middle.png")
      self.surf = pygame.transform.scale(self.surf, (221,300))
    if pygame.mouse.get_pos()[0] > self.rect.centerx + 150:
      self.surf = pygame.image.load("/Users/krzysztofragan/Desktop/vscode/DetektywKleks_gra/images/kleks_right.png")
      self.surf = pygame.transform.scale(self.surf, (221,300))
    

class Ghul(pygame.sprite.Sprite):
  '''
  Ghull class makes ghul enemies. For now they can appear in several random positions in one line.
  '''
  # ghul_movement = [pygame.image.load('../images/ghul_move/ghul_animation-1.png'),
  # pygame.image.load('../images/ghul_move/ghul_animation-1.png'),
  # pygame.image.load('../images/ghul_move/ghul_animation-1.png'),
  # #to potem sie przejdzie przez te rolke: https://coderslegacy.com/python/pygame-rpg-movement-animations/
  # ]

  def __init__(self, x, y, speed, limit, hp):
    super(Ghul, self).__init__() 
    self.x = x
    self.y = y
    self.surf = pygame.image.load("/Users/krzysztofragan/Desktop/vscode/DetektywKleks_gra/images/ghul.png")
    self.surf = pygame.transform.scale(self.surf, (142,200))
    self.rect = self.surf.get_rect(center = (x, y))
    self.speed = speed
    self.limit = limit
    self.hp = hp
    self.move_frame = 0
    self.kill_num = 0



#--------  ENEMIE MOVEMENT ----------
  def update(self):
    self.rect.move_ip(self.speed, 0)
    # if self.speed != 0:
    #   if self.move_frame <= 10:
    #     self.surf = ghul_movement[self.move_frame]
    #     self.move_frame += 1
    #   else:
    #     self.move_frame = 0
    #------ LIMITS IN THE SCREEN EDGES- KILL ENEMIE --------
    if self.rect.left < 0:
      self.kill()
    elif self.rect.right > self.limit:
      self.kill()

# -----------  DAMAGE TO ENEMIE AND KILL ENEMIE -------------
  def hit(self):
    mousepos = pygame.mouse.get_pos()
    # limitations in head coordinates
    if self.rect.collidepoint(mousepos) and mousepos[0] > self.rect.left + 40 and mousepos[0] < self.rect.left + 83 and mousepos[1] < self.rect.top + 42:
      self.kill()
      self.kill_num += 1
    # below the head
    elif self.rect.collidepoint(mousepos) and mousepos[1] >= self.rect.top + 42:

      self.hp = self.hp - 50 
      print(self.hp)       
      if self.hp <= 0:
        self.kill()
        self.kill_num += 1
    return self.kill_num
  
  def count_kills(self):
    return self.kill_num
