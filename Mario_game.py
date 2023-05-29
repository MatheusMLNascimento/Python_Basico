import pygame
import os
from pygame.locals import *
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("Aventura contra o TINHOSO!")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

HP_FONT = pygame.font.SysFont('comicsans', 40)
SOM_FUNDO = pygame.mixer.Sound(os.path.join('Assets', 'space+chillout.mp3'))

Largura, Altura = 800, 600
WIN = pygame.display.set_mode((Largura, Altura))

mario_hp = 50
MARIO_WIDTH, MARIO_HEIGHT = 55, 40
VEL = 5

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (Altura, Largura))
PERSO_IMAGEM = pygame.image.load(
    os.path.join('Assets', 'PAur.png'))
MARIO_PERSO = pygame.transform.scale(
    PERSO_IMAGEM, (MARIO_WIDTH, MARIO_HEIGHT))

def tela_ini(mario):
    WIN.blit(MARIO_PERSO, (mario.x, mario.y))
    mario_hp_text = HP_FONT.render("HP: " + str(mario_hp), 1, PRETO)
    WIN.blit(mario_hp_text, (Largura - mario_hp_text.get_width() - 10, 10))
    pygame.display.update()


def mario_movimento(keys_pressed, mario):
    if keys_pressed[pygame.K_a] and mario.x - VEL > 0:  # Direita
        mario.x -= VEL
    if keys_pressed[pygame.K_d] and mario.x + mario.width:  # Esquerda
        mario.x += VEL
    if keys_pressed[pygame.K_s] and mario.y + mario.height < Altura - 15:  # Baixo
        mario.y += VEL
    if keys_pressed[pygame.K_w] and mario.y + VEL > 0:  # Cima
        mario.y -= VEL


FPS = 60


def main():
    WIN.blit(SPACE, (0, 0))
    mario = pygame.Rect(Largura//2, Altura//2, MARIO_WIDTH, MARIO_HEIGHT)
    SOM_FUNDO.play()

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        mario_movimento(keys_pressed, mario)
        tela_ini(mario)
    pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()