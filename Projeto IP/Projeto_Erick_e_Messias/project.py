import pygame
import random
import time

pygame.init()
#TODAS AS IMAGENS QUE VÃO SER USADAS
fundo_balao = [pygame.image.load("Dialogo/frase1.jpg"), pygame.image.load("Dialogo/frase2.jpg"), pygame.image.load("Dialogo/frase3.png"), pygame.image.load("Dialogo/frase4.jpg")]
tabela = [pygame.image.load("pictures/moldura.png"), pygame.image.load("pictures/moldura1.png")]
fundo_balao1 = (pygame.transform.scale(fundo_balao[0], (1000, 600)), pygame.transform.scale(fundo_balao[1], (1000, 600)), pygame.transform.scale(fundo_balao[2], (1000, 600)), pygame.transform.scale(fundo_balao[3], (1000, 600)))
fundo02 = pygame.image.load("pictures/fundo02.png")
fundo02 = pygame.transform.scale(fundo02,(1000,600))
score = pygame.image.load("pictures/score.png")

#GIF DA TELA TELA INICIAL
telainicial = [pygame.image.load("telainicial/img0.png"), pygame.image.load("telainicial/img1.png"), pygame.image.load("telainicial/img2.png"), pygame.image.load("telainicial/img3.png"), pygame.image.load("telainicial/img4.png"), pygame.image.load("telainicial/img5.png"), pygame.image.load("telainicial/img6.png"), pygame.image.load("telainicial/img7.png")]

#GIF DO MAGO DE MOVENDO PARA VITORIA JOGADOR 1
mago1 = [pygame.image.load("wins1/jog1mago0.png"), pygame.image.load("wins1/jog1mago1.png"), pygame.image.load("wins1/jog1mago2.png"), pygame.image.load("wins1/jog1mago3.png"), pygame.image.load("wins1/jog1mago4.png"), pygame.image.load("wins1/jog1mago5.png"), pygame.image.load("wins1/jog1mago6.png"), pygame.image.load("wins1/jog1mago7.png")]
mago1_2 = [pygame.image.load("wins1/jog1mago8.png"), pygame.image.load("wins1/jog1mago9.png"), pygame.image.load("wins1/jog1mago10.png"), pygame.image.load("wins1/jog1mago11.png"), pygame.image.load("wins1/jog1mago12.png"), pygame.image.load("wins1/jog1mago13.png"), pygame.image.load("wins1/jog1mago14.png"), pygame.image.load("wins1/jog1mago15.png")]
mago1_3 = [pygame.image.load("wins1/jog1mago16.png"), pygame.image.load("wins1/jog1mago17.png"), pygame.image.load("wins1/jog1mago18.png"), pygame.image.load("wins1/jog1mago19.png"), pygame.image.load("wins1/jog1mago20.png"), pygame.image.load("wins1/jog1mago21.png"), pygame.image.load("wins1/jog1mago22.png"), pygame.image.load("wins1/jog1mago23.png")]
mago1_4 = [pygame.image.load("wins1/jog1mago24.png"), pygame.image.load("wins1/jog1mago25.png")]
def winsjogador1():
    clock.tick(fps)
    for r in range(10):
        for i in range(8):
            clock.tick(fps)
            tela.blit(mago1[i],(0,0))
            pygame.display.update()
        for i in range(8):
            clock.tick(fps)
            tela.blit(mago1_2[i],(0,0))
            pygame.display.update()
        for i in range(8):
            clock.tick(fps)
            tela.blit(mago1_3[i],(0,0))
            pygame.display.update()
        for i in range(2):
            clock.tick(fps)
            tela.blit(mago1_4[i],(0,0))
            pygame.display.update()
    return(winsjogador1)

