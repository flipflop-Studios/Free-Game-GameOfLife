import pygame, time, random, math
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (50,50,255)
DARK_BLUE = (50,50,150)
BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHT_GREY = (240,240,240)
TRANS_GREY = (100,100,100,100)

pygame.init()

pygame.display.set_caption('Game of life - by Flipflop-Studios')

screen = pygame.display.set_mode((1600,800))

clock = pygame.time.Clock()

def createMatrix(x,y):
    matrix = []
    for i in range(x):
        row = []
        for e in range(y):
            if random.randint(1,2) == 1:
                row.append('W')
            else:
                row.append('B')
        matrix.append(row)
    return matrix
def drawMatrix(matrix):
    for i in range(len(matrix)):
        for e in range(len(matrix[i])):
            if matrix[i][e] == 'B':
                if e/2 == int(e/2) and i/2 == int(i/2) or e/2 != int(e/2) and i/2 != int(i/2):
                    pygame.draw.rect(screen, WHITE, (e * 20, i * 20, 20, 20))
                else:
                    pygame.draw.rect(screen, LIGHT_GREY, (e * 20, i * 20, 20, 20))
            if matrix[i][e] == 'W':
                    pygame.draw.rect(screen, BLACK, (e * 20, i * 20, 20, 20))
def evolMatrix(matrix):
    new_matrix = [['B' for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(1, len(matrix)-1):
        for e in range(1, len(matrix[i])-1):
            neighs = countNeighs(matrix, i, e)
            if matrix[i][e] == 'W' and 2 <= neighs <= 3:
                new_matrix[i][e] = 'W'
            elif matrix[i][e] == 'B' and neighs == 3:
                new_matrix[i][e] = 'W'
    return new_matrix
def countNeighs(matrix,i,e):
    neighs = 0
    if i == 0 or e == 0 or i == 39 or e == 79:
        print()
    else:
        if matrix[i-1][e-1] == 'W':
            neighs += 1
        if matrix[i-1][e] == 'W':
            neighs += 1
        if matrix[i-1][e+1] == 'W':
            neighs += 1
        if matrix[i][e-1] == 'W':
            neighs += 1
        if matrix[i][e+1] == 'W':
            neighs += 1
        if matrix[i+1][e-1] == 'W':
            neighs += 1
        if matrix[i+1][e] == 'W':
            neighs += 1
        if matrix[i+1][e+1] == 'W':
            neighs += 1
    return neighs
def setW(matrix,x,y):
    for i in range(len(matrix)):
        for e in range(len(matrix[i])):
            if i*20 <= y and (i+1)*20 >= y and e*20 <= x and (e+1)*20 >= x:
                if matrix[i][e] == 'B':
                    matrix[i][e] = 'W'
                else:
                    matrix[i][e] = 'B'
    return matrix
def drawMousePos(matrix,x,y):
    for i in range(len(matrix)):
        for e in range(len(matrix[i])):
            if i*20 <= y and (i+1)*20 >= y and e*20 <= x and (e+1)*20 >= x:
                transparent_rect = pygame.Surface((20, 20), pygame.SRCALPHA)
                transparent_rect.fill(TRANS_GREY)
                screen.blit(transparent_rect, (e*20, i*20, 20, 20))
def drawState(state):
    transparent_rect = pygame.Surface((20, 20), pygame.SRCALPHA)
    if state == 'creation':
        transparent_rect.fill((50, 50, 205, 128))
        screen.blit(transparent_rect, (1560, 20))
        screen.blit(transparent_rect, (1540, 20))
        screen.blit(transparent_rect, (1560, 100))
        screen.blit(transparent_rect, (1540, 100))
        screen.blit(transparent_rect, (1520, 40))
        screen.blit(transparent_rect, (1520, 60))
        screen.blit(transparent_rect, (1520, 80))
    elif state == 'evolution':
        transparent_rect.fill((50, 205, 50, 128))
        screen.blit(transparent_rect, (1520, 20))
        screen.blit(transparent_rect, (1520, 40))
        screen.blit(transparent_rect, (1520, 60))
        screen.blit(transparent_rect, (1520, 80))
        screen.blit(transparent_rect, (1520, 100))
        screen.blit(transparent_rect, (1540, 20))
        screen.blit(transparent_rect, (1540, 60))
        screen.blit(transparent_rect, (1540, 100))
        screen.blit(transparent_rect, (1560, 20))
        screen.blit(transparent_rect, (1560, 60))
        screen.blit(transparent_rect, (1560, 100))

matrix = []
for i in range(40):
    row = []
    for e in range(80):
            row.append('W')
    matrix.append(row)
matrix = evolMatrix(matrix)

state = 'creation'
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            matrix = setW(matrix,mouse_x,mouse_y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and state == 'evolution':
                state = 'creation'
            elif event.key == pygame.K_UP and state == 'creation':
                state = 'evolution'
            if event.key == pygame.K_1:
                matrix = []
                for i in range(40):
                    row = []
                    for e in range(80):
                        row.append('W')
                    matrix.append(row)
                matrix = evolMatrix(matrix)


    if state == 'evolution':
        matrix = evolMatrix(matrix)

    screen.fill(BLACK)

    drawMatrix(matrix)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    drawMousePos(matrix,mouse_x,mouse_y)

    drawState(state)

    pygame.display.update()

    clock.tick(20)

pygame.quit()
