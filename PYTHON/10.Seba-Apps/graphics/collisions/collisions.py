from graphics import GraphWin, Point, Rectangle
import sys, os
import time
import random
import winsound

win = GraphWin("Things of stuff", 1200, 800)

# Used for more accurate calculations
# timesteps = 10
fps = 0.00053

def drawRect(ent):
  ent = Rectangle(Point(ent.x, ent.y), Point(ent.w, ent.h))
  ent.draw(win)

def colx(c1, c2):
  sumM = c1.m + c2.m
  newV = (c1.m-c2.m)/sumM * c1.vx + 2 * c2.m / sumM * c2.vx
  return newV
def coly(c1, c2):
  sumM = c1.m + c2.m
  newV = (c1.m-c2.m)/sumM * c1.vy + 2 * c2.m / sumM * c2.vy
  return newV

def playaudio():
  winsound.PlaySound("D:/Workshop-HDD/Studio/Python/graphics/stuf/sound.wav", winsound.SND_ASYNC)
  # pass

class cube:
  def __init__(self, x = 0, y = 0, w = 0, h = 0, vx = 0, vy = 0, m = 0):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.vx = vx
    self.vy = vy
    self.m = m
    self.fr = 0.99
    self.rec = Rectangle(Point(self.x, self.y), Point(self.x+self.w, self.y+self.h))
    self.rec.setFill("red")
    self.rec.draw(win)

  def hitwall(self):
    if self.x + self.w > win.width:
      self.vx = -self.vx
      playaudio()
    elif self.x < 0:
      self.vx = -self.vx
      playaudio()
    if self.y + self.h > win.height:
      self.vy = -self.vy
      playaudio()
    elif self.y < 0:
      self.vy = -self.vy
      playaudio()
  
  def update(self):
    self.rec.move(self.vx, self.vy)
    self.x += self.vx
    # self.vx *= 1.01
    self.y += self.vy
    # self.vy *= 1.01
    time.sleep(fps)

  def bounce(self):
    self.vx = -self.vx
    self.vy = -self.vy

  def friction(self):
    self.vx *= self.fr
    self.vy *= self.fr
  
  def gravity(self):
    self.vy += 0.08

  def killonspeed(self, max):
    if self.vx > max or self.vy > max:
      self.x = 10
      self.vx = 0
      self.y = 10
      self.vy = 0
      # winsound.PlaySound("D:/Workshop-HDD/Studio/Python/graphics/stuf/kill.wav", winsound.SND_ASYNC)


c1 = cube(300, 200, 100, 100, -3, random.randrange(8), 1)
c2 = cube(300, 400, 150, 150, random.randrange(10), random.randrange(5), 2)

clicked = 0

while(clicked == 0):

  # c1.friction()
  c1.hitwall()
  c1.update()
  c1.killonspeed(800)

  # c2.friction()
  c2.update()
  c2.hitwall()
  c2.killonspeed(200)

  # c1.gravity()
  # c2.gravity()

  if c2.x < c1.x + c1.w and c2.x + c2.w > c1.x and c2.y < c1.y + c1.h and c2.y + c2.h > c1.y:

    if c2.x < c1.x + c1.w and c2.x + c2.w > c1.x:
      vx1 = colx(c1, c2)
      vx2 = colx(c2, c1)
      c1.vx = vx1
      c2.vx = vx2

    if c2.y < c1.y + c1.h and c2.y + c2.h > c1.y:
      vy1 = coly(c1, c2)
      vy2 = coly(c2, c1)
      c1.vy = vy1
      c2.vy = vy2
    
    playaudio()
    
  if win.checkMouse(): clicked = 1
  # Helps killing process
  
win.close()