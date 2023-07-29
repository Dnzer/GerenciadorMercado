from tkinter import *
import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

user=None
password=None
def printLogin():
    print("Esse é o nome do usuario",user)
    print("Essa é a senha ", password)

tela=customtkinter.CTk()
tela.geometry('580x400')#largura, altura
tela.title('Login')
tela.resizable(width=False,height=False)

tela.iconbitmap('icone.ico')

img=PhotoImage(file='financeiro_resized.png')#corrigir tamanho da imagem

label_imagem=customtkinter.CTkLabel(master=tela,image=img)
label_imagem.place(x=5,y=5)

#Frame
frame=customtkinter.CTkFrame(master=tela,width=350,height=396)
frame.pack(side=RIGHT)

#Add widgets ao frame

label=customtkinter.CTkLabel(master=frame,text='Sistema de login')
label.place(x=25,y=5)

entryUser=customtkinter.CTkEntry(master=frame,placeholder_text='Nome do usuário',width=300,textvariable=user)
entryUser.place(x=25,y=105)

label1=customtkinter.CTkLabel(master=frame,text='O campo é obrigatório',text_color='green')
label1.place(x=25,y=135)


#Não está capturando o valor digitado
entrysenha=customtkinter.CTkEntry(master=frame,placeholder_text='Senha',width=300,textvariable=password)
entrysenha.place(x=25,y=175)

label2=customtkinter.CTkLabel(master=frame,text='O campo é obrigatório',text_color='green')
label2.place(x=25,y=205)


botao=customtkinter.CTkButton(master=frame,text='LOGIN',width=300,command=printLogin)
botao.place(x=25,y=285)






tela.mainloop()