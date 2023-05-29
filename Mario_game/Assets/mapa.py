import pygame

# p = parede
# vazio  = espaço em branco

mapa = [
        "pppppppppppppppppppppppppppppppppppppppp",
        "p                                      p",
        "p                                      p",
        "p                                      p",
        "p                        ppp           p",
        "p                       p p p          p",
        "p                      p  p  p         p",
        "p                     pp     pp        p",
        "p                     p ppppp p        p",
        "p                     p       p        p",
        "p                     p       p        p",
        "p                     p       p        p",
        "p                     p       p        p",
        "p               ppppppp       ppppppp  p",
        "p               p     p       p     p  p",
        "p               p     p       p     p  p",
        "p               ppppppp       ppppppp  p",
        "p                                      p",
        "p                                      p",
        "pppppppppppppppppppppppppppppppppppppppp",

]
amarelo = (255, 255, 0)
preto = (0, 0, 0)
largura = 800
altura = 600

BLK_LARGURA = largura / 40
BLK_ALTURA = altura / 20

pygame.init()
tela = pygame.display.set_mode((largura, altura))

for id_linha, linha in enumerate(mapa):
    for id_coluna, caracter in enumerate(linha):
        cor = preto
        if caracter == 'p':
            cor = amarelo
        x = id_coluna * BLK_LARGURA
        y = id_linha * BLK_ALTURA
        r = pygame.Rect((x, y), (BLK_LARGURA, BLK_LARGURA))
        pygame.draw.rect(tela, cor, r, 0)
pygame.display.update()


while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
