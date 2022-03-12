import futsal as ft
import pygame
from color import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
object_clicked = False
current_click = -1

ball, team_1, team_2 = ft.init()

ball.change_vec(10, 10)

running = True
fps = 60
clock = pygame.time.Clock()

def draw():
    global ball, team_1, team_2

    pygame.draw.circle(screen, WHITE, ball.pos(), 8)
    pygame.draw.circle(screen, BLACK, ball.pos(), 8, 2)

    for i in range(5):
        if i == 0:
            pygame.draw.circle(screen, TEAM_1_GK, team_1[i].pos(), 12)
            pygame.draw.circle(screen, TEAM_2_GK, team_2[i].pos(), 12)
        else:
            pygame.draw.circle(screen, TEAM_1, team_1[i].pos(), 12)
            pygame.draw.circle(screen, TEAM_2, team_2[i].pos(), 12)
        pygame.draw.circle(screen, BLACK, team_1[i].pos(), 12, 2)
        pygame.draw.circle(screen, BLACK, team_2[i].pos(), 12, 2)

def clicked_obj(x, y):
    global object_clicked, current_click, ball, team_1, team_2
    if object_clicked:
        if current_click == 0:
            ball.change_pos(x, y)
        elif current_click <= 5:
            team_1[current_click-1].change_pos(x, y)
        else:
            team_2[current_click-6].change_pos(x, y)

def move_obj():
    global ball, team_1, team_2
    ball.move()
    ball.slow_down()
    for plyer in team_1:
        plyer.move()
    for plyer in team_2:
        plyer.move()

while running:
    screen.fill(BACKGROUND)
    clock.tick(fps)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    clicked_obj(mouse_x, mouse_y)
    draw()
    move_obj() 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if object_clicked == False: 
                if ft.distance(ball.pos(), (mouse_x, mouse_y)) <= 8:
                    current_click = 0
                for i in range(len(team_1)):
                    if ft.distance(team_1[i].pos(), (mouse_x, mouse_y)) <= 12:
                        current_click = i + 1
                for j in range(len(team_2)):
                    if ft.distance(team_2[j].pos(), (mouse_x, mouse_y)) <= 12:
                        current_click = j + 6
                if current_click != -1:
                    object_clicked = True
            else:
                current_click = -1
                object_clicked = False

        if event.type == pygame.KEYDOWN:
            ball.change_vec((400-ball.pos()[0])/25, (300-ball.pos()[1])/25)

    pygame.display.flip()