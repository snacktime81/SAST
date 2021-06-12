import pygame
from player import Player
import random as rnd
from bullet import Bullet
import math
import time

def collision(obj1, obj2):
  dist = ((obj1.pos[0] - obj2.pos[0]) ** 2 + (obj1.pos[1] - obj2.pos[1]) ** 2)
  if math.sqrt(dist) < 20: return True
  else: return False

def draw_text(txt, size, pos, color):
  font = pygame.font.Font('freesansbold.ttf', size)
  r = font.render(txt, True, color)
  screen.blit(r, pos)


pygame.init()
WIDTH, HEIGHT = 1000, 800

clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption("bullet avoid")
screen = pygame.display.set_mode((WIDTH, HEIGHT))


bg_image = pygame.image.load('/home/user/바탕화면/수업 자료/과학과 소프트웨어적 사고/총알피하기/bg.jpg')
bg_pos = 0

player = Player(WIDTH, HEIGHT)

bullets = []
for _ in range(10):
  bullets.append(Bullet(0, HEIGHT * rnd.random(), rnd.random() - 0.5, rnd.random() - 0.5))

time_for_adding_bullets = 0
play_time = 0

time.sleep(3)
clock.tick(FPS)

pygame.mixer.music.load('/home/user/바탕화면/수업 자료/과학과 소프트웨어적 사고/총알피하기/bgm.wav')
pygame.mixer.music.play(-1)

x = 0
running = True
gameover = False

while running:

  dt = clock.tick(FPS)

  if gameover == False:
    play_time += dt
    time_for_adding_bullets += dt
    if time_for_adding_bullets >= 3000:
      bullets.append(Bullet(0, HEIGHT * rnd.random(), rnd.random() - 0.5, rnd.random() - 0.5))
      time_for_adding_bullets -= 3000 


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        player.goto(1, 0)
      elif event.key == pygame.K_LEFT:
        player.goto(-1, 0)
      elif event.key == pygame.K_UP:
        player.goto(0, -1)
      elif event.key == pygame.K_DOWN:
        player.goto(0, 1)
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        player.goto(-1, 0)
      elif event.key == pygame.K_LEFT:
        player.goto(1, 0)
      elif event.key == pygame.K_UP:
        player.goto(0, 1)
      elif event.key == pygame.K_DOWN:
        player.goto(0, -1)      

  screen.fill((0, 0, 0))
  screen.blit(bg_image, (bg_pos, 0))
  bg_pos -= dt * 0.01
  player.update(dt,screen)
  player.draw(screen)

  for b in bullets:
    b.update_and_draw(dt, screen)

  txt = f"Time : {play_time/1000:.1f}, Bullets : {len(bullets)}"
  draw_text(txt, 32, (10, 10), (255,255,255))

  if gameover:
    txt = "Game Over"
    draw_text(txt, 100, (WIDTH/2 - 300 , HEIGHT/2 - 50), (255, 255, 255))
    running = False
  pygame.display.update()

  for b in bullets:
    if collision(player, b):
      
      gameover = True


time.sleep(1)
