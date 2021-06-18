import pygame

class Player:
  def __init__(self, x, y):
    self.image = pygame.image.load('pygame_practice/picture/player.png')
    self.image = pygame.transform.scale(self.image, (64, 64))
    self.image2 = pygame.image.load('pygame_practice/picture/player_invin.png')
    self.image2 = pygame.transform.scale(self.image2, (64, 64))
    self.pos = [x//2, y//2]
    self.to = [0, 0]
    self.angle = 0

  def goto(self, x, y):
    self.to[0] += x
    self.to[1] += y

  def draw(self, screen, state):
    if self.to == [-1, -1]: self.angle = 45
    elif self.to == [-1, 0]: self.angle = 90
    elif self.to == [-1, 1]: self.angle = 135
    elif self.to == [0, 1]: self.angle = 180
    elif self.to == [1, 1]: self.angle = -135
    elif self.to == [1, 0]: self.angle = -90
    elif self.to == [1, -1]: self.angle = -45
    elif self.to == [0, -1]: self.angle = 0
    if state: # 무적상태 라면 비행기가 반짝거리는 그림으로 바뀐다
      k = self.image2
    else: # 무적상태가 아니라면 일반 비행기 그림이 나온다
      k = self.image
    rotated_image = pygame.transform.rotate(k, self.angle)
    calibpos = (self.pos[0] - rotated_image.get_width()/2, self.pos[1] - rotated_image.get_height()/2)
    screen.blit(rotated_image, calibpos)

  def calibpos(self): #플레이어의 현재위치를 알려주는 함수이다.
    calibpos = (self.pos[0] - self.image.get_width()/2, self.pos[1] - self.image.get_height()/2)
    return calibpos

  def update(self, dt, screen):
    width, height = screen.get_size()
    self.pos[0] = (self.pos[0] + dt * self.to[0]) % width
    self.pos[1] = (self.pos[1] + dt * self.to[1]) % height
    self.pos[1] = min((max(self.pos[1], 32)), height - 32)
    self.pos[0] = min((max(self.pos[0], 32)), width - 32)