#GIF MAGO SE MOVENDO PARA VITORIA JOGADOR 2
mago2 = [pygame.image.load("wins2/jog2mago0.png"), pygame.image.load("wins2/jog2mago1.png"), pygame.image.load("wins2/jog2mago2.png"), pygame.image.load("wins2/jog2mago3.png"), pygame.image.load("wins2/jog2mago4.png"), pygame.image.load("wins2/jog2mago5.png"), pygame.image.load("wins2/jog2mago6.png"), pygame.image.load("wins2/jog2mago7.png")]
mago2_2 = [pygame.image.load("wins2/jog2mago8.png"), pygame.image.load("wins2/jog2mago9.png"), pygame.image.load("wins2/jog2mago10.png"), pygame.image.load("wins2/jog2mago11.png"), pygame.image.load("wins2/jog2mago12.png"), pygame.image.load("wins2/jog2mago13.png"), pygame.image.load("wins2/jog2mago14.png"), pygame.image.load("wins2/jog2mago15.png")]
mago2_3 = [pygame.image.load("wins2/jog2mago16.png"),pygame.image.load("wins2/jog2mago17.png"), pygame.image.load("wins2/jog2mago18.png"), pygame.image.load("wins2/jog2mago19.png"), pygame.image.load("wins2/jog2mago20.png"), pygame.image.load("wins2/jog2mago21.png"), pygame.image.load("wins2/jog2mago22.png"), pygame.image.load("wins2/jog2mago23.png")]
mago2_4 = [pygame.image.load("wins2/jog2mago24.png"), pygame.image.load("wins2/jog2mago25.png")]
def winsjogador2():
    clock.tick(fps)
    for i in range(10):
        for i in range(8):
            clock.tick(fps)
            tela.blit(mago2[i],(0,0))
            pygame.display.update()
        for i in range(8):
            clock.tick(fps)
            tela.blit(mago2_2[i],(0,0))
            pygame.display.update()
        for i in range(8):
            clock.tick(fps)
            tela.blit(mago2_3[i],(0,0))
            pygame.display.update()
        for i in range(2):
            clock.tick(fps)
            tela.blit(mago2_4[i],(0,0))
            pygame.display.update()
    return(winsjogador2)
#GIF MAGO SE MOVENDO PARA EMPATE
empate = [pygame.image.load("empate/empate0.png"), pygame.image.load("empate/empate1.png"), pygame.image.load("empate/empate2.png"), pygame.image.load("empate/empate3.png"), pygame.image.load("empate/empate4.png"), pygame.image.load("empate/empate5.png"), pygame.image.load("empate/empate6.png"), pygame.image.load("empate/empate7.png")]
empate1 = [pygame.image.load("empate/empate8.png"), pygame.image.load("empate/empate9.png"), pygame.image.load("empate/empate10.png"), pygame.image.load("empate/empate11.png"), pygame.image.load("empate/empate12.png"), pygame.image.load("empate/empate13.png"), pygame.image.load("empate/empate14.png"), pygame.image.load("empate/empate15.png")]
empate2 = [pygame.image.load("empate/empate16.png"), pygame.image.load("empate/empate17.png"), pygame.image.load("empate/empate18.png"), pygame.image.load("empate/empate19.png"), pygame.image.load("empate/empate20.png"), pygame.image.load("empate/empate21.png"), pygame.image.load("empate/empate22.png"), pygame.image.load("empate/empate23.png")]
empate3 = [pygame.image.load("empate/empate24.png"), pygame.image.load("empate/empate25.png")]

jogador1 = 0
jogador2 = 0
clock = pygame.time.Clock()
fps = 18

preto = (0,0,0)
dourado = (255, 200, 0)
fonte = pygame.font.Font("8-Bit Madness.ttf", 45) #FONTE

lado_celula = 100
n_linhas = 4
n_linhas1 = 6
#CRIANDO A TELA
tela = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Caça ao Tesouro - RPG")
#SONS DO BAU E GOBLIN
sombau = pygame.mixer.Sound("sons/sombau.wav")
somgoblin = pygame.mixer.Sound("sons/somgoblin.wav")
#SOM DE FUNDO
somfundo = pygame.mixer.music.load("sons/GreenSleeves.mp3")
pygame.mixer.music.play(-1)

num_goblins = 0
num_tesouro = 0
conteudo_celula = [[0 for i in range(n_linhas1)] for j in range(n_linhas1)]
cont = 0
giftela = True
#GIF TELA INICIAL
while giftela:
    for r in range(1):
        for i in range(7):
            clock.tick(12)
            tela.blit(telainicial[i], (0,0))
            pygame.display.update()

    for evento in pygame.event.get():

        if (evento.type == pygame.QUIT):
            giftela = False

        if (evento.type == pygame.MOUSEBUTTONDOWN):
            mous_x, mous_y = pygame.mouse.get_pos()

            cel_x = mous_x // lado_celula
            cel_y = mous_y // lado_celula

            if (cel_x >= 2 and cel_x <= 7) and (cel_y >= 4 and cel_y <= 5):
                giftela = False
                tela_inicial = True
