import pygame
import creature_classes
import activity_classes
from pygame.locals import *
import random




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

enemies_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)



#----- LVL1 ghuls positions ----------------
ghul_x = [disp_x-100, disp_x/2, disp_x-1000, disp_x-300]
ghul_y = disp_y/2

ADDENEMY = pygame.USEREVENT + 1  #making event about adding ghul
pygame.time.set_timer(ADDENEMY, 2000) #each ghul is added after 2s


#Main loop
while running:
  i = 0
  #checking if the user clicked close window
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == K_ESCAPE:
        running = False
    if event.type == ADDENEMY:  
        ghul_speed = random.randrange(-15,15) # set up random speed of ghul "-"" is left, "+" is right 
        ghul = creature_classes.Ghul(random.choice(ghul_x), ghul_y, ghul_speed, disp_x)
        enemies_list.add(ghul)
        all_sprites.add(ghul)

    elif event.type == pygame.QUIT:
      running = False

  pressed_keys = pygame.key.get_pressed() # get all pressed keys
  player.update(pressed_keys) #movement of player
  
  screen.fill((255,255,255))  #creating white color background


  for object in all_sprites: # creating everyone (player and ghuls) on the screen 
    screen.blit(object.surf, object.rect)

  for ghul in enemies_list: # ghuls can move
    ghul.update()
  pygame.display.flip()
pygame.quit()