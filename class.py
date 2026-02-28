class  Anjo:
    def __init__ (self , nome , poder , evolucao):
        self.nome = nome
        self.poder = poder
        self.evolucao = evolucao


anjo1 = Anjo ("itadori" , "kokusen" , "sukuna")
anjo2 = Anjo ("satoru gojo" , "infinito" , "seis olhos")
anjo3 = Anjo ("geto" , "manipulacao de espiritos" , "kenjaku")

print("o nome, poder e evolucao dos anjos 1, 2 e 3 sao: " + anjo1.nome + ", " + anjo2.poder + " e " + anjo3.evolucao)