#CONVERSA DO MAGO COM OS JOGADORES
while tela_inicial:
    for evento in pygame.event.get():

        if (evento.type==pygame.QUIT):
            tela_inicial = False

        if (evento.type == pygame.MOUSEBUTTONDOWN and cont == 0):
            tela.blit(fundo_balao1[0], (0,0))
            pygame.display.update()
            cont += 1
        elif (evento.type == pygame.MOUSEBUTTONDOWN and cont == 1 ):
            tela.blit(fundo_balao1[1], (0,0))
            pygame.display.update()
            cont += 1
        elif (evento.type == pygame.MOUSEBUTTONDOWN and cont == 2 ):
            tela.blit(fundo_balao1[2], (0,0))
            pygame.display.update()
            cont += 1
        elif (evento.type == pygame.MOUSEBUTTONDOWN and cont == 3):
            tela.blit(fundo_balao1[3], (0,0))
            pygame.display.update()
            cont += 1
        elif (evento.type == pygame.MOUSEBUTTONDOWN and cont == 4):
            tela_inicial = False
            jogo = True

if jogo:
    tela.blit(fundo02,(0,0))
    tela.blit(tabela[1], (41, 59))
    for i in range(0, n_linhas):
        for j in range(0, n_linhas):
            pygame.draw.rect(tela, preto, ((lado_celula*i) + 100, (lado_celula*j) + 110, lado_celula, lado_celula), 1)
    tela.blit(tabela[0], (41,59))
    pygame.display.update()
#DEFININDO O NÚMERO DE TESOUROS E SUA POSIÇÃO
    while (num_tesouro < 6):
        T = random.randint(1, 100)
        T2 = random.randint(1, 16)
        tes = 0
        for i in range(1,5):
            for j in range(1,5):
                if (conteudo_celula[i][j] == 0 and tes == T2 ):
                    if(T > 40):
                        conteudo_celula[i][j] = "O"
                        num_tesouro += 1
                tes += 1
