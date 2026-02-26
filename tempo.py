import time 
import random 

sua_vida = 100
vida_monstro = 100
ataque = random.randint(1, 10)
nome = input ("qual seu nome heroi? ") 
print ("o monstro apareceu" , nome , "prepare-se para a batalha!")

while vida_monstro > 0:
    dano_monstro = random.randint(1, 10)
    sua_vida -= dano_monstro
    ataque = random.randint(1, 10)
    vida_monstro -= ataque
    time.sleep(1.5)
    
    if dano_monstro > 10:
        print ("o monstro atacou voce com um golpe forte e causou" , dano_monstro , "de dano")
    if dano_monstro < 5:
        print ("voce desviou do ataque do monstro" , dano_monstro , "de dano")
    if ataque > 8:
        print ("critico o monstro sentiu o golpe", dano_monstro, "de dano!")
    if ataque < 3:
        print ("o monstro bloqueou parte do dano", ataque, "de dano!")
    if vida_monstro <= 0:
        print ("voce conseguiu ganhar do monstro" , nome , "parabens!")
    if sua_vida <= 0:
        print ("o monstro derrotou voce" , nome , "tente novamente!")
        break

    # Criando um arquivo chamado save.txt e escrevendo nele
arquivo = open("save.txt", "w")
arquivo.write("Heroi: Shadow Monarchy\nNivel: 2")
arquivo.close() # Sempre feche o arquivo quando terminar!

print("Jogo Salvo com sucesso!")




