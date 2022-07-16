import pygame
import creature_classes
import activity_classes
from pygame.locals import *
import random
import pygame_gui
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIButton
import json

'''
this is main
'''


pygame.init()

#----------------  DISPLAY SCALLING -------------------------
infostuffs = pygame.display.Info() # gets monitor info
monitor_x, monitor_y = infostuffs.current_w, infostuffs.current_h # puts monitor length and height into variables
disp_x, disp_y = 1920, 1080 # lenght and height of the display
if disp_x > monitor_x: # scales screen down if too long
    disp_y /= disp_x / monitor_x
    disp_x = monitor_x
if disp_y > monitor_y: # scales screen down if too tall
    disp_x /= disp_y / monitor_y
    disp_y = monitor_y

disp_x = int(disp_x) # So resolution does not contain decimals
disp_y = int(disp_y)
# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #define screen size
screen = pygame.display.set_mode((disp_x, disp_y))
running = True

#DISPLAY WIHT CURRENT KILLS
# kill_counter = 0
data = {'kill_counter': 0}
font = pygame.font.Font('freesansbold.ttf', 32)

#SAVING SCORE
try:
  with open('kills_score.txt') as saved_file:
    data = json.load(saved_file)
except:
  print('No score file created yet')
def show_score(x,y):
  score = font.render(f'Kills: {data["kill_counter"]}', True, (255,0,255))
  screen.blit(score, (x,y))




crosshair = activity_classes.Crosshair(disp_x, disp_y)

player = creature_classes.Player(disp_x , disp_y) # player initialization

pygame.mouse.set_visible(False) # setting mouse invisible

#------------- Sprite group ---------------------
enemies_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)



#----- LVL1 ghuls positions ----------------
ghul_x = [disp_x-100, disp_x/2, disp_x-1000, disp_x-300]
ghul_y = disp_y/2

ADDENEMY = pygame.USEREVENT + 1  #making event about adding ghul
pygame.time.set_timer(ADDENEMY, 2000) #each ghul is added after 2s


#Main loop
while running:
  clock = pygame.time.Clock()
  i = 0
  #checking if the user clicked close window
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == K_ESCAPE:
        running = False
    if event.type == ADDENEMY:  
      ghul_speed = random.randrange(-10,10) # set up random speed of ghul "-"" is left, "+" is right 
      ghul = creature_classes.Ghul(random.choice(ghul_x), ghul_y, ghul_speed, disp_x, 100)
      enemies_list.add(ghul)
      all_sprites.add(ghul)  
    if event.type == MOUSEBUTTONDOWN:  # if mouse clicked check if enemie is hit
      ghul.hit()
      data["kill_counter"] += ghul.count_kills()
    if event.type ==pygame.MOUSEMOTION:
      crosshair.rect.center = event.pos
      

    elif event.type == pygame.QUIT:
      with open('kills_score.txt', 'w') as f:
        json.dump(data, f)
      running = False

  pressed_keys = pygame.key.get_pressed() # get all pressed keys
  player.update(pressed_keys) #movement of player
  
  screen.fill((255,255,255))  #creating white color background


  for object in all_sprites: # creating everyone (player and ghuls) on the screen 
    screen.blit(object.surf, object.rect)

  for ghul in enemies_list: # ghuls can move
    ghul.update()

  show_score(10,10)
  screen.blit(crosshair.surf, crosshair.rect) #drawing crosshair as last elemnt to be always on the top
  pygame.display.flip()
  clock.tick(60)
pygame.quit()