
from tkinter import *

class BancoDeDados:
    def __init__(self, master=None):
        self.Tela()

        imgFundo = PhotoImage(file="Aserts\\BancoDeDados.png")
        labfundo = Label(janela, image=imgFundo)      
        labfundo.pack()
        cont = "Lu:123"
        Contas = Label(janela, text=cont, background="#d9d9d9")
        Contas.place(x=48,y=183)
        janela.mainloop()


    def Tela(self):
        janela.title("Menu")
        janela.geometry("380x514")
        janela.resizable(width=False, height=False)

janela = Tk()
BancoDeDados(janela)