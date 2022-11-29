
from tkinter import *

class Menu:
    def __init__(self, master=None):
        self.Tela()

        imgFundo = PhotoImage(file="Aserts\\Menu.png")
        labfundo = Label(janela, image=imgFundo)      
        labfundo.pack()
        janela.mainloop()


    def Tela(self):
        janela.title("Menu")
        janela.geometry("380x514")
        janela.resizable(width=False, height=False)

janela = Tk()
Menu(janela)