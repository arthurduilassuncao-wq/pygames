import pygame
import random

pygame.init()

fonte = pygame.font.SysFont("Arial", 30, bold=True)
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("A Ascensão de Shadow Monarchy")

# Dados do Jogador
jogador_pos = [400, 300]
pontos = 0
velocidade_base = 5
# Desenhar Personagens
    
img_heroi = pygame.image.load("shadow_monarchy.png")
img_heroi = pygame.transform.scale(img_heroi, (50, 50))
img_monstro = pygame.image.load("monstro.png")
img_monstro = pygame.transform.scale(img_monstro, (60, 60))
img_item = pygame.image.load("scroll.png")
img_item = pygame.transform.scale(img_item, (20, 20))


# Dados do Item
item_pos = [200, 200]

# --- NOVO: Dados do Inimigo ---
inimigo_pos = [0, 0]
velocidade_inimigo = 2 

relogio = pygame.time.Clock()
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # 1. Lógica de Velocidade do Jogador
    velocidade_jogador = velocidade_base + pontos
    if pontos >= 5:
        velocidade_jogador = velocidade_base + 10

    # 2. Movimentação do Jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a]: jogador_pos[0] -= velocidade_jogador
    if teclas[pygame.K_d]: jogador_pos[0] += velocidade_jogador
    if teclas[pygame.K_w]: jogador_pos[1] -= velocidade_jogador
    if teclas[pygame.K_s]: jogador_pos[1] += velocidade_jogador

    # --- NOVO: IA do Inimigo (Perseguição) ---
    if inimigo_pos[0] < jogador_pos[0]: inimigo_pos[0] += velocidade_inimigo
    if inimigo_pos[0] > jogador_pos[0]: inimigo_pos[0] -= velocidade_inimigo
    if inimigo_pos[1] < jogador_pos[1]: inimigo_pos[1] += velocidade_inimigo
    if inimigo_pos[1] > jogador_pos[1]: inimigo_pos[1] -= velocidade_inimigo

    # 3. Retângulos de Colisão
    jogador_rect = pygame.Rect(jogador_pos[0], jogador_pos[1], 50, 50)
    item_rect = pygame.Rect(item_pos[0], item_pos[1], 20, 20)
    inimigo_rect = pygame.Rect(inimigo_pos[0], inimigo_pos[1], 40, 40) # Rect do Inimigo

    # 4. Colisão com Item
    if jogador_rect.colliderect(item_rect):
        pontos += 1
        item_pos[0] = random.randint(50, 750)
        item_pos[1] = random.randint(50, 550)

    # --- NOVO: Colisão com Inimigo (Game Over / Reset) ---
    if jogador_rect.colliderect(inimigo_rect):
        print("O Vulto te pegou!")
        pontos = 0 # Perde o poder
        inimigo_pos = [0, 0] # Inimigo volta pro início
        jogador_pos = [400, 300] # Você é teleportado

    # 5. Desenho
    tela.fill((30, 30, 30))
    
    # Texto do Placar
    cor_texto = (255, 255, 255)
    aviso = ""
    if pontos >= 5:
        cor_texto = (136, 231, 136)
        aviso = " - TURBO ATIVADO!"
    
    texto_placar = fonte.render(f"Sombras: {pontos}{aviso}", True, cor_texto)
    tela.blit(texto_placar, (10, 10))
    
    #desenhar personagens
    
    tela.blit(img_heroi, (jogador_pos[0], jogador_pos[1]))
    tela.blit(img_monstro, (inimigo_pos[0], inimigo_pos[1]))
    tela.blit(img_item, (item_pos[0], item_pos[1]))

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()