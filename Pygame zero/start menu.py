import pgzrun

WIDTH = 1000
HEIGHT = 700

start_bg = Actor('start bg')
start_img = Actor('start.png')
start_clicked = False


def draw():
    start_bg.draw()
    start_img.draw()
    if keyboard.space:
        screen.fill('BLACK')
         
pgzrun.go() 

#import pygame
#pygame.init()

#screen = pygame.display.set_mode((1000,700))
#start_img = pygame.image.load('start.png')
#font = pygame.font.Font('vc.ttf')

 
#
#l#oop over, quite pygame
#pygame.quit()
#
