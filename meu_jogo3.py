import pygame
import random # Vamos usar para o item aparecer em lugares aleatórios

pygame.init()

fonte = pygame.font.SysFont("Arial", 30, bold=True)
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("A Ascensão de Shadow Monarchy")

jogador_pos = [400, 300]
item_pos = [200, 200]
velocidade_base = 5
pontos = 0

relogio = pygame.time.Clock()
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # 1. Movimentação (Lido a cada frame, fora do for de eventos)
    teclas = pygame.key.get_pressed()

    if pontos >= 5:
        velocidade_jogador = velocidade_base + 10
    else:
        velocidade_jogador = velocidade_base + pontos
    

    if teclas[pygame.K_a]: jogador_pos[0] -= velocidade_jogador
    if teclas[pygame.K_d]: jogador_pos[0] += velocidade_jogador
    if teclas[pygame.K_w]: jogador_pos[1] -= velocidade_jogador
    if teclas[pygame.K_s]: jogador_pos[1] += velocidade_jogador

    # 2. Criando os Retângulos de Colisão (Invisíveis, servem para o cálculo)
    jogador_rect = pygame.Rect(jogador_pos[0], jogador_pos[1], 50, 50)
    item_rect = pygame.Rect(item_pos[0], item_pos[1], 20, 20)

    # 3. Teste de Colisão
    if jogador_rect.colliderect(item_rect):
        pontos += 1
        print(f"Sombra coletada! Total: {pontos}")
        # Move o item para um lugar novo aleatório
        item_pos[0] = random.randint(50, 750)
        item_pos[1] = random.randint(50, 550)
    
        # 4. Desenho
    tela.fill((30, 30, 30))
    # Cria a "imagem" do texto com os pontos atuais
    texto_placar = fonte.render(f"Sombras: {pontos}", True, (255, 255, 255))
    if velocidade_jogador >= 10:
        texto_placar = fonte.render(f"Sombras: {pontos} - Velocidade maxima atingida!", True, (136, 231, 136))

    # Desenha o texto na posição (10, 10)
    tela.blit(texto_placar, (10, 10))
    
    # Desenha o Jogador (Roxo)
    pygame.draw.rect(tela, (128, 0, 128), jogador_rect)
    
    # Desenha o Item (Dourado)
    pygame.draw.rect(tela, (255, 215, 0), item_rect)

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()