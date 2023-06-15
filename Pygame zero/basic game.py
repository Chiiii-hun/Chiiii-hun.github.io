import pgzrun
import random

WIDTH = 800
HEIGHT = 600


player = Actor('song')
player.x = 300
player.y = 300

coin = Actor('coin')
coin.x = random.randint(0, 750)
coin.y = random.randint(0, 550)

score = 0
timer = 10

def update():
    global score
    global timer

    if timer <= 0:
        return

    timer -= 1 / 60

    if keyboard.up:
        player.y -= 8
    if keyboard.down:
        player.y += 8
    if keyboard.left:
        player.x -= 8
    if keyboard.right:
        player.x += 8

    if player.colliderect(coin):
        coin.x = random.randint(0, 750)
        coin.y = random.randint(0, 550)
        score += 1

def draw():
    if timer <= 0:
        screen.clear()
        screen.draw.text('Game Over', (350,270), color=(255,255,255), fontsize=30)
        screen.draw.text('Score: ' + str(score), (350,330), color=(255,255,255), fontsize=30)
    else:
        screen.fill(("red"))
        player.draw()
        coin.draw()
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
        screen.draw.text('Time: ' + str(round(timer, 2)), (330,10), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line
