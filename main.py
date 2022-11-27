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
        nome = self.Email.get()
        senha = self.Senha.get()
        if nome == "Lucas" and senha == "Lucas58227":
            self.Mensagem["text"] = "Bem Vindo Lucas"
        else:
            self.Mensagem["text"] = "Login Incorreto"



janela = Tk()
Aplicativo(janela)
janela.mainloop()