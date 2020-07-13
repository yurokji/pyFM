from team import Team
from team_stat import TeamStat
from league import League
from player import Player
import pygame
import numpy as np  

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (100,100,100)
YELLOW = (255, 255, 0)
BLUE = (0,0,255)
RED = (255,0,0)
size = [1200, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("football simulator")
clock  = pygame.time.Clock()
num_detail = 100
ground_rect = []
ground_img = pygame.Surface(size)

def drawGround(img):
    global ground_rect
    img.fill(GREEN)
    boundary = img.get_rect()
    sz = img.get_size()
    center = boundary.center
    aspect_ratio = int(sz[0]/sz[1])
    dx = 100
    dy = 100 // aspect_ratio
    ground_rect = [boundary[0] + dx, boundary[1] + dy, sz[0] - dx*2, sz[1] - dy*2 ]
    start_pt = [center[0], center[1] - (sz[1] - dy*2)//2]
    end_pt = [center[0], center[1] + (sz[1] - dy*2)//2]
    pygame.draw.rect(img, BLACK, ground_rect, 5)
    pygame.draw.line(img, BLACK, start_pt, end_pt, 5)
    pygame.draw.circle(img, BLACK, center, 100, 5)


def drawGrid(img, detail, visible):
    global ground_rect
    sx = ground_rect[0]
    sy = ground_rect[1]
    ex = ground_rect[0] + ground_rect[2]
    ey = ground_rect[1] + ground_rect[3]

    detail_x = detail * 2
    detail_y = detail

    dx = int((ex - sx) / detail_x)
    dy = int((ey - sy) / detail_y)

    for i in range(detail_x + 1):
        curr_x = sx + i * dx
        if visible:
            pygame.draw.line(img, GRAY, [curr_x,sy], [curr_x,ey], 1)
    for i in range(detail_y + 1):
        curr_y = sy + i * dy
        if visible:
            pygame.draw.line(img, GRAY, [sx,curr_y], [ex,curr_y], 1)


def drawBall(img, detail, pos_x, pos_y):
    global ground_rect
    sx = ground_rect[0]
    sy = ground_rect[1]
    ex = ground_rect[0] + ground_rect[2]
    ey = ground_rect[1] + ground_rect[3]

    detail_x = detail * 2
    detail_y = detail

    dx = int((ex - sx) / detail_x)
    dy = int((ey - sy) / detail_y)

    curr_x = sx + pos_x * dx
    curr_y = sy + pos_y * dy
    pygame.draw.circle(img, YELLOW, (curr_x, curr_y), 20)


def drawPlayer(img, detail, position, home):
    global ground_rect
    pos = list(position)
    if home == 0:
        pos[0] = 200 - position[0]

    sx = ground_rect[0]
    sy = ground_rect[1]
    ex = ground_rect[0] + ground_rect[2]
    ey = ground_rect[1] + ground_rect[3]

    detail_x = detail * 2
    detail_y = detail

    dx = int((ex - sx) / detail_x)
    dy = int((ey - sy) / detail_y)

    curr_x = sx + pos[0] * dx
    curr_y = sy + pos[1] * dy

    if home:
        pygame.draw.circle(img, BLUE, (curr_x, curr_y), 15)
    else:
        pygame.draw.circle(img, RED, (curr_x, curr_y), 15)


def drawPlayers(img, detail, positions, randomness, home):
    for i, position in enumerate(positions):
        if randomness:
            position[1][0] += np.random.randint(-1, 2)
            position[1][1] += np.random.randint(-1, 2)
        drawPlayer(img, detail, position[1], home)



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
match_homeTeam.setFormation(442)
match_awayTeam.setFormation(442)
homeTeamPlayers = homeTeam.getMatchObj().getFormationObj().getBestEleven()
awayTeamPlayers = homeTeam.getMatchObj().getFormationObj().getBestEleven()
homeTeamPosition =[player.getPosition() for player in homeTeamPlayers]
awayTeamPosition =[player.getPosition() for player in awayTeamPlayers]
print("homeTeamPosition: ", homeTeamPosition)
print("awayTeamPosition: ", awayTeamPosition)

drawGround(ground_img)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(10)
    drawGround(ground_img)
    drawGrid(ground_img, num_detail, visible=True)
    drawBall(ground_img, num_detail, 100, 50)
    drawPlayers(ground_img, num_detail, homeTeamPosition, randomness=True, home=True)
    drawPlayers(ground_img, num_detail, awayTeamPosition, randomness=True, home=False)

    screen.blit(ground_img, (0,0))
    pygame.display.flip()





# epl = League(teams)
# epl.begin()
# # print(epl.getSchedule())
# for i in range(epl.getTotalRound()):
# 	epl.nextRound()
# 	epl.showTable()


# # 가상의 선수 23명으로 팀을 만들어보았습니다.
# # 선수 한명에 관한 정보를 출력해봅시다
# teamName = teams[4].getTeamName()
# print(f'{teamName}')
# for i, player in enumerate(teams[4].getPlayers()):
#     print(i, player.getProfileObj().getProfile()["이름"], end='\t')
#     print(player.getProfileObj().getProfile()["포지션"], end='\t')
#     print(player.getAbilityObj().getTechnical()["드리블"], end='\t')
#     print(player.getAbilityObj().getMental()["시야"], end='\t')
#     print(player.getAbilityObj().getPhysical()["스피드"], end='\t')
#     print(player.getStatObj().getStat()["도움"], end='\t')
#     print(player.getFormObj().getForm()["부상"])