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


bg_image = pygame.image.load('pygame_practice/picture/bg.jpg')
bg_pos_w = 0 # 배경을 움직이기 위해서 만듬
bg_pos_h = 0
bg_to_w = 0
bg_to_h = 0

player = Player(WIDTH, HEIGHT)

bullets_red = []
for _ in range(7):
  bullets_red.append(Bullet(0, HEIGHT * rnd.random(), rnd.random() - 0.5, rnd.random() - 0.5))

bullets_blue = []
for _ in range(3): # 파란색 총알은 3개부터 시작한다
  bullets_blue.append(Bullet(0, HEIGHT * rnd.random(), rnd.random() - 0.5, rnd.random() - 0.5))

bullets_white = []
for _ in range(1): # 흰색 총알은 1개 부터 시작한다
  bullets_white.append(Bullet(0, HEIGHT * rnd.random(), rnd.random() - 0.5, rnd.random() - 0.5))

time_for_adding_bullets = 0
time_for_adding_bullets_blue = 0 # 시간이 지남에 따라 파란색 총알을 증가시키기 위해 만듬
time_for_adding_bullets_white = 0 # 시간이 지남에 따라 흰색 총알을 증가시키기 위해 만듬

play_time = 0

clock.tick(FPS)

pygame.mixer.music.load('pygame_practice/sound/bgm.wav') 
pygame.mixer.music.play(-1)
collision_sound = pygame.mixer.Sound('pygame_practice/sound/shot.wav') # 충돌시 생기는 효과음을 가져옴

explosion = pygame.image.load('pygame_practice/picture/explosion.png') # 충돌시 생기는 터지는 그림을 가져옴
explosion = pygame.transform.scale(explosion, (120, 120)) # 그림의 크기를 비행기 보다 조금더  크게 설정함

life = 5 # 목숨을 5개로 설정함
k = -3 # 무적시간을 3초로 설정해주기 위해 -3으로 설정함
invin = False # 플레이어의 현재 상태가 무적인지 아닌지를 판단하기 위해서 만듬 True면 무적상태이고 False면 무적상태가 아니다
life_bar = 150 # 목숨을 나타내는 막대기의 길이 값
bullet_add_cnt = 0
x = 0
running = True
gameover = False

while running:

  dt = clock.tick(FPS)

  if gameover == False:
    play_time += dt
    time_for_adding_bullets += dt
    time_for_adding_bullets_blue += dt
    time_for_adding_bullets_white += dt
    if time_for_adding_bullets >= 3000:
      bullets_red.append(Bullet(0, HEIGHT * rnd.random(), rnd.random() - 0.5, rnd.random() - 0.5))
      time_for_adding_bullets -= 3000
    if time_for_adding_bullets_blue >= 6000: # 6초마다 파란색 총알 추가
      bullets_blue.append(Bullet(0, HEIGHT * rnd.random(), rnd.random() - 0.5, rnd.random() - 0.5))
      time_for_adding_bullets_blue -= 6000
    if time_for_adding_bullets_white >= 10000: # 10초마다 흰색 총알 추가
      bullets_white.append(Bullet(0, HEIGHT * rnd.random(), rnd.random() - 0.5, rnd.random() - 0.5))
      time_for_adding_bullets_white -= 10000
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        player.goto(1, 0)
        bg_to_w -= dt * 0.05 # 플레이어가 누르는 방향키에 반응하여 배경을 움직이기 위함
      elif event.key == pygame.K_LEFT:
        player.goto(-1, 0)
        bg_to_w += dt * 0.05
      elif event.key == pygame.K_UP:
        player.goto(0, -1)
        bg_to_h -= dt * 0.05
      elif event.key == pygame.K_DOWN:
        player.goto(0, 1)
        bg_to_h += dt * 0.05
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        player.goto(-1, 0)
        bg_to_w += dt * 0.05
      elif event.key == pygame.K_LEFT:
        player.goto(1, 0)
        bg_to_w -= dt * 0.05
      elif event.key == pygame.K_UP:
        player.goto(0, 1)
        bg_to_h += dt * 0.05
      elif event.key == pygame.K_DOWN:
        player.goto(0, -1)
        bg_to_h -= dt * 0.05   

  screen.fill((0, 0, 0))
  bg_pos_w += bg_to_w # 방향기를 누를 상태에 따라 배경이 지속적으로 이동함
  bg_pos_h += bg_to_h
  screen.blit(bg_image, (bg_pos_w, bg_pos_h)) # 상하로도 배경이 움직이기 위해 bg_pos_h를 넣어줌
  player.update(dt,screen)
  player.draw(screen, invin) # invin을 넣어서 플레이어의 무적 상태를 확인해 준다.

  for b in bullets_red:
    b.update_and_draw(dt, screen)
  for b2 in bullets_blue: # 파란색 총알을 그린다
    b2.update_and_draw_blue(dt, screen)
  for b3 in bullets_white: # 흰색 총알을 그린다
    b3.update_and_draw_white(dt, screen)
  txt = f"Time : {play_time/1000:.1f}, Bullets : {len(bullets_red)+len(bullets_blue)+len(bullets_white)}" # 빨강, 파랑, 희색의 총알의 수를 모두 더하여 출력한다 
  draw_text(txt, 32, (10, 10), (255,255,255))
  draw_text(f"Life : {str(life)}", 32, (10, 50), (255, 255, 255)) # 남은 목숨의 수를 출력한다.
  pygame.draw.rect(screen, (255, 255, 255), [10, 100, life_bar, 30]) # 남은 목숨을 막대기 형태로 표현한다

  if gameover:
    txt = "Game Over"
    draw_text(txt, 100, (WIDTH/2 - 300 , HEIGHT/2 - 50), (255, 255, 255))
    running = False
  pygame.display.update()

  if play_time//1000 >= k + 3: #충돌시 시간에서 3초가 흐른후에 충돌여부를 확인 할 수 있게 만듬
    invin = False
    for b in bullets_red:
      if collision(player, b):
        collision_sound.play() # 충돌시 효과음을 불러옴
        screen.blit(explosion, player.calibpos()) #충돌시 플레이어의 위치에 터지는 그림효과가 나타난다.
        pygame.display.update() #터지는 그림효과를 볼 수 있게하기 위함
        life -= 1 # 충돌시 생명을 1개 감소함
        life_bar -= 30
        k = play_time//1000 # 충돌시 시간을 측정함
    for b2 in bullets_blue: # 파란색 총알과 충돌하는 경우
      if collision(player, b2):
        collision_sound.play()
        screen.blit(explosion, player.calibpos()) 
        pygame.display.update() 
        life -= 2 # 충돌시 생명을 2개 감소함
        life_bar -= 60
        k = play_time//1000
    for b3 in bullets_white: # 흰색 총알과 충돌하는 경우
      if collision(player, b3):
        collision_sound.play()
        screen.blit(explosion, player.calibpos()) 
        pygame.display.update() 
        life -= 3 # 충돌시 생명을 3개 감소함
        life_bar -= 90
        k = play_time//1000 
      if life == 0:
          gameover = True
  else: 
    invin = True

time.sleep(1)
