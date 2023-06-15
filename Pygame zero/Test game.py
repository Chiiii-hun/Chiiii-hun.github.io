import pgzrun
import pygame
import random


#screen
WIDTH = 600
LENGTH = 600

score = 0
game_over = False
run = True
direction = True

char = Actor('squirrel')
char._surf = pygame.transform.scale(char._surf, (150, 200))
char._update_pos
char.x = 50
char.y = 50

coin = Actor("coin")
coin.pos = 200,200

def draw():
    screen.fill(("red"))
    coin.draw()
    char.draw()

    screen.draw.text('Score: ' + str(score), (15,10), color=("black"), topleft = (10,10), fontsize=30)

    if game_over:
        screen.draw.text('Game Over', (360, 300), color=(255,255,255), fontsize=60)
        screen.draw.text('Final Score:' + str(score), topleft = (10,10), color=('black'), fontsize=60)

def place_coin():
    coin_x = random.randint(20, (WIDTH - 20))
    coin_y = random.randint(20, (LENGTH - 20))

def time_up():
    global game_over
    game_over = True

pygame.init()



def update():
    global score


while run:


    # Display the player sprite at x
    # and y coordinates
    # Flipping the player sprite if player
    # changes the direction
    if direction == True:
        char.draw(char.x, char.y)
    if direction == False:
        char.draw(pygame.transform.flip(char, True, False), (char.x, char.y))
  
  
    # Display the player sprite at x and y coordinates
    (char, (char.x, char.y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = True
            elif event.key == pygame.K_LEFT:
                direction = False
            
    # Storing the key pressed in a
    # new variable using key.get_pressed()
    # method
    key_pressed_is = pygame.key.get_pressed()
  
    # Decreasing the x coordinate if the Left arrow key is pressed
    if key_pressed_is[pygame.K_LEFT]:
                char.x -= 8
  
    # Increasing the x coordinate if the button pressed is Right arrow key
    if key_pressed_is[pygame.K_RIGHT]:
                char.x += 8
  
    # Decreasing the y coordinate if the button pressed is Up arrow key
    if key_pressed_is[pygame.K_UP]:
                char.y -= 8
  
    # Increasing the y coordinate if the button pressed is Down arrow key
    if key_pressed_is[pygame.K_DOWN]:
                char.y += 8
                
    

    coin_collected = char.colliderect(coin)

    if coin_collected:
        score = score + 1
        place_coin()

place_coin

pygame.display.update()
pgzrun.go()

