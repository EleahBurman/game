import pygame
import random
import sys
pygame.init()

width=800
height=600
red=(255,0,0)
blue=(0,0,255)
black=(0,0,0)
player_size=50
player_pos = [width/2, height-2*player_size]

enemy_size=50
enemy_pos=[random.randint(0,width-enemy_size),0]
screen=pygame.display.set_mode((width,height))

game_over = False
clock=pygame.time.Clock()
while not game_over:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

    if event.type == pygame.KEYDOWN:
      x = player_pos[0]
      y = player_pos[1]
      if event.key == pygame.K_LEFT:
        x -= player_size
      elif event.key == pygame.K_RIGHT:
        x += player_size
      
      player_pos = [x,y]
  
  screen.fill(black)
  if enemy_pos[1] >= 0 and enemy_pos[1] < height:
    enemy_pos[1] += 10
  else:
    enemy_pos[0] = random.randint(0,width-enemy_size)
    enemy_pos[1] = 1
  pygame.draw.rect(screen, blue, (enemy_pos[0],enemy_pos[1], enemy_size, enemy_size))
  pygame.draw.rect(screen, red, (player_pos[0],player_pos[1],player_size,player_size))
  
  clock.tick(30)
  pygame.display.update()