import pygame


# 1. Iniciar o Pygame
pygame.init()

# 2. Criar a tela do jogo
tela = jogador_pos = [200, 200]
pygame.display.set_caption("A Ascensão de Shadow Monarchy")
jogador_pos = [400, 300]

# 3. O Loop do Jogo
item_pos = [200, 200]
velocidade = 5 
rodando = True
relogio = pygame.time.Clock()
while rodando:
    # Verificador de eventos (teclado, mouse, fechar janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a]:
        jogador_pos[0] -= velocidade
    if teclas[pygame.K_d]:
        jogador_pos[0] += velocidade
    if teclas[pygame.K_w]:
        jogador_pos[1] -= velocidade
    if teclas[pygame.K_s]:
        jogador_pos[1] += velocidade
    item_rect = pygame.draw.rect(tela, (255, 215, 0), (item_pos [0], item_pos [1], 20, 20))

    # Preencher a tela com uma cor (R, G, B)
    tela.fill((30, 30, 30))

    # Desenhar o jogador (um quadrado roxo)
    jogador_rect = pygame.Rect(jogador_pos[0], jogador_pos[1], 50, 50)
    pygame.draw.rect(tela, (128, 0, 128), jogador_rect)
    if jogador_rect.colliderect(item_rect):
        item_pos = [1000, 1000]
        print(" Sombra coletada!")

    # Atualizar a tela
    pygame.display.flip()

    relogio.tick(60)

# Encerrar o jogo
pygame.quit()
