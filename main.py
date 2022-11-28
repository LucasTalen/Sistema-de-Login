
from tkinter import *

class Aplicativo:
    def __init__(self, master=None):
        janela.title("Login")
        janela.geometry("200x150")

        

        self.head = Frame(master)
        self.head["pady"] = 10
        self.head.pack()

        self.email = Frame(master)
        self.email["padx"] = 20
        self.email.pack()


        self.senha = Frame(master)
        self.senha["padx"] = 20
        self.senha.pack()


        self.logar = Frame(master)
        self.logar["pady"] = 10
        self.logar.pack()                        

        self.titulo = Label(self.head, text="Sistema de login ")
        self.titulo.pack()



        self.EmailLabel = Label(self.email, text="Email")
        self.EmailLabel.pack(side=LEFT)

        self.Email = Entry(self.email)
        self.Email.pack(side=RIGHT)


        self.SenhaLabel = Label(self.senha, text="Senha")
        self.SenhaLabel.pack(side=LEFT)

        

        self.Senha = Entry(self.senha, show="*")
        self.Senha.pack(side=RIGHT)

        self.Botao = Button(self.logar, text="Entrar", command=self.AutenticarLogin)
        self.Botao.pack()

        self.Mensagem = Label(self.logar, text="")
        self.Mensagem.pack()



    def AutenticarLogin(self):
        autenticarlogin = self.CriarUsuario()

        email = self.Email.get()
        senha = self.Senha.get()
        """
        if email == emailBancoDeDados and senha == senhaBancoDeDados:
            self.Mensagem["text"] = "Bem Vindo Lucas"
        else:
            self.Mensagem["text"] = "Login Incorreto"
        """
        with open("BancoDeDados.txt", "r", encoding="utf-8") as arquivo:
            usuario = arquivo.readlines()
            for linha in usuario:
                linha = linha.strip('\n')
                EmailBancoDeDados,SenhaBancoDeDados = linha.split(":")
                if EmailBancoDeDados == email and SenhaBancoDeDados == senha:
                    self.Mensagem["text"] = "Você esta logado!"
       
    def CriarUsuario(self):
        with open("BancoDeDados.txt", "r") as arquivo:
            arquivo.read()
        
    def ProcurarUsuario(self):
        pass


janela = Tk()
Aplicativo(janela)
janela.mainloop()