#firebase
#Documentação api firebase
#https://github.com/nhorvath/Pyrebase4
import pyrebase

from tkinter import *
import customtkinter

#Definindo estilo padrão das telas
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

#configurando a conexão com o firebase
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

def telaInicial():
    telaInicial=customtkinter.CTk()
    telaInicial.geometry('580x400')#largura, altura
    telaInicial.title('SYSmercado')
    #telaInicial.resizable(width=False,height=False)

    telaInicial.iconbitmap('icone.ico')
    botaoLogin=customtkinter.CTkButton(master=telaInicial,text='ENTRAR ',width=300)
    botaoLogin.place(x=135,y=285)
    telaInicial.mainloop()
def telaGerente():
    tela = customtkinter.CTk()
    tela.geometry('580x400')  # largura, altura
    tela.title('SYSmercado')
    tela.resizable(width=False,height=True)
    tela.iconbitmap('icone.ico')


    # FrameMENU
    frame = customtkinter.CTkFrame(master=tela, width=165, height=396)
    frame.pack(side=LEFT)

    # Add widgets ao frame
    # aumentar o tamanho dessa fonte
    label1= customtkinter.CTkLabel(master=frame, text='Usuário:')
    label1.place(x=10, y=10)
    label2 = customtkinter.CTkLabel(master=frame, text='Cargo:')
    label2.place(x=10, y=40)



    botao1 = customtkinter.CTkButton(master=frame, text='Relatório', width=150)
    botao1.place(x=5, y=70)

    botao2 = customtkinter.CTkButton(master=frame, text='CadastrarProduto', width=150)
    botao2.place(x=5, y=100)

    botao3 = customtkinter.CTkButton(master=frame, text='CadastrarFuncionario', width=150)
    botao3.place(x=5, y=130)

    # FrameTELA
    frametela = customtkinter.CTkFrame(master=tela, width=410, height=396,bg_color='white')
    frametela.pack(side=RIGHT)

    # Add widgets ao frame
    # aumentar o tamanho dessa fonte
    label1 = customtkinter.CTkLabel(master=frame, text='Usuário:')
    label1.place(x=10, y=10)
    label2 = customtkinter.CTkLabel(master=frame, text='Cargo:')
    label2.place(x=10, y=40)










    tela.mainloop()



def telaCompras():
    tela = customtkinter.CTk()
    tela.geometry('580x400')  # largura, altura
    tela.title('SYSmercado')
    tela.resizable(width=False,height=True)
    tela.iconbitmap('icone.ico')


    # FrameMENU
    frame = customtkinter.CTkFrame(master=tela, width=165, height=396)
    frame.pack(side=RIGHT)

    # Add widgets ao frame
    # aumentar o tamanho dessa fonte
    label1= customtkinter.CTkLabel(master=frame, text='Usuário:')
    label1.place(x=10, y=10)


    labelpagamento = customtkinter.CTkLabel(master=frame, text='SELECIONE MEIO DE PAGAMENTO')
    labelpagamento.place(x=10, y=70)
    botao1 = customtkinter.CTkButton(master=frame, text=' ', width=150)
    botao1.place(x=5, y=100)

    label2 = customtkinter.CTkLabel(master=frame, text='TOTAL:')
    label2.place(x=10, y=140)

    labelTroco = customtkinter.CTkLabel(master=frame, text='TROCO: R$')
    labelTroco.place(x=10, y=170)

    botao2 = customtkinter.CTkButton(master=frame, text='FINALIZAR', width=150)
    botao2.place(x=5, y=200)



    # FrameTELA
    frametela = customtkinter.CTkFrame(master=tela, width=410, height=396,bg_color='white')
    frametela.pack(side=LEFT)

    # Add widgets ao frame
    # aumentar o tamanho dessa fonte
    label1 = customtkinter.CTkLabel(master=frame, text='Usuário:')
    label1.place(x=10, y=10)











    tela.mainloop()














def login(email,senha):
    try:
        login=auth.sign_in_with_email_and_password(email,senha)
        print("SuccessFully loggend in !")
    except:
        print("ERRO: verifique o email e a senha")

def telaLogin():
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
    label=customtkinter.CTkLabel(master=frame,text='LOGIN',font=("Helvetica",20))
    label.place(x=25,y=5)

    entryUser=customtkinter.CTkEntry(master=frame,placeholder_text='Nome do usuário',width=300)
    entryUser.place(x=25,y=105)

    label1=customtkinter.CTkLabel(master=frame,text='O campo é obrigatório',text_color='green')
    label1.place(x=25,y=135)

    #Não está capturando o valor digitado
    entrysenha=customtkinter.CTkEntry(master=frame,placeholder_text='Senha',width=300,show='*')
    entrysenha.place(x=25,y=175)

    label2=customtkinter.CTkLabel(master=frame,text='O campo é obrigatório',text_color='green')
    label2.place(x=25,y=205)

    #email=entryUser.get()
    #senha=int(entrysenha.get())

    botao=customtkinter.CTkButton(master=frame,text='LOGIN',width=300,command= lambda  :login(entryUser.get(),entrysenha.get()))
    botao.place(x=25,y=285)
    tela.mainloop()





def signUp(email,senha):
    auth.create_user_with_email_and_password(email,senha)

def telaCriaUser():
    tela=customtkinter.CTk()
    tela.geometry('580x400')#largura, altura
    tela.title('cadastro funcionario')
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
    label=customtkinter.CTkLabel(master=frame,text='Cadastro',font=("Helvetica",20))
    label.place(x=25,y=5)

    entryUser=customtkinter.CTkEntry(master=frame,placeholder_text='Nome do usuário',width=300)
    entryUser.place(x=25,y=105)

    label1=customtkinter.CTkLabel(master=frame,text='O campo é obrigatório',text_color='green')
    label1.place(x=25,y=135)



    entrysenha=customtkinter.CTkEntry(master=frame,placeholder_text='Senha',width=300,show='*')
    entrysenha.place(x=25,y=175)

    label2=customtkinter.CTkLabel(master=frame,text='O campo é obrigatório',text_color='green')
    label2.place(x=25,y=205)


    botao=customtkinter.CTkButton(master=frame,text='CADASTRAR',width=300,command= lambda :signUp(entryUser.get(),entrysenha.get()))
    botao.place(x=25,y=285)
    tela.mainloop()

#telaCriaUser()
#telaLogin()
#telaInicial()
#telaGerente()


telaCompras()


tela.mainloop()
