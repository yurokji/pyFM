from team import Team
from team_stat import TeamStat
from league import League
from player import Player
from match import Match
import numpy as np 
import pygame




GREEN = (0, 255, 0)
WHITE = (200,200,200)
BLACK = (0,0,0)
GRAY = (100,100,100)
RED = (255,0,0)
BLUE = (0,0,255)
ground_rect = []

def drawGround(img):
    global ground_rect
    img.fill(GREEN)
    boundary = img.get_rect()
    sz = img.get_size()
    center = boundary.center
    aspect_ratio = int(sz[0] / sz[1])
    dx = 100
    dy = 100 // aspect_ratio
    ground_rect = [boundary[0] + dx, boundary[0] + dy, sz[0] - dx*2, sz[1] - dy*2]
    start_line = [center[0], center[1] - (sz[1] - dy*2) // 2]
    end_line =   [center[0], center[1] + (sz[1] - dy*2) // 2]
    pygame.draw.rect(img, BLACK, ground_rect, 5)
    pygame.draw.line(img, BLACK, start_line, end_line, 5)


def drawGrid(img, detail, visible=True):
    global ground_rect
    sx = ground_rect[0]
    sy = ground_rect[1]
    ex = ground_rect[0] + ground_rect[2] 
    ey = ground_rect[1] + ground_rect[3]

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
                                                                                                                                                                                                                                                                                                                                                                                                                                                      
def drawBall(img, detail, pos_x, pos_y):
    global ground_rect
    sx = ground_rect[0]
    sy = ground_rect[1]
    ex = ground_rect[0] + ground_rect[2] 
    ey = ground_rect[1] + ground_rect[3]

    dx = int((ex - sx)/ detail[0])
    dy = int((ey - sy)/ detail[1])

    curr_x = sx + pos_x * dx
    curr_y = sy + pos_y * dy
    pygame.draw.circle(img, RED, (curr_x, curr_y), 2)

def drawPlayers(img, detail, positions, randomness, home=True):
    for i, position in enumerate(positions):
        if randomness:
            position[1][0] += np.random.randint(-1, 2)
            position[1][1] += np.random.randint(-1, 2)
        drawPlayer(img, detail, position[1], home)

def drawPlayer(img, detail, position, home):
    global ground_rect
    pos = list(position)
    if home == 0:
        pos[0] = 200 - position[0]


    sx = ground_rect[0]
    sy = ground_rect[1]
    ex = ground_rect[0] + ground_rect[2] 
    ey = ground_rect[1] + ground_rect[3]
    dx = int((ex - sx)/ detail[0])
    dy = int((ey - sy)/ detail[1])
    curr_x = sx + pos[0] * dx
    curr_y = sy + pos[1] * dy
    if home:
        pygame.draw.circle(img, BLUE, (curr_x, curr_y), 3)
    else:
        pygame.draw.circle(img, RED, (curr_x, curr_y), 3)



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




team_names = ["리버풀", "맨시티", "레스터시티", "첼시", "맨유", "울버햄튼", "쉐필드", "아스날", "토트넘", "번리", "에버튼", "크리스탈팰리스", "뉴캐슬", "사우스햄튼", "브라이튼", "웨스트햄", "왓포드", "아스톤빌라", "본머스", "노르위치시티"]

numTeams = len(team_names)
teams = []
list_profile = ["호날두", "FW", "포르투갈", 186, 75, 35]

for i in range(numTeams):
    team = Team(team_names[i])
    for j in range(Team.numPlayers):
        p = Player(list_profile)
        team.addPlayer(p)
    teams.append(team)



homeTeam = teams[2]
awayTeam = teams[4]
match_homeTeam = homeTeam.prepMatch()
match_awayTeam = awayTeam.prepMatch()
homeTeam.getMatchObj().setFormation(442)
awayTeam.getMatchObj().setFormation(442)
homeTeamPlayers = homeTeam.getMatchObj().getFormationObj().getBestEleven()
awayTeamPlayers = homeTeam.getMatchObj().getFormationObj().getBestEleven()
positions = [player.getPosition() for player in homeTeamPlayers]
brect= drawGround(ground_img)


while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    drawGround(ground_img)
    detail = drawGrid(ground_img, num_detail, visible = True)
    screen.blit(ground_img, (0,0))

    ball_img = pygame.Surface(size, pygame.SRCALPHA)
    pos_x += np.random.randint(-1, 2)
    pos_y += np.random.randint(-1, 2)
    # drawBall(ball_img, brect, detail, pos_x, pos_y)
    # drawPlayers(ball_img, detail, positions, 1)
    # screen.blit(ball_img, (0,0))
    drawPlayers(ball_img, detail, positions, 0)
    screen.blit(ball_img, (0,0))
    pygame.display.flip()

# 
# # # print(epl.getSchedule())
# # for i in range(epl.getTotalRound()):
# # 	epl.nextRound()
# # 	epl.showTable()


# # # 가상의 선수 23명으로 팀을 만들어보았습니다.
# # # 선수 한명에 관한 정보를 출력해봅시다
# # teamName = teams[4].getTeamName()
# # print(f'{teamName}')
# # for i, player in enumerate(teams[4].getPlayers()):
# #     print(i, player.getProfileObj().getProfile()["이름"], end='\t')
# #     print(player.getProfileObj().getProfile()["포지션"], end='\t')
# #     print(player.getAbilityObj().getTechnical()["드리블"], end='\t')
# #     print(player.getAbilityObj().getMental()["시야"], end='\t')
# #     print(player.getAbilityObj().getPhysical()["스피드"], end='\t')
# #     print(player.getStatObj().getStat()["도움"], end='\t')
# #     print(player.getFormObj().getForm()["부상"])