energia_monstro = 100

def atacar():
    global energia_monstro
    energia_monstro = energia_monstro - 20
    print("Você deu um golpe! Energia do monstro:", energia_monstro)

    if energia_monstro <= 0:
        print ("o monstro foi derrotado")
    else:
        print ("o monstro ainda resiste")
    
    # AGORA É COM VOCÊ:
    # 1. Crie um IF aqui dentro para verificar se a energia é menor ou igual a 0
    # 2. Se for, dê um print("O monstro foi derrotado!")
    # 3. Se não, dê um print("O monstro ainda resiste!")

# Depois de terminar a função, chame ela 3 vezes para ver o monstro cair!
#atacar()
#atacar()
#atacar()
for i in range (5):
    atacar()
