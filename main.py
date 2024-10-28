import pygame
from time import sleep
pygame.init()

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load("assets/ratsasan.mp3")
pygame.mixer.music.play()
sleep(2)

pygame.mixer.init()
pygame.mixer.music.load("assets/scary.mp3")
pygame.mixer.music.play()
sleep(1)

image = pygame.image.load("assets/scr.jpg")
window.blit(image, (0, 0))

pygame.display.update()
sleep(1)