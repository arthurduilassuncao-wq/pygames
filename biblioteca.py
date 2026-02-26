
import random

input("Pressione Enter para atacar o dragão...")

ataque = random.randint (1 , 10)

if ataque >= 8:
    print ("ataque critico! voce causou ", ataque , "de dano!")
if ataque <= 8:
    print ("voce causou ",ataque," de dano!")                         
           
