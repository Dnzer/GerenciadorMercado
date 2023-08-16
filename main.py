
import tkinter as tk
from tkinter import PhotoImage
from tkinter.constants import RIGHT, LEFT
import SuperMercado
import customtkinter

import bancoDados


def telaInicial():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')


    telaInicial=customtkinter.CTk()
    telaInicial.geometry('580x400')#largura, altura
    telaInicial.title('SYSmercado')
    #telaInicial.resizable(width=False,height=False)
    telaInicial.iconbitmap('icone.ico')

    img = PhotoImage(file='Logo_telainicio.png')
    label_imagem = tk.Label(master=telaInicial, image=img)
    label_imagem.place(x=120, y=60)

    botaoLogin=customtkinter.CTkButton(master=telaInicial,text='ENTRAR ',width=300,command=telaLogin)
    botaoLogin.place(x=135,y=285)
    telaInicial.mainloop()

def gerarRelatorio():
    tela =customtkinter.CTkToplevel
    tela = customtkinter.CTkToplevel()
    tela.geometry('580x400')  # largura, altura
    tela.title('cadastro funcionario')
    tela.resizable(width=False, height=False)

    tela.iconbitmap('icone.ico')
    # corrigir tamanho da imagem
    img = PhotoImage(file='financeiro_resized.png')

    label_imagem = customtkinter.CTkLabel(master=tela, image=img)
    label_imagem.place(x=15, y=25)

    # Frame
    frame = customtkinter.CTkFrame(master=tela, width=350, height=396)
    frame.pack(side=RIGHT)

    # Add widgets ao frame
    # aumentar o tamanho dessa fonte
    label = customtkinter.CTkLabel(master=frame, text='Cadastro', font=("Helvetica", 20))
    label.place(x=25, y=5)

    entryUser = customtkinter.CTkEntry(master=frame, placeholder_text='Nome do usuário', width=300)
    entryUser.place(x=25, y=105)

    label1 = customtkinter.CTkLabel(master=frame, text='O campo é obrigatório', text_color='green')
    label1.place(x=25, y=135)

    entrysenha = customtkinter.CTkEntry(master=frame, placeholder_text='Senha', width=300, show='*')
    entrysenha.place(x=25, y=175)

    label2 = customtkinter.CTkLabel(master=frame, text='O campo é obrigatório', text_color='green')
    label2.place(x=25, y=205)

    botao = customtkinter.CTkButton(master=frame, text='CADASTRAR', width=300)
    botao.place(x=25, y=285)
    tela.mainloop()



def cadastrarProd(idProduto, nome, descricao, preco, quantidade_estoque, categoria, custo, codigo_barras):
    print("Função cadastrar Produto!!!")
    print("Esse é o ID do produto",idProduto)
    print("Esse é o nome do produto", nome)
    print("Esse é a descrição do produto", descricao)
    print("Esse é o preco do produto", preco)
    print("Esse é a qt_estoque do produto", quantidade_estoque)
    print("Esse é a categoria do produto", categoria)
    print("Esse é o custo do produto", custo)
    print("Esse é o código de barras- do produto", codigo_barras)

    #lista_compras = ['banana', 'laranja', 'maçã']

    SuperMercado.Produto.se


    bancoDados.supermercadoDB.inserir_produto()

def cadastrarFunc(nome,cargo,admissao,salario,CPF,endereco,data_nasc,tel):
    print("Nome do usuario:",nome)
    print("Cargo:",cargo)
    print("admissão",admissao)
    print("Salario",salario)
    print("CPF: ",CPF)
    print("endereço: ",endereco)
    print("data_nasc",data_nasc)
    print("Telefone",tel)




def telaCriaUser():
    tela = customtkinter.CTkToplevel()
    tela.geometry('580x400')  # largura, altura
    tela.title('cadastro funcionario')
    tela.resizable(width=False, height=False)

    tela.iconbitmap('icone.ico')
    # corrigir tamanho da imagem
    img = PhotoImage(file='financeiro_resized.png')

    label_imagem = customtkinter.CTkLabel(master=tela, image=img)
    label_imagem.place(x=15, y=25)

    # Frame
    frame = customtkinter.CTkFrame(master=tela, width=350, height=396)
    frame.pack(side=RIGHT)

    # Add widgets ao frame
    # aumentar o tamanho dessa fonte
    label = customtkinter.CTkLabel(master=frame, text='Cadastro', font=("Helvetica", 20))
    label.place(x=25, y=5)

    nome = customtkinter.CTkEntry(master=frame, placeholder_text='Nome do funcinario', width=300)
    nome.place(x=25, y=50)

    cargo = customtkinter.CTkEntry(master=frame, placeholder_text='Cargo', width=300)
    cargo.place(x=25, y=80)

    admissao = customtkinter.CTkEntry(master=frame, placeholder_text='Data de admissão', width=300)
    admissao.place(x=25,y=110)

    salario  = customtkinter.CTkEntry(master=frame, placeholder_text='Salário', width=300)
    salario.place(x=25,y=140)

    CPF = customtkinter.CTkEntry(master=frame, placeholder_text='CPF', width=300)
    CPF.place(x =25,y=170)

    endereco = customtkinter.CTkEntry(master=frame, placeholder_text='Endereço', width=300)
    endereco.place(x=25,y=200)

    data_nasc = customtkinter.CTkEntry(master=frame, placeholder_text='Data de nascimento', width=300)
    data_nasc.place(x=25,y=230)

    tel = customtkinter.CTkEntry(master=frame, placeholder_text='Telefone', width=300)
    tel.place(x=25,y=260)

    botao = customtkinter.CTkButton(master=frame, text='CADASTRAR', width=300,command= lambda :cadastrarFunc(nome.get(),
                                                                                                    cargo.get(),
                                                                                                    admissao.get(),
                                                                                                    salario.get(),
                                                                                                    CPF.get(),
                                                                                                    endereco.get(),
                                                                                                    data_nasc.get(),
                                                                                                    tel.get()
                                                                                                     )
                                    )
    botao.place(x=25, y=295)
    tela.mainloop()

def telaCadastrarProd():
    tela = customtkinter.CTkToplevel()
    tela.geometry('580x400')  # largura, altura
    tela.title('Cadastro de produto ')
    tela.resizable(width=False, height=True)
    tela.iconbitmap('icone.ico')


    ID = customtkinter.CTkEntry(master=tela, placeholder_text='ID',width=300)
    ID.place(x=140, y=10)

    nome = customtkinter.CTkEntry(master=tela, placeholder_text='Nome do produto', width=300)
    nome.place(x=140, y=50)

    des = customtkinter.CTkEntry(master=tela, placeholder_text='Descrição do produto', width=300)
    des.place(x=140, y=90)

    preco = customtkinter.CTkEntry(master=tela, placeholder_text='Preço', width=300)
    preco.place(x=140, y=130)

    quantidade_estoque = customtkinter.CTkEntry(master=tela, placeholder_text='Quantidade em estoque', width=300)
    quantidade_estoque.place(x=140, y=170)

    categoria = customtkinter.CTkEntry(master=tela, placeholder_text='Categoria do produto', width=300)
    categoria.place(x=140, y=210)

    custo = customtkinter.CTkEntry(master=tela, placeholder_text='Custo', width=300)
    custo.place(x=140, y=250)

    cod_barra = customtkinter.CTkEntry(master=tela, placeholder_text='Código de barras', width=300)
    cod_barra.place(x=140, y=290)








    botao = customtkinter.CTkButton(master=tela, text='Cadastrar Produto', width=15,
                                    command=lambda: cadastrarProd(ID.get(),
                                                                  nome.get(),
                                                                  des.get(),
                                                                  preco.get(),
                                                                  quantidade_estoque.get(),
                                                                  categoria.get(),
                                                                  custo.get(),
                                                                  cod_barra.get())
                                    )
    botao.place(x=220, y=330)

    tela.mainloop()



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

    botao1 = customtkinter.CTkButton(master=frame, text='Relatório', width=150,command=gerarRelatorio)
    botao1.place(x=5, y=70)

    botao2 = customtkinter.CTkButton(master=frame, text='CadastrarProduto', width=150,command=telaCadastrarProd)
    botao2.place(x=5, y=100)

    botao3 = customtkinter.CTkButton(master=frame, text='CadastrarFuncionario', width=150,command=telaCriaUser)
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


def opcaoPagamento(escolha):

    if escolha == 'dinheiro':
        print("Escolheu dinheiro")
    if escolha =='cartão':
        print("Escolheuc cartão")
    if escolha =='pix':
        print("Escolheu pix")


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

    listPagamento=['Dinheiro','Cartão de credito',"pix"]
    pag = customtkinter.CTkOptionMenu(master = frame,values=listPagamento)
    pag.place(x=10,y=100)


    label2 = customtkinter.CTkLabel(master=frame,text='TOTAL:')
    label2.place(x=10, y=140)

    labelTroco = customtkinter.CTkLabel(master=frame, text='TROCO: R$')
    labelTroco.place(x=10, y=170)


    botao2 = customtkinter.CTkButton(master=frame, text='FINALIZAR', width=150, command= lambda op = str(pag.get()) :opcaoPagamento(op))
    botao2.place(x=5, y=200)

    # FrameTELA
    frametela = customtkinter.CTkFrame(master=tela, width=410, height=396,bg_color='white')
    frametela.pack(side=LEFT)

    # Add widgets ao frame
    # aumentar o tamanho dessa fonte
    label1 = customtkinter.CTkLabel(master=frame, text='Usuário:')
    label1.place(x=10, y=10)

    tela.mainloop()


def telaLogin():
    tela=customtkinter.CTk()
    tela.geometry('580x400')#largura, altura
    tela.title('Login')
    tela.resizable(width=False,height=False)

    tela.iconbitmap('icone.ico')
    #corrigir tamanho da imagem
    #img=PhotoImage(file='financeiro_resized.png')

    #label_imagem=customtkinter.CTkLabel(master=tela,image=img)
    #label_imagem.place(x=15,y=25)

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

    botao=customtkinter.CTkButton(master=frame,text='LOGIN',width=300,command= lambda  :SuperMercado.Funcionario.login(entryUser.get(),entrysenha.get()))
    botao.place(x=25,y=285)
    tela.mainloop()



#telaCriaUser()
#telaLogin()
#telaInicial()
telaGerente()
#telaCadastrarProd()
#telaCompras()
