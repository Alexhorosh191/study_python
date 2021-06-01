import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
bg_color = (192, 192, 192)
screen.fill(bg_color)


def draw_smiley_face():
    def draw_face():
        circle(screen, (255, 255, 0), (400, 400), 300)
        circle(screen, (0, 0, 0), (400, 400), 300, 1)

    def draw_eyes():
        circle(screen, (255, 0, 0), (250, 350), 70)
        circle(screen, (255, 0, 0), (550, 350), 50)
        circle(screen, (0, 0, 0), (250, 350), 35)
        circle(screen, (0, 0, 0), (550, 350), 25)
        circle(screen, (0, 0, 0), (250, 350), 70, 1)
        circle(screen, (0, 0, 0), (550, 350), 50, 1)

    def draw_eyebrows():
        line(screen, (0, 0, 0), (100, 200), (350, 310), 20)
        line(screen, (0, 0, 0), (670, 230), (470, 330), 20)

    def draw_smile():
        rect(screen, (0, 0, 0), (275, 550, 250, 50))

    draw_face()
    draw_eyes()
    draw_eyebrows()
    draw_smile()


draw_smiley_face()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
