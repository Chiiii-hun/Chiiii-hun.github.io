import pygame
pygame.init()

screen = pygame.display.set_mode((1000,700))
start_img = pygame.image.load('start.png')
font = pygame.font.Font('vc.ttf')

 
x = 350; # x coordnate of image
y = 450; # y coordinate of image
screen.fill('White')
screen.blit(start_img ,  ( x,y)) # paint to screen
pygame.display.flip() # paint screen one time
 
running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            if start_img.get_rect().collidepoint(x, y):
                print('clicked on image')
#loop over, quite pygame
pygame.quit()
