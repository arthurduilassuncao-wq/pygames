dados_salvos = open ("recorde.txt", "r")
conteudo = dados_salvos.read()
print("O sistema recuperou os seguinte dados: ", conteudo)
dados_salvos.close()