import pygame
from pygame.locals import * 
import random
import time

WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600
POS_X_INICIAL = WINDOWS_WIDTH/2
POS_Y_INICIAL = WINDOWS_HEIGHT/2
BLOCK = 10
def iniciarGame():
    def gameOver():
        pygame.font.init()
        fonte = pygame.font.SysFont('arial', 60, True, False)
        gameOverTxt = 'GAME OVER'
        textOver = fonte.render(gameOverTxt, True, (255,255,255))
        window.blit(textOver, (110, 300))
        pygame.display.update()
        time.sleep(2)
        iniciarGame()
        # pygame.quit()
        # quit()
    def colisao(pos1, pos2):
        return pos1 == pos2

    def verificaMargem(pos):
        if 0 <= pos[0] < WINDOWS_WIDTH and 0 <= pos[1] < WINDOWS_HEIGHT:
            return False
        else: return True 

    obstaculoPos = []
    def posAleatoria():
        x = random.randint(0, WINDOWS_WIDTH)
        y = random.randint(0, WINDOWS_HEIGHT)
        if (x,y) in obstaculoPos:
            posAleatoria()
        return x // BLOCK * BLOCK, y // BLOCK * BLOCK

    pygame.init() #iniciando a biblioteca PYGAME
    window = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
    pygame.display.set_caption('Joga da cobrinha')


    cobraPos = [(POS_X_INICIAL, POS_Y_INICIAL),(POS_X_INICIAL+BLOCK, POS_Y_INICIAL),(POS_X_INICIAL+(2*BLOCK), POS_Y_INICIAL)]
    cobraSurface = pygame.Surface((BLOCK, BLOCK))
    cobraSurface.fill((53,59,72))
    direcao = K_LEFT

    macaSurface = pygame.Surface((BLOCK, BLOCK))
    macaSurface.fill((255,0,0))
    macaPos = posAleatoria()

    count = 0
    speed = 15

    pygame.font.init()
    fonte = pygame.font.SysFont('arial', 35, True, False)

    obstaculoSurface = pygame.Surface((BLOCK, BLOCK))
    obstaculoSurface.fill((0,0,0))

    while True:
        pygame.time.Clock().tick(speed)
        window.fill((68,189,50))

        mensagem = f'Pontos: {count}'
        texto = fonte.render(mensagem, True, (255,255,255))

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                quit()
            elif evento.type == KEYDOWN:
                if evento.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                    if evento.key == K_UP and direcao == K_DOWN:
                        continue
                    elif evento.key == K_DOWN and direcao == K_UP:
                        continue
                    elif evento.key == K_LEFT and direcao == K_RIGHT:
                        continue
                    elif evento.key == K_RIGHT and direcao == K_LEFT:
                        continue
                    else: direcao = evento.key

        window.blit(macaSurface,macaPos)

        if colisao(cobraPos[0], macaPos):
            cobraPos.append((-10,-10))
            macaPos = posAleatoria()
            obstaculoPos.append(posAleatoria())
            count = count + 1
            print(count, speed)
            if count%5 == 0:
                speed += 3

        for pos in obstaculoPos:
            if colisao(cobraPos[0], pos):
                gameOver()
            window.blit(obstaculoSurface, pos)

        for pos in cobraPos:
            window.blit(cobraSurface,pos) #metodo para desenhar algo na tela

        for item in range(len(cobraPos)-1, 0, -1):
            if colisao(cobraPos[0], cobraPos[item]):
                gameOver()
            cobraPos[item] = cobraPos[item-1]

        if verificaMargem(cobraPos[0]):
            gameOver()

        if direcao == K_RIGHT:
            cobraPos[0] = cobraPos[0][0] + BLOCK, cobraPos[0][1]
        elif direcao == K_LEFT:
            cobraPos[0] = cobraPos[0][0] - BLOCK, cobraPos[0][1]
        elif direcao == K_UP:
            cobraPos[0] = cobraPos[0][0], cobraPos[0][1] - BLOCK 
        elif direcao == K_DOWN:
            cobraPos[0] = cobraPos[0][0], cobraPos[0][1] + BLOCK

        window.blit(texto, (420, 18))
        pygame.display.update()
iniciarGame()