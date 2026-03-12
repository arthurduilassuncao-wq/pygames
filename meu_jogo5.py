import pygame
import random

pygame.init()

# Fonte
fonte = pygame.font.SysFont("Arial", 30, bold=True)

# Tela
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("A Ascensão de Shadow Monarchy")

# =========================
# DADOS DO JOGADOR
# =========================
jogador_pos = [400, 300]
velocidade_base = 5
pontos = 0

# =========================
# IMAGENS
# =========================
img_heroi = pygame.image.load("shadow_monarchy.png")
img_heroi = pygame.transform.scale(img_heroi, (50, 50))

img_monstro = pygame.image.load("monstro.png")
img_monstro = pygame.transform.scale(img_monstro, (60, 60))

img_item = pygame.image.load("scroll.png")
img_item = pygame.transform.scale(img_item, (20, 20))

# =========================
# ITEM
# =========================
item_pos = [200, 200]

# =========================
# INIMIGO
# =========================
inimigo_pos = [random.randint(0,750), random.randint(0,550)]
velocidade_inimigo = 2

# =========================
# PAREDE
# =========================
parede_rect = pygame.Rect(300, 400, 200, 50)

# =========================
# MENU
# =========================
botao_rect = pygame.Rect(300, 250, 200, 50)

# =========================
# ESTADO DO JOGO
# =========================
estado = "MENU"

# =========================
# LOOP
# =========================
relogio = pygame.time.Clock()
rodando = True

while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if estado == "MENU":
                if botao_rect.collidepoint(evento.pos):
                    estado = "JOGANDO"

    # =========================
    # MENU
    # =========================
    if estado == "MENU":

        tela.fill((20,20,20))

        pos_mouse = pygame.mouse.get_pos()

        if botao_rect.collidepoint(pos_mouse):
            cor_botao = (128,0,128)
        else:
            cor_botao = (255,255,0)

        pygame.draw.rect(tela, cor_botao, botao_rect)

        txt = fonte.render("START GAME", True, (0,0,0))
        tela.blit(txt,(325,260))

        titulo = fonte.render("A ASCENSAO DE SHADOW MONARCHY",True,(255,215,0))
        tela.blit(titulo,(140,150))

    # =========================
    # JOGO
    # =========================
    elif estado == "JOGANDO":

        # Velocidade do jogador
        if pontos < 5:
            velocidade_jogador = velocidade_base + pontos
        else:
            velocidade_jogador = velocidade_base + 10

        pos_antiga_x = jogador_pos[0]
        pos_antiga_y = jogador_pos[1]

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_a]:
            jogador_pos[0] -= velocidade_jogador
        if teclas[pygame.K_d]:
            jogador_pos[0] += velocidade_jogador
        if teclas[pygame.K_w]:
            jogador_pos[1] -= velocidade_jogador
        if teclas[pygame.K_s]:
            jogador_pos[1] += velocidade_jogador

        # IA inimigo
        if inimigo_pos[0] < jogador_pos[0]:
            inimigo_pos[0] += velocidade_inimigo
        elif inimigo_pos[0] > jogador_pos[0]:
            inimigo_pos[0] -= velocidade_inimigo

        if inimigo_pos[1] < jogador_pos[1]:
            inimigo_pos[1] += velocidade_inimigo
        elif inimigo_pos[1] > jogador_pos[1]:
            inimigo_pos[1] -= velocidade_inimigo

        # Retângulos
        jogador_rect = pygame.Rect(jogador_pos[0], jogador_pos[1],50,50)
        item_rect = pygame.Rect(item_pos[0], item_pos[1],20,20)
        inimigo_rect = pygame.Rect(inimigo_pos[0], inimigo_pos[1],60,60)

        # Colisão parede
        if jogador_rect.colliderect(parede_rect):
            jogador_pos[0] = pos_antiga_x
            jogador_pos[1] = pos_antiga_y

        # Colisão item
        if jogador_rect.colliderect(item_rect):
            pontos += 1
            item_pos[0] = random.randint(50,750)
            item_pos[1] = random.randint(50,550)

        # Vitória
        if pontos >= 10:
            estado = "VITORIA"

        # Colisão inimigo
        if jogador_rect.colliderect(inimigo_rect):

            print("O vulto te pegou!")

            pontos = 0
            jogador_pos = [400,300]

            inimigo_pos = [
                random.randint(0,750),
                random.randint(0,550)
            ]

            item_pos = [
                random.randint(50,750),
                random.randint(50,550)
            ]

        # Desenho
        tela.fill((30,30,30))

        pygame.draw.rect(tela,(100,100,100),parede_rect)

        cor_texto = (255,255,255)
        aviso = ""

        if pontos >= 5:
            cor_texto = (136,231,136)
            aviso = " - TURBO!"

        texto = fonte.render(f"Sombras: {pontos}{aviso}",True,cor_texto)
        tela.blit(texto,(10,10))

        tela.blit(img_heroi,jogador_pos)
        tela.blit(img_monstro,inimigo_pos)
        tela.blit(img_item,item_pos)

    # =========================
    # VITORIA
    # =========================
    elif estado == "VITORIA":

        tela.fill((0,0,0))

        tela.blit(img_heroi,(375,150))

        msg = fonte.render(
            "VOCE SE TORNOU O REI DAS SOMBRAS!",
            True,(255,215,0)
        )

        msg2 = fonte.render(
            "APERTE R PARA REINICIAR",
            True,(255,255,255)
        )

        tela.blit(msg,(140,250))
        tela.blit(msg2,(240,320))

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_r]:

            pontos = 0
            jogador_pos = [400,300]
            inimigo_pos = [random.randint(0,750),random.randint(0,550)]

            estado = "JOGANDO"

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
