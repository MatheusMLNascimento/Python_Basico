import os
import sys

dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

####
import pygame
import random
from pygame.locals import *
pygame.init()

pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("Aventura contra o TINHOSO!")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)

HP_FONT = pygame.font.SysFont('comicsans', 40)
VENCEDOR_FONT = pygame.font.SysFont('comicsans', 60)

SOM_FUNDO = pygame.mixer.Sound(
    os.path.join('Assets', 'space+chillout.mp3'))
SOM_ATIRANDO = pygame.mixer.Sound(
    os.path.join('Assets', 'Gun+Silencer.mp3'))

mario_hit_x = random.randint(100, 700)
mario_hit_y = random.randint(100, 500)
# hit_box_mario = pygame.Rect(415, 315, 8, 12)
hit_box_inimigo = pygame.Rect(mario_hit_x, mario_hit_y, 8, 12)

Barreira_left = pygame.Rect(0, 0, 75, 600)
Barreira_right = pygame.Rect(735, 0, 75, 600)
Barreira_top = pygame.Rect(0, 0, 800, 55)
Barreira_down = pygame.Rect(0, 540, 800, 75)


Largura, Altura = 800, 600
WIN = pygame.display.set_mode((Largura, Altura))

MARIO_WIDTH, MARIO_HEIGHT = 48, 50
VEL = 5
BULLET_VEL = 8
MAX_BULLET = 5

MARIO_HIT = pygame.USEREVENT + 1
ENE_HIT = pygame.USEREVENT + 2


SPACE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'Background_FirstFloor.png')), (Largura, Altura))

PERSO_IMAGEM = pygame.image.load(
    os.path.join('Assets', 'perso_princi.png'))
MARIO_PERSO = pygame.transform.scale(
    PERSO_IMAGEM, (MARIO_WIDTH, MARIO_HEIGHT))

Aim_img = pygame.image.load(
    os.path.join('Assets', 'Aim_image.png'))
Aim_icon = pygame.transform.scale(Aim_img, (20, 20))

Gun_img = pygame.image.load(
    os.path.join('Assets', 'Normal_gun2.png'))
Gun_icon = pygame.transform.scale(Gun_img, (48, 50))
# Gun_image = pygame.transform.flip(Gun_icon, True, False)



def balas_disparadas(mario_balas, inimigo_hp):
    for bala in mario_balas:
        bala.x += BULLET_VEL
        if bala.x > Largura:
            mario_balas.remove(bala)
        if bala.colliderect(hit_box_inimigo):
            pygame.event.post(pygame.event.Event(ENE_HIT))
            if inimigo_hp <= 0:
                inimigo_hp = 30
                hit_box_inimigo.x, hit_box_inimigo.y = random.randint(100, 700), random.randint(100, 500)



def hit_box(mario, gun):
    if mario.colliderect(hit_box_inimigo):
        pygame.event.post(pygame.event.Event(MARIO_HIT))
        mario.x += 5
        gun.x += 5


def draw_winner(text):
    draw_text = VENCEDOR_FONT.render(text, 1, BRANCO)
    WIN.blit(draw_text, (Largura//2 - draw_text.get_width()/2,
                         Altura/2 - draw_text.get_height()/2))

    pygame.display.update()
    pygame.time.delay(5000)


def tela_ini(mario_hp, inimigo_hp, mario_balas, mario, aim, gun):
    pygame.draw.rect(WIN, BRANCO, Barreira_left)
    WIN.blit(SPACE, (0, 0))
    #  pygame.draw.rect(WIN, VERMELHO, hit_box_mario)
    pygame.draw.rect(WIN, AMARELO, hit_box_inimigo)

    inimigo_hp_text = HP_FONT.render(
        "Inimigo HP: " + str(inimigo_hp), 1, BRANCO)
    mario_hp_text = HP_FONT.render(
        "HP: " + str(mario_hp), 1, BRANCO)

    WIN.blit(mario_hp_text, (
        Largura - mario_hp_text.get_width() - 10, 10))
    WIN.blit(inimigo_hp_text, (10, 10))

    for bala in mario_balas:
        pygame.draw.rect(WIN, AMARELO, bala)

    WIN.blit(MARIO_PERSO, (mario.x, mario.y))
    WIN.blit(Aim_icon, (aim.x, aim.y))
    WIN.blit(Gun_icon, (gun.x, gun.y))

    pygame.display.update()

def barreira(mario, gun):
    if mario.colliderect(Barreira_left):
        mario.x += 5
    if mario.colliderect(Barreira_right):
        mario.x -= 5
    if mario.colliderect(Barreira_top):
        mario.y += 5
    if mario.colliderect(Barreira_down):
        mario.y -= 5

    if gun.colliderect(Barreira_left):
        gun.x += 5
    if gun.colliderect(Barreira_right):
        gun.x -= 5
    if gun.colliderect(Barreira_top):
        gun.y += 5
    if gun.colliderect(Barreira_down):
        gun.y -= 5


def mario_movimento(keys_pressed, mario, gun):
    if keys_pressed[pygame.K_a] and mario.x - VEL > 0:  # Esquerda
        mario.x -= VEL
        gun.x -= VEL
        # hit_box_mario.x -= VEL
    if keys_pressed[pygame.K_d] and mario.x + mario.width:  # Direita
        mario.x += VEL
        gun.x += VEL
        # hit_box_mario.x += VEL
    if keys_pressed[pygame.K_s] and mario.y + mario.height < Altura - 15:  # Baixo
        mario.y += VEL
        gun.y += VEL
        # hit_box_mario.y += VEL
    if keys_pressed[pygame.K_w] and mario.y + VEL > 0:  # Cima
        mario.y -= VEL
        gun.y -= VEL
        # hit_box_mario.y -= VEL


FPS = 60

aim_xy = pygame.mouse.get_pos()
print(aim_xy)


def main():
    aim = pygame.Rect(aim_xy[0], aim_xy[1], 10, 10)
    mario = pygame.Rect(400, 300, MARIO_WIDTH, MARIO_HEIGHT)
    gun = pygame.Rect(400, 300, MARIO_WIDTH, MARIO_HEIGHT)

    SOM_FUNDO.play()

    mario_balas = []

    mario_hp = 50
    inimigo_hp = 30


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_LCTRL and len(mario_balas) < MAX_BULLET:
                    bala = pygame.Rect(
                        gun.x + gun.width, gun.y + gun.height//2 - 2, 10, 5)
                    mario_balas.append(bala)
                    SOM_ATIRANDO.play()

            if event.type == MARIO_HIT:
                mario_hp -= 1
            if event.type == ENE_HIT:
                inimigo_hp -= 1

        winner_text = ""
        if mario_hp <= 0:
            winner_text = "Mario venceu!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        mario_movimento(keys_pressed, mario, gun)

        if mario.colliderect(Barreira_left):
            mario.x += 5

        hit_box(mario, gun)

        balas_disparadas(mario_balas, inimigo_hp)

        barreira(mario, gun)

        tela_ini(mario_hp, inimigo_hp, mario_balas, mario, aim, gun)

        pygame.mouse.set_visible(False)
        (aim.x, aim.y) = pygame.mouse.get_pos()
        aim.x -= aim.height / 2
        aim.y -= aim.width / 2

    main()


if __name__ == "__main__":
    main()