#DEFININDO O NÚMERO DE GOBLIN E SUA POSIÇÃO
    while (num_goblins < 3):
        G = random.randint(1, 100)
        G2 = random.randint(1, 16)
        gob = 0
        for i in range(1,5):
            for j in range(1,5):
                if (conteudo_celula[i][j] == 0 and gob == G2):
                    if(G > 70):
                        conteudo_celula[i][j] = "G"
                        num_goblins += 1
                gob += 1

    for i in range(1,5):
        for j in range(1,5):

            if (conteudo_celula[i][j] != "O" and conteudo_celula[i][j] != "G"):
                n_de_tesouros = 0
                #Acima
                if (i - 1 >= 0 and conteudo_celula[i - 1][j]) == "O":
                    n_de_tesouros += 1
                #Abaixo
                if (i + 1 < n_linhas and conteudo_celula[i + 1][j]) == "O":
                    n_de_tesouros += 1
                #Esquerda
                if (j - 1 >= 0 and conteudo_celula[i][j - 1]) == "O":
                    n_de_tesouros += 1
                #Direita
                if (j + 1 < n_linhas and conteudo_celula[i][j + 1]) == "O":
                    n_de_tesouros +=1

                conteudo_celula[i][j] = str(n_de_tesouros)

    celula = [[False for i in range(n_linhas1)] for j in range(n_linhas1)]

    jogo_interrompido = True
    jogador1_ganhou = False
    jogador2_ganhou = False
    contcelula = 0
    vez = 0

    tela.blit(score, (550, 110))
    pygame.display.update()
    while jogo_interrompido:

        jogada = True

        for evento in pygame.event.get():

            if (evento.type==pygame.QUIT):
                jogo_interrompido = False

            if (jogador1_ganhou) or (jogador2_ganhou):
                continue

            tela_mudou = False

            if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):
                mouse_x, mouse_y = evento.pos

                celula_x = mouse_x // lado_celula
                celula_y = mouse_y // lado_celula

                if (celula_x >= 1 and celula_x <= 4) and (celula_y >= 1 and celula_y <= 4):

                    if (not celula[celula_x][celula_y]):
                        tela_mudou = True
                        celula[celula_x][celula_y] = True
                        #JOGADOR 1 VS JOGADOR 2
                        while jogada:
                            if (vez == 0):
                                if (conteudo_celula[celula_x][celula_y] == "O" and contcelula != 16):
                                    jogador1 += 100
                                    tela.blit(score, (550, 110))
                                    texto1 = fonte.render("{}".format(jogador1), True, preto)
                                    tela.blit(texto1,(700,270))
                                    texto2 = fonte.render("{}".format(jogador2), True, preto)
                                    tela.blit(texto2,(700,380))
                                    pygame.display.update()
                                    contcelula += 1
                                    vez += 1
                                    jogada = False
                                    break
                                elif (conteudo_celula[celula_x][celula_y] == "G" and contcelula != 16):
                                    if(jogador1 == 0):
                                        jogador1 = 0
                                        tela.blit(score, (550, 110))
                                        texto1 = fonte.render("{}".format(jogador1), True, preto)
                                        tela.blit(texto1,(700,270))
                                        texto2 = fonte.render("{}".format(jogador2), True, preto)
                                        tela.blit(texto2,(700,380))
                                        pygame.display.update()
                                        vez += 1
                                        contcelula += 1
                                        jogada = False
                                        break
                                    elif(jogador1 > 0):
                                        jogador1 -= 50
                                        tela.blit(score, (550, 110))
                                        texto1 = fonte.render("{}".format(jogador1), True, preto)
                                        tela.blit(texto1,(700,270))
                                        texto2 = fonte.render("{}".format(jogador2), True, preto)
                                        tela.blit(texto2,(700,380))
                                        pygame.display.update()
                                        contcelula += 1
                                        vez +=1
                                        jogada = False
                                        break
                                else:
                                    vez += 1
                                    contcelula += 1
                                    jogada = False
                                    break
                            if(vez == 1):
                                if (conteudo_celula[celula_x][celula_y] == "O" and contcelula != 16):
                                    jogador2 += 100
                                    tela.blit(score, (550, 110))
                                    texto2 = fonte.render("{}".format(jogador2), True, preto)
                                    tela.blit(texto2,(700,380))
                                    texto1 = fonte.render("{}".format(jogador1), True, preto)
                                    tela.blit(texto1,(700,270))
                                    pygame.display.update()
                                    vez = 0
                                    contcelula += 1
                                    jogada = False
                                    break
                                elif(conteudo_celula[celula_x][celula_y] == "G" and contcelula != 16):
                                    if(jogador2 == 0):
                                        jogador2 = 0
                                        tela.blit(score, (550, 110))
                                        texto2 = fonte.render("{}".format(jogador2), True, preto)
                                        tela.blit(texto2,(700,380))
                                        texto1 = fonte.render("{}".format(jogador1), True, preto)
                                        tela.blit(texto1,(700,270))
                                        pygame.display.update()
                                        vez = 0
                                        contcelula += 1
                                        jogada = False
                                        break
                                    elif(jogador2 > 0):
                                        jogador2 -= 50
                                        tela.blit(score, (550, 110))
                                        texto2 = fonte.render("{}".format(jogador2), True, preto)
                                        tela.blit(texto2,(700,380))
                                        texto1 = fonte.render("{}".format(jogador1), True, preto)
                                        tela.blit(texto1,(700,270))
                                        pygame.display.update()
                                        vez = 0
                                        contcelula += 1
                                        jogada = False
                                        break
                                else:
                                    vez = 0
                                    contcelula += 1
                                    jogada = False
                                    break
                if (tela_mudou):
                    i = celula_x
                    j = celula_y
                    if(conteudo_celula[i][j] == "O"):
                        pygame.mixer.music.set_volume(10)
                        sombau.play()
                        bau = pygame.image.load('pictures/bau.png')
                        bau = pygame.transform.scale(bau, (lado_celula - 2, lado_celula - 2))
                        tela.blit(bau, (lado_celula*i + 1, lado_celula*j + 1))
                    elif(conteudo_celula[i][j] == "G"):
                        pygame.mixer.music.set_volume(10)
                        somgoblin.play()
                        goblin = pygame.image.load('pictures/goblin.png')
                        goblin = pygame.transform.scale(goblin, (lado_celula - 2, lado_celula - 2))
                        tela.blit(goblin, (lado_celula*i + 2, lado_celula*j + 10))
                    else:
                        texto = fonte.render(conteudo_celula[i][j], True, preto)
                        tela.blit(texto, (lado_celula*i + 0.4*lado_celula, lado_celula*j + 0.4*lado_celula))
                    pygame.mixer.music.set_volume(80)
                    pygame.display.update()

                if (contcelula == 16):
                    if(jogador1 > jogador2): #CHAMAR A FUNÇÃO DO GIF
                        winsjogador1()
                        jogo_interrompido = False
                    elif (jogador2 > jogador1): #CHAMAR A FUNÇÃO DO GIF
                        winsjogador2()
                        jogo_interrompido = False
                    elif(jogador1 == jogador2):
                        for i in range(10):
                            for i in range(8):
                                clock.tick(fps)
                                tela.blit(empate[i],(0,0))
                                pygame.display.update()
                            for i in range(8):
                                clock.tick(fps)
                                tela.blit(empate1[i],(0,0))
                                pygame.display.update()
                            for i in range(8):
                                clock.tick(fps)
                                tela.blit(empate2[i],(0,0))
                                pygame.display.update()
                            for i in range(2):
                                clock.tick(fps)
                                tela.blit(empate3[i],(0,0))
                                pygame.display.update()
                        jogo_interrompido = False
pygame.quit()
#MELHOR PROJETO!!!
