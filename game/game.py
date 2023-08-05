import pygame
import sys
pygame.init()

width=800
height=600
red=(255,0,0)
player_pos = [400, 300]
player_size=50
screen=pygame.display.set_mode((width,height))

game_over = False

while not game_over:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

    if event.type == pygame.KEYDOWN:
      x = player_pos[0]
      y = player_pos[1]
      if event.key == pygame.K_LEFT:
        x -= 5
      elif event.key == pygame.K_RIGHT:
        x += 5
      
      player_pos = [x,y]
  pygame.draw.rect(screen, red, (player_pos[0],player_pos[1],player_size,player_size))
  
  pygame.display.update()