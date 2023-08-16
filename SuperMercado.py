import os
import datetime
from typing import TypeVar, List, Tuple
import bancoDados
import sqlite3

T = TypeVar('T')

try:
    conn = sqlite3.connect('BaseBancoDados.db')
    cursor = conn.cursor()
except sqlite3.Error as e:
    print(f"Error connecting to the database: {e}")
    exit(0)


class Produto:
    def __init__(self, idProduto, nome, descricao, preco, quantidade_estoque, categoria, custo, codigo_barras):
        self.__idProduto = idProduto
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque
        self.__categoria = categoria
        self.__custo = custo
        self.__codigo_barras = codigo_barras

    def calcular_total(self, quantidade: int) -> float:
        return self.__preco * quantidade

    # Métodos Getter
    def get_idProduto(self) -> int:
        return self.__idProduto

    def get_nome(self) -> str:
        return self.__nome

    def get_descricao(self) -> str:
        return self.__descricao

    def get_preco(self) -> float:
        return self.__preco
    def get_quantidade_estoque(self) -> int:
        return self.__quantidade_estoque

    # Métodos Setter
    def set_nome(self, nome: float):
        self.__nome = nome

    def set_descricao(self,des):
        self.__descricao = des

    def set_preco(self, novo_preco: float):
        self.__preco = novo_preco
    
    def set_quantidade_estoque(self, novo_quantidade_estoque: int) -> int:
        self.__quantidade_estoque = novo_quantidade_estoque

    def set_categoria(self,categoria):
        self.__categoria = categoria

    def set_custo(self,custo):
        self.__custo = custo

    def set_codigoBarras(self,codBarras):
        self.__codigo_barras = codBarras

