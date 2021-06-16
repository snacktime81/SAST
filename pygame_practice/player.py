import pygame

class Player:
  def __init__(self, x, y):
    self.image = pygame.image.load('pygame_practice/picture/player.png')
    self.image = pygame.transform.scale(self.image, (64, 64))
    self.pos = [x//2, y//2]
    self.to = [0, 0]
    self.angle = 0

  def goto(self, x, y):
    self.to[0] += x
    self.to[1] += y

  def draw(self, screen):
    if self.to == [-1, -1]: self.angle = 45
    elif self.to == [-1, 0]: self.angle = 90
    elif self.to == [-1, 1]: self.angle = 135
    elif self.to == [0, 1]: self.angle = 180
    elif self.to == [1, 1]: self.angle = -135
    elif self.to == [1, 0]: self.angle = -90
    elif self.to == [1, -1]: self.angle = -45
    elif self.to == [0, -1]: self.angle = 0

    rotated_image = pygame.transform.rotate(self.image, self.angle)

    calibpos = (self.pos[0] - rotated_image.get_width()/2, self.pos[1] - rotated_image.get_height()/2)
    screen.blit(rotated_image, calibpos)

  def update(self, dt, screen):
    width, height = screen.get_size()
    self.pos[0] = (self.pos[0] + dt * self.to[0]) % width
    self.pos[1] = (self.pos[1] + dt * self.to[1]) % height
  
    self.pos[0] = min((max(self.pos[0], 32)), width - 32)
    self.pos[1] = min(max(self.pos[1], 32), height - 32)

#    if self.pos[0] < 32:
#      self.pos[0] = 32
#    if self.pos[1] < 32:
#      self.pos[1] = 32
#    if self.pos[0] > width - 32:
#      self.pos[0] = width - 32
#    if self.pos[1] > height - 32:
#      self.pos[1] = height - 32  