import pgzrun
import pygame 
import random
import os

window = pygame.display.set_mode((1000,700))
WIDTH = 1000
HEIGHT = 700

direction = True

char = Actor('song')
flip_char = Actor('song flip')
char.x = 300
char.y = 300

shell = Actor('shell')
shell.x = random.randint(50, 950)
shell.y = random.randint(50, 650)

start_bg = Actor('start bg')
game_bg = Actor('song bg')
score = 0
timer = 30
game_state = 'game'

def update():
    global score
    global timer

    if timer <= 0:
        return
    timer -= 1 / 60

# controls the character
    if keyboard.up:
        char.draw() 
        char.y -= 8
    if keyboard.down:
        char.draw() 
        char.y += 8
    if keyboard.left:
        flip_char.draw()
        char.x -= 8
    if keyboard.right:
        char.draw() 
        char.x += 8

    # when character touches the object the score increases 
    if char.colliderect(shell):
        shell.x = random.randint(50, 950)
        shell.y = random.randint(50, 650)
        score += 1

    return score

score_now = int(str(score))
        
        

# gets the high score of the game
def get_high_score():
    f = open('score.txt', 'r') #opens file in read mode
    file = f.readlines()
    high_score = int(file[0])
    f.close()

    return high_score


# saves high score
def updateFile():
    f = open('score.txt', 'r') #opens file in read mode
    file = f.readlines()
    last = int(file[0])
    
    if last < int(score): #sees if current score is higher than the last
        f.close()
        file = open('score.txt', 'w') #opens th efile and rewrites the new score
        file.write(str(score))
        file.close()

        return score
    return last

high_score = int(get_high_score())

def draw():
    
    if timer <= 0:
        screen.clear()
        screen.draw.text('Game Over', (420,270), color=(255,255,255), fontname="vc.ttf", fontsize=40)

        last_high_score = high_score
        current_score = score_now
        
        if current_score > last_high_score:
            screen.draw.text("Congratulations! New High Score:" + str(score), (250,400), fontname="vc.ttf", color=(255,255,255), fontsize=40)
        else:
            screen.draw.text('Score: ' + str(score), (420,330), color=(255,255,255), fontname="vc.ttf", fontsize=40)

    else:
        game_bg.draw()
        shell.draw()
        char.draw() 
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontname="vc.ttf", fontsize=20)
        screen.draw.text('Time: ' + str(round(timer)), (330,10), color=(255,255,255), fontname="vc.ttf", fontsize=20)
    
        
        
pgzrun.go() 