class Pessoa:
    def __init__(self, nome, cpf, endereco, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__telefone = telefone

    def get_nome(self) -> str:
        return self.__nome

    def get_cpf(self) -> str:
        return self.__cpf

    def get_endereco(self) -> str:
        return self.__endereco

    def get_telefone(self) -> str:
        return self.__telefone

    # Métodos Setter
    def set_nome(self, novo_nome: str):
        self.__nome = novo_nome

    def set_cpf(self, novo_cpf: str):
        self.__cpf = novo_cpf

    def set_endereco(self, novo_endereco: str):
        self.__endereco = novo_endereco

    def set_telefone(self, novo_telefone: str):
        self.__telefone = novo_telefone

class Cliente(Pessoa):
    def __init__(self, nome, cpf, endereco, telefone, eMail):
        super().__init__(nome, cpf, endereco, telefone)
        self.__eMail = eMail

    # Métodos Getter
    def get_eMail(self) -> str:
        return self.__eMail

    # Métodos Setter
    def set_eMail(self, novo_eMail: str):
        self.__eMail = novo_eMail

class Funcionario(Pessoa):
    def __init__(self, id, nome, senha, cargo, dataAdmissao, salario, cpf, dataNasc, telefone, endereco):
        super().__init__(nome, cpf, endereco, telefone)
        self.__id=id
        self.__senha=senha
        self.__cargo = cargo
        self.__dataAdmissao = dataAdmissao
        self.__salario = salario
        self.__dataNasc = dataNasc

    def login(nome, senha):
        try:
            cursor.execute('SELECT * FROM Funcionarios WHERE Nome_funcionario = ? AND Senha = ?', (nome, senha))
            user = cursor.fetchone()
            if user:
                return True  # Returns the user ID if the login is successful
            else:
                return None  # Returns None if the login fails
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")
            return None


        
    # Métodos Getter
    def get_id(self):
        return self.__id

    def get_cargo(self) -> str:
        return self.__cargo

    def get_dataAdmissao(self) -> str:
        return self.__dataAdmissao

    def get_salario(self) -> float:
        return self.__salario

    def get_dataNasc(self) -> str:
        return self.__dataNasc

    # Métodos Setter
    def set_cargo(self, novo_cargo: str):
        self.__cargo = novo_cargo

    def set_dataAdmissao(self, nova_dataAdmissao: str):
        self.__dataAdmissao = nova_dataAdmissao

    def set_salario(self, novo_salario: float):
        self.__salario = novo_salario

    def set_dataNasc(self, nova_dataNasc: str):
        self.__dataNasc = nova_dataNasc

class Vendas:
    def __init__(self, total_venda, cliente="?"):
        self.__data_hora = self.obter_data_hora_formatada()  # Call the method here
        self.__id_funcionario=funcionario_logado.get_id()
        self.__total_venda=total_venda
        self.__cliente = self.busca_cpf(cliente)  # The error is here
        self.__quant_produtos=self.cont_produtos()

    def obter_data_hora_formatada(self):
        data_hora_atual = datetime.datetime.now()
        data_hora_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M")
        return data_hora_formatada

    def busca_cpf(self, cliente):
        if cliente == "?":
            return "?"
        else:
            return cliente.get_cpf()

    def cont_produtos(self):
        return len(caixa.get_produtos())
class Venda:
    def __init__(self, cliente="?"):
        self.__cliente = cliente
        self.__itens = []  # Lista de tuplas (produto, quantidade)

    def adicionar_item(self, produto: Produto, quantidade: int):
        self.__itens.append((produto, quantidade))

    def calcular_total_venda(self) -> float:
        total_venda = 0.0
        for produto, quantidade in self.__itens:
            total_venda += produto.calcular_total(quantidade)
        return total_venda

    def finalizar_venda(self):
        total_venda = self.calcular_total_venda()
        self.__caixa.adicionar_venda(self, total_venda)
        self.__caixa.baixar_estoque()

        print(f"Venda finalizada para o cliente {self.__cliente.get_nome()}. Total: R$ {total_venda:.2f}")

class CaixaSupermercado:
    def __init__(self):
        self.__produtos: List[Tuple[T, int]] = []  
        self.__vendas = []


    def get_produtos(self) -> List[Tuple[T, int]]:
        return self.__produtos
    def adicionar_produto(self, produto_id: int, quantidade: int = 1):
        try:    
            cursor.execute('SELECT * FROM Produtos WHERE ID_produto = ?', (produto_id,))
            produto_data = cursor.fetchone()

            if produto_data:
                idProduto, nome, descricao, preco, quantidade_estoque, categoria, custo, codigo_barras = produto_data

                if quantidade_estoque >= quantidade:
                    produto = Produto(idProduto, nome, descricao, preco, quantidade_estoque, categoria, custo, codigo_barras)
                    self.__produtos.append((produto, quantidade))
                    print(f"Produto '{nome}' adicionado ao caixa.")

                    # Update the stock in the products list (not in the database)
                    new_stock = quantidade_estoque - quantidade
                    produto.set_quantidade_estoque(new_stock)
                else:
                    print(f"Estoque insuficiente para o produto '{nome}'.")
            else:
                print(f"Produto com ID {produto_id} não encontrado na base de dados.")
            total_compra=self.calcular_total_compra()
            print(total_compra)
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")

            
    def calcular_total_compra(self) -> float:
        total_compra = 0.0
        for item, quant in self.__produtos:
            total_compra += item.get_preco() * quant
        return total_compra
    
    def finalizar_venda(self):
        for produto, quantidade in self.__produtos:
            produto_id = produto.get_idProduto()
            try:
                cursor.execute('SELECT Quantidade_estoque FROM Produtos WHERE ID_produto = ?', (produto_id,))
                current_stock = cursor.fetchone()[0]

                new_stock = current_stock - quantidade
                cursor.execute('UPDATE Produtos SET Quantidade_estoque = ? WHERE ID_produto = ?', (new_stock, produto_id))
                conn.commit()
            except sqlite3.Error as e:
                print(f"Error connecting to the database: {e}")

        cadastro_cliente=Cliente("ZÉ", "45635715966", "Av. C", "6666666666", "lucas@example.com")
        vendas=Vendas(self.calcular_total_compra(), cadastro_cliente)
        self.__produtos = []  # Clear the list of products after finalizing the sale

  
    def adicionar_venda(self, venda: Venda):
        self.__vendas.append(venda)


class EmployeeNotFoundError(Exception):
    pass

if __name__ == "__main__":
    supermercado_db=bancoDados.SupermercadoDB()
        ##funcionarios.extend([funcionario1, funcionario2])

    try:
        # Create a Funcionario instance and attempt to log in
        logado = Funcionario.login("Luisa Costa", "SenhaLuisa")
        if logado is None:
            raise EmployeeNotFoundError

        # Retrieve employee information from the database
        cursor.execute('SELECT * FROM Funcionarios WHERE Nome_funcionario = ?', ("Luisa Costa",))
        employee_data = cursor.fetchone()

        if employee_data:
            # Create a Funcionario object using retrieved data
            id, nome, senha, cargo, dataAdmissao, salario, cpf, dataNasc, telefone, endereco = employee_data
            funcionario_logado = Funcionario(id, nome, senha, cargo, dataAdmissao, salario, cpf, dataNasc, telefone, endereco)
        else:
            raise EmployeeNotFoundError

    except EmployeeNotFoundError:
        print("Funcionário não encontrado. Certifique-se de que o código está correto.")

    while logado:
        cursor.execute('SELECT * FROM Produtos')
        for row in cursor.fetchall():
            print(row)
        
        caixa = CaixaSupermercado()

        try:
            caixa.adicionar_produto(6, )
            caixa.adicionar_produto(2, 8)
            caixa.adicionar_produto(6, 4)

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

        # Finalize the sale
        caixa.finalizar_venda()
        
        os.system('PAUSE')