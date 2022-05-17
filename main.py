import pygame
import creature_classes
import activity_classes
from pygame.locals import *




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


player = creature_classes.Player(disp_x , disp_y) # player initialization




#Main loop
while running:

  #checking if the user clicked close window
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == K_ESCAPE:
        running = False
    
    elif event.type == pygame.QUIT:
      running = False

  pressed_keys = pygame.key.get_pressed() # get all pressed keys
  player.update(pressed_keys) #movement of player
  
  screen.fill((255,255,255))  #creating white color background

  screen.blit(player.surf, player.rect) #visualisation of player

  pygame.display.flip()

pygame.quit()