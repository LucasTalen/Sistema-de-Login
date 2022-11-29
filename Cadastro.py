
from tkinter import *


class Cadastro:
    def __init__(self, master=None):
        self.Tela()

        imgFundo = PhotoImage(file="Aserts\\Cadastro.png")
        labfundo = Label(janela, image=imgFundo)      
        labfundo.pack()

        janela.mainloop()

    def Tela(self):
        janela.title("Cadastro")
        janela.geometry("380x514")
        janela.resizable(width=False, height=False)


def CriarUsuario(self):
    with open("BancoDeDados.txt", "r") as arquivo:
        arquivo.read()


janela = Tk()
Cadastro(janela)