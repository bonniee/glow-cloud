
# def getNumberSound(i)
import pygame
from datetime import datetime

pygame.init()
pygame.mixer.init()


def playNumber(num):
  if (num < 0):
    return
  if (num < 20):
    s = getNumberSound(num)
    s.play()
    return
  else:
    little = getNumberSound(num % 10)
    big = getNumberSound(num / 10)
    big.play()
    little.play()
    
def playTimeSound():
  dt = datetime.now()
  hour = dt.hour
  minute = dt.minute
  itis = pygame.mixer.Sound("sounds/itis.wav")
  itis.play()
  getNumberSound(hour).play()
  if (minute == 0):
    oclock = pygame.mixer.sound("sounds/oclock.wav")
    oclock.play()
  else:
    playNumber(minute)


  
