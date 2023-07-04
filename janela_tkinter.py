import tkinter

#criando a janela
janela= tkinter.Tk()

#definindo tamanho da janela
janela.geometry("500x300")

#definindo uma ação para o botão executar 
def clique(): 
    print("Fazer login")

# escrevendo na janela 
texto = tkinter.Label(janela, text="Fazer Login")

#colocando texto na janela e passando a distancia dos itens 
texto.pack(padx=10, pady=10)

#criando campo para digitar email e senha
email = tkinter.Entry(janela, )
email.pack(padx=10, pady=10)
senha = tkinter.Entry(janela,  show="*")
senha.pack(padx=10, pady=10)

#colocando a janela de chackbox 
checkbox = tkinter.Checkbutton(janela, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)

#colocando um botão 
botao = tkinter.Button(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

#rodando a janela
janela.mainloop()