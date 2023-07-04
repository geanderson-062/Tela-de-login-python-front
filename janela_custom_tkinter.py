#importando a lib
import customtkinter

#alterando a tematica do sistema
customtkinter.set_appearance_mode ("dark")
customtkinter.set_default_color_theme("green") # outro thema dark-blue

#criando a janela
janela= customtkinter.CTk()

#definindo tamanho da janela
janela.geometry("500x300")

#definindo uma ação para o botão executar 
def clique(): 
    print("Fazer login")

# escrevendo na janela 
texto = customtkinter.CTkLabel(janela, text="Fazer Login")

#colocando texto na janela e passando a distancia dos itens 
texto.pack(padx=10, pady=10)

#criando campo para digitar email e senha
email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)
senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

#colocando a janela de chackbox 
checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)

#colocando um botão 
botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

#rodando a janela
janela.mainloop()