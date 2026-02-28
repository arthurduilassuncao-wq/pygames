import tkinter as tk

# Criando a janela principal)
janela = tk.Tk()
#configurando a janela)
janela.title("Certificado de Programador")
# definindo o tamanho da janela)
janela.geometry("1000x500")
# Criando um rotulo para o certificado)
Label = tk.Label(janela, text = "Parabéns, Arthur! Você dominou o Python!" , fg="purple")
# Exibindo o rotulo na janela)
Label.pack()
# Iniciando o loop principal da janela)
janela.mainloop()