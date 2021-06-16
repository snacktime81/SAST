import pygame

class Bullet:
  def __init__(self, x, y, to_x, to_y):
    self.pos = [x, y]
    self.to = [to_x, to_y]
    self.radius = 7
    self.color = (190, 0, 0)
  
  def update_and_draw(self, dt, screen):
    width, height = screen.get_size()
    self.pos[0] = (self.pos[0] + dt * self.to[0]) % width
    self.pos[1] = (self.pos[1] + dt * self.to[1]) % height
    pygame.draw.circle(screen, self.color, self.pos, self.radius)

  def update_and_draw_blue(self, dt, screen): # 파란색 총알을 그리는 함수
    width, height = screen.get_size()
    self.pos[0] = (self.pos[0] + dt * self.to[0]) % width
    self.pos[1] = (self.pos[1] + dt * self.to[1]) % height
    pygame.draw.circle(screen, (0, 0, 190), self.pos, 10) # 색은 파란색, 반지름은 10이다

  def update_and_draw_white(self, dt, screen): # 흰색 총알을 그리는 함수
    width, height = screen.get_size()
    self.pos[0] = (self.pos[0] + dt * self.to[0]) % width
    self.pos[1] = (self.pos[1] + dt * self.to[1]) % height
    pygame.draw.circle(screen, (255, 255, 255), self.pos, 5) # 색은 흰색, 반지름은 5이다