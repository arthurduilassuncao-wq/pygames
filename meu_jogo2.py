import pygame

pygame.init()

# 2. Criar a tela do jogo

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("A Ascensão de Shadow Monarchy")

jogador_pos = [400, 300]

# 3. O Loop do Jogo
velocidade = 5
rodando = True
relogio = pygame.time.Clock()

while rodando:

    # Verificador de eventos (teclado, mouse, fechar janela)
    for evento in pygame.event.get():
        teclas = pygame.key.get_pressed()

    if teclas[pygame.K_a]:
        jogador_pos[0] -= velocidade
    if teclas[pygame.K_d]:
        jogador_pos[0] += velocidade
    if teclas[pygame.K_w]:
        jogador_pos[1] -= velocidade
    if teclas[pygame.K_s]:

        jogador_pos[1] += velocidade

    relogio.tick(60)

    if evento.type == pygame.QUIT:
            rodando = False

    # Preencher a tela com uma cor (R, G, B)

    tela.fill((30, 30, 30))

    # Desenhar o jogador (um quadrado roxo)

    pygame.draw.rect(tela, (128, 0, 128), (jogador_pos[0], jogador_pos[1], 50, 50))

    # Atualizar a tela

    pygame.display.flip()

# Encerrar o jogo

pygame.quit()