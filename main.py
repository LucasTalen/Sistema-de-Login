from tkinter import *
from tkinter import messagebox
class Login:
    def __init__(self, master=None):
        self.Tela()

        imgFundo = PhotoImage(file="Aserts\\Login.png")
        labfundo = Label(janela, image=imgFundo)      
        labfundo.pack()
    
        self.Email = Entry(janela, background= "#d9d9d9")
        self.Email.place(x=50, y=240, height=35, width=280)
        
        self.Senha = Entry(janela, show="*", background= "#d9d9d9")
        self.Senha.place(x=50, y=322, height=35, width=280)

        self.Botao = Button(janela, command=self.AutenticarLogin, background= "#d9d9d9")
        self.Botao.place(x=115, y=405, height=45, width=145)

        janela.mainloop()    
        
    def Tela(self):
        janela.title("Login")
        janela.geometry("380x514")
        janela.resizable(width=False, height=False)
        
    def AutenticarLogin(self):
        email = self.Email.get()
        senha = self.Senha.get()
        SenhaIncorreta = True
        with open("BancoDeDados.txt", "r", encoding="utf-8") as arquivo:
            usuario = arquivo.readlines()

            for linha in usuario:
                linha = linha.strip('\n')
                EmailBancoDeDados,SenhaBancoDeDados = linha.split(":")

                if EmailBancoDeDados == email and SenhaBancoDeDados == senha:
                    AlertaMsgCorreta = messagebox.showinfo("Logado", "Logado com Sucesso!")
                    Alerta = Button(janela, text = "Logado", command = AlertaMsgCorreta)
                    Alerta.pack()
                    SenhaIncorreta = False
                    break

            if SenhaIncorreta == True:
                AlertaMsgIncorreta = messagebox.showinfo("Erro", "Email ou Senha incorreto!")
                Alerta = Button(janela, text = "Erro", command = AlertaMsgIncorreta)
                Alerta.pack()

janela = Tk()
Login(janela)