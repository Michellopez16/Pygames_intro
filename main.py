import pygame
from sys import exit

pygame.init() # correr antes de cualquier codigo de pygame

width,height = 800,400
screen = pygame.display.set_mode((width,height)) # se ve solo un frame 
pygame.display.set_caption("Runner")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #quit() #https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used
            #exit() # need import sys
            raise SystemExit
        
    # draw all our elements
    #update everything 
    pygame.display.update()

