import pygame
import numpy as np

GREEN = (0, 255, 0)
WHITE = (200,200,200)
BLACK = (0,0,0)
GRAY = (100,100,100)
RED = (255,0,0)
BLUE = (0,0,255)
ground = []

def drawGround(img):
    img.fill(GREEN)
    boundary = img.get_rect()
    sz = img.get_size()
    center = boundary.center
    aspect_ratio = int(sz[0] / sz[1])
    dx = 100
    dy = 100 // aspect_ratio
    boundray_rect = [boundary[0] + dx, boundary[0] + dy, sz[0] - dx*2, sz[1] - dy*2]
    start_line = [center[0], center[1] - (sz[1] - dy*2) // 2]
    end_line =   [center[0], center[1] + (sz[1] - dy*2) // 2]
    pygame.draw.rect(img, BLACK, boundray_rect, 5)
    pygame.draw.line(img, BLACK, start_line, end_line, 5)
    return boundray_rect

def drawGrid(img, grect, detail, visible=True):
    sx = grect[0]
    sy = grect[1]
    ex = grect[0] + grect[2] 
    ey = grect[1] + grect[3]

    detail_x = detail*2
    detail_y = detail
    dx = int((ex - sx)/ detail_x)
    dy = int((ey - sy)/ detail_y)

    for i in range(detail_x + 1):
        curr_x = sx + i * dx
        if visible:
            pygame.draw.line(img, GRAY, [curr_x, sy], [curr_x, ey], 1)
    for i in range(detail_y + 1):
        curr_y = sy + i * dy
        if visible:
            pygame.draw.line(img, GRAY, [sx, curr_y], [ex, curr_y], 1)

    return [detail_x, detail_y]
                                                                                                                                                                                                                                                                                                                                                                                                                                                      
def drawBall(img, grect, detail, pos_x, pos_y):
    sx = grect[0]
    sy = grect[1]
    ex = grect[0] + grect[2] 
    ey = grect[1] + grect[3]

    dx = int((ex - sx)/ detail[0])
    dy = int((ey - sy)/ detail[1])

    curr_x = sx + pos_x * dx
    curr_y = sy + pos_y * dy
    pygame.draw.circle(img, RED, (curr_x, curr_y), 2)

def drawPlayer(img, grect, detail, pos_x, pos_y):
    sx = grect[0]
    sy = grect[1]
    ex = grect[0] + grect[2] 
    ey = grect[1] + grect[3]

    dx = int((ex - sx)/ detail[0])
    dy = int((ey - sy)/ detail[1])

    curr_x = sx + pos_x * dx
    curr_y = sy + pos_y * dy
    pygame.draw.circle(img, BLUE, (curr_x, curr_y), 2)



size = [1200, 600]
num_detail = 100
screen = pygame.display.set_mode(size)
pygame.display.set_caption("football simulator")
run = True
clock = pygame.time.Clock()
ground_img = pygame.Surface(size)



# pos_x = np.random.randint(0, detail[0] + 1)
# pos_y = np.random.randint(0, detail[1] + 1)
pos_x = num_detail
pos_y = num_detail //2

PX = [pos_x, pos_x, pos_x, pos_x, pos_x, pos_x, pos_x, pos_x, pos_x, pos_x, pos_x, pos_x, pos_x, pos_x, pos_x,pos_x,pos_x,pos_x,pos_x,pos_x]
PY = [pos_y, pos_y, pos_y, pos_y, pos_y, pos_y, pos_y, pos_y, pos_y, pos_y, pos_y, pos_y, pos_y, pos_y, pos_y,pos_y,pos_y,pos_y,pos_y,pos_y]

while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    brect= drawGround(ground_img)
    detail = drawGrid(ground_img, brect,pos_x, visible = True)
    screen.blit(ground_img, (0,0))

    ball_img = pygame.Surface(size, pygame.SRCALPHA)
    pos_x += np.random.randint(-1, 2)
    pos_y += np.random.randint(-1, 2)
    drawBall(ball_img, brect, detail, pos_x, pos_y)
    for i in range(20):
        PX[i] += np.random.randint(-1, 2)
        PY[i] += np.random.randint(-1, 2)
        drawPlayer(ball_img, brect, detail, PX[i], PY[i])
    screen.blit(ball_img, (0,0))
    pygame.display.flip()



