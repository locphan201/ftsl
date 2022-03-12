from .bll import Ball
from .player import Player

def init():
    ball = Ball(15, 15)
    team_1 = []
    team_2 = []
    for i in range(5):
        team_1.append(Player(15+i*30, 40))
        team_2.append(Player(15+i*30, 70))
    return ball, team_1, team_2

def distance(pt1, pt2):
    return ((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)**0.5