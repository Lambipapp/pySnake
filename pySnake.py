import pygame
import time

import snake
import gameboard

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


mapSize = 25, 25
ppc = 25    #pixels per cell
wSize = (mapSize[0] * ppc, mapSize[1] * ppc)
pygame.init()
window = pygame.display.set_mode(wSize)
pygame.display.set_caption("snake")

def drawSquare(pos, size, color):
     pygame.draw.rect(window, color, (pos[0] * size, pos[1] * size, size, size))

gb = gameboard.gameboard(mapSize[0], mapSize[1])
snake = snake.snake(gb, mapSize)


dt = 0
prevT = time.time()
timer = 0
timeStep = 0.25

active = True
while active:
    currT = time.time()
    dt = currT - prevT
    prevT = currT
    timer += dt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    
    dirKey = pygame.key.get_pressed()

    if dirKey[pygame.K_RIGHT]:
        snake.setDirection((1, 0))

    if dirKey[pygame.K_LEFT]:
        snake.setDirection((-1, 0))

    if dirKey[pygame.K_UP]:
        snake.setDirection((0, -1))

    if dirKey[pygame.K_DOWN]:
        snake.setDirection((0, 1))


    if timer >= timeStep:
        timer = 0
        
        if snake.move(gb) == -1:
            active = False

    # Draw game:
    window.fill(black)
    for x in range(mapSize[0]):
        for y in range(mapSize[1]):
            cv = gb.getCellVal(x, y)
            if cv == 1:
                drawSquare((x,y),ppc, white)
            elif cv == 2:
                drawSquare((x,y),ppc, red)
    pygame.display.update()
    
    

pygame.quit()

