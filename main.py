from tkinter import *
from tkinter import messagebox

janela = Tk()
class Aplicativo:

    def Menu(self):
        self.Tela()

        imgFundo = PhotoImage(file="Aserts\\Menu.png")
        labfundo = Label(janela, image=imgFundo)      
        labfundo.pack()

        self.Login1 = Button(janela,text="Login", command=self.chamarLogin, background="#d9d9d9")
        self.Login1.place(x=123, y=225,width=150, height=20)

        self.Cadastro = Button(janela,text="Cadastrar", background="#d9d9d9")
        self.Cadastro.place(x=123, y=270,width=150, height=20)

        self.BancoDeDados = Button(janela,text="Banco De Dados", background="#d9d9d9")
        self.BancoDeDados.place(x=123, y=325,width=150, height=20)


        janela.mainloop()

    def Tela(self):
        janela.title("Menu")
        janela.geometry("380x514")
        janela.resizable(width=False, height=False)

    Menu()
