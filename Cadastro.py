from tkinter import *
from tkinter import messagebox

class Cadastro:
    def __init__(self, master=None):
        self.Tela()

        imgFundo = PhotoImage(file="Aserts\\Cadastro.png")
        labfundo = Label(janela, image=imgFundo)      
        labfundo.pack()

        self.Usuario = Entry(janela, background= "#d9d9d9")
        self.Usuario.place(x=55, y=144, height=36, width=270)

        self.Email = Entry(janela, background= "#d9d9d9" )
        self.Email.place(x=55, y=223, height=36, width=270)

        self.Senha = Entry(janela, show="*", background= "#d9d9d9")
        self.Senha.place(x=55, y=298, height=36, width=270)

        self.ConfirmarSenha = Entry(janela, show="*", background= "#d9d9d9")
        self.ConfirmarSenha.place(x=55, y=363, height=36, width=270)

        self.Botao = Button(janela, text="Cadastrar", command=self.CriarUsuario, background= "#d9d9d9")
        self.Botao.place(x=115, y=425, height=45, width=145)

        janela.mainloop()

    def Tela(self):
        janela.title("Cadastro")
        janela.geometry("380x514")
        janela.resizable(width=False, height=False)


    def CriarUsuario(self):
        usuario = self.Usuario.get()
        email = self.Email.get()
        senha = self.Senha.get()
        confirmarSenha = self.ConfirmarSenha.get()
        if senha == confirmarSenha and senha != "" and email != "":
            with open("BancoDeDados.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"\n{email}:{senha}")
                AlertaMsgCorreta = messagebox.showinfo("Conta", "Conta criada com sucesso!")
        else:
            AlertaMsgIncorreta = messagebox.showinfo("Senha", "Senha incorreta!")


janela = Tk()
Cadastro(janela)



"""

Alerta = Button(janela, text = "Logado", command = AlertaMsgCorreta)
Alerta.pack()

"""