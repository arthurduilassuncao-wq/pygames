nome_heroi = input("qual o nome do seu heroi? ")


arquivo = open("recorde.txt" , "w")
arquivo.write("O recorde do heroi " + nome_heroi + "\nNivel atual de 999 pontos!")
arquivo.close()




