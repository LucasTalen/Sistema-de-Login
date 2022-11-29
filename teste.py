"""with open("email.txt", "r", encoding="utf-8") as arquivo:
    email = arquivo.readline()
    print(email)
    for linha in email:
        pass
"""
"""
# def Criar Conta
email = input("Digite seu email: ")
senha = input("Digite uma senha: ")
with open("BancoDeDados.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"\n{email}:{senha}")
"""
"""
frase = "lucas:123"
nome,senha = frase.split(":")
print(nome)
print(senha)
"""
"""
email = str(input("Digite seu email: "))
senha = str(input("Digite sua senha: "))
logado = False

with open("BancoDeDados.txt", "r", encoding="utf-8") as arquivo:
    usuario = arquivo.readlines()
    for linha in usuario:
        linha = linha.strip('\n')
        emailUsuario,senhaUsuario = linha.split(":")
        if emailUsuario.find(email) and senhaUsuario.find(senha):
            print("logado")
       """
from tkinter import *
def clique(retorno):
    print(retorno)
    print(janela.geometry())

janela = Tk()

janela.bind("<Button-1>", clique)

imgFundo = PhotoImage(file="Aserts\\Login.png")
labfundo = Label(janela, image=imgFundo)      
labfundo.pack()
    

janela.mainloop()  
