#firebase
#Documentação api firebase
#https://github.com/nhorvath/Pyrebase4
import pyrebase

from tkinter import *
import customtkinter

firebaseconfig={
'apiKey': "AIzaSyDBGgXz-pWCjtRHJqfzW74ENPFZ9VjAHE4",
'authDomain': "sysmercado.firebaseapp.com",
  #'projectId': "sysmercado",
"databaseURL": "https://databaseName.firebaseio.com",
'storageBucket': "sysmercado.appspot.com"
  #'messagingSenderId': "619957296807",
  #'appId': "1:619957296807:web:fc1c2276f97e77562e0582",
  #'measurementId': "G-K9SFZK26L7"
}

firebase = pyrebase.initialize_app(firebaseconfig)
auth=firebase.auth()

#Criar novo usuario
def signigUp(usuario,senha):
    #email=input("entre com seu email: ")
    #senha=input("entre com a sua senha: ")

    auth.create_user_with_email_and_password(usuario,senha)




customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')


def printLogin():
    #COMO PEGAR OS VALORES DO ENTRY
    print("Esse é o nome do usuario:",entryUser.get())
    print("Essa é a senha:", entrysenha.get())
    signigUp(entryUser.get(),entrysenha.get())

tela=customtkinter.CTk()
tela.geometry('580x400')#largura, altura
tela.title('Login')
tela.resizable(width=False,height=False)

tela.iconbitmap('icone.ico')
#corrigir tamanho da imagem
img=PhotoImage(file='financeiro_resized.png')


label_imagem=customtkinter.CTkLabel(master=tela,image=img)
label_imagem.place(x=15,y=25)

#Frame
frame=customtkinter.CTkFrame(master=tela,width=350,height=396)
frame.pack(side=RIGHT)

#Add widgets ao frame
#aumentar o tamanho dessa fonte
label=customtkinter.CTkLabel(master=frame,text='Cadastro')
label.place(x=25,y=5)

entryUser=customtkinter.CTkEntry(master=frame,placeholder_text='Nome do usuário',width=300)
entryUser.place(x=25,y=105)

label1=customtkinter.CTkLabel(master=frame,text='O campo é obrigatório',text_color='green')
label1.place(x=25,y=135)



entrysenha=customtkinter.CTkEntry(master=frame,placeholder_text='Senha',width=300,show='*')
entrysenha.place(x=25,y=175)




label2=customtkinter.CTkLabel(master=frame,text='O campo é obrigatório',text_color='green')
label2.place(x=25,y=205)


botao=customtkinter.CTkButton(master=frame,text='LOGIN',width=300,command=printLogin)
botao.place(x=25,y=285)






tela.mainloop()
