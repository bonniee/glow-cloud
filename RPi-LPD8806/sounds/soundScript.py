import pygame, time

pygame.init()
pygame.mixer.init()
s1 = pygame.mixer.Sound("1.wav")
s1.play()
time.sleep(20)
