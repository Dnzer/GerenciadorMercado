import sqlite3


#class sistemaSupermercado:
class supermercadoDB:
    def __init__(self):
        self.conn = sqlite3.connect('supermercado.db')
        self.cursor = self.conn.cursor()
        self.criar_tabela_produtos()
        self.criar_tabela_clientes()
        self.criar_tabela_funcionarios()
        self.criar_tabela_vendas()
        self.criar_tabela_venda()

    def criar_tabela_produtos(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Produtos (
                ID_produto INTEGER PRIMARY KEY,
                Nome_produto TEXT NOT NULL,
                Descricao TEXT,
                Preco REAL NOT NULL,
                Quantidade_estoque INTEGER NOT NULL,
                Categoria TEXT,
                Custo REAL,
                Codigo_barras TEXT
            )
        ''')
        self.conn.commit()

    def criar_tabela_clientes(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clientes (
                ID_cliente INTEGER PRIMARY KEY,
                CPF TEXT UNIQUE NOT NULL,
                Nome_cliente TEXT NOT NULL,
                Endereco TEXT,
                Email TEXT,
                Numero_telefone TEXT
            )
        ''')
        self.conn.commit()

    def criar_tabela_funcionarios(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Funcionarios (
                ID_funcionario INTEGER PRIMARY KEY,
                Nome_funcionario TEXT NOT NULL,
                Senha_funcionario TEXT NOT NULL,
                Cargo TEXT,
                Data_admissao DATE,
                Salario REAL,
                CPF TEXT UNIQUE NOT NULL,
                Endereco TEXT,
                Data_nasc TEXT,
                Numero_telefone TEXT

            )
        ''')
        self.conn.commit()

    def criar_tabela_vendas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Vendas (
                ID_venda INTEGER PRIMARY KEY,
                Data_hora_venda TEXT NOT NULL,
                ID_funcionario INTEGER,
                Total_venda REAL NOT NULL,
                CPF_consumidor TEXT,
                Desconto_total REAL,
                Qtd_produtos_vendidos INTEGER,
                FOREIGN KEY (ID_funcionario) REFERENCES Funcionarios (ID_funcionario),
                FOREIGN KEY (CPF_consumidor) REFERENCES Clientes (CPF)
            
            )
        ''')
        self.conn.commit()

    def criar_tabela_venda(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Itens_de_Venda (
                ID_item_venda INTEGER PRIMARY KEY,
                ID_venda INTEGER,
                ID_produto INTEGER,
                Quantidade_vendida INTEGER,
                Preco_unitario REAL,
                FOREIGN KEY (ID_venda) REFERENCES Vendas (ID_venda),
                FOREIGN KEY (ID_produto) REFERENCES Produtos (ID_produto)
            )
        ''')
        self.conn.commit()
 
    #Atualiza tabelas
    def inserir_func(self, funcionario):
        self.cursor.execute('''
            INSERT INTO Funcionarios (ID_funcionario, Nome_funcionario, Cargo, Data_admissao, Salario, CPF, Endereco, Data_nasc, Numero_telefone)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (funcionario.id, funcionario.nome, funcionario.cargo, funcionario.dataAdmissao, funcionario.salario, funcionario.cpf, funcionario.endereco, funcionario.dataNasc, funcionario.telefone))
        self.conn.commit() 
    
    def inserir_produto(self, produto):
        self.cursor.execute('''
            INSERT INTO Produtos (ID_produto, Nome_produto, Descricao, Preco, Quantidade_estoque, Categoria, Custo, Codigo_barras)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (produto.idProduto, produto.nome, produto.descricao, produto.preco, produto.quantidade_estoque, produto.categoria, produto.custo, produto.codigo_barras))
        self.conn.commit()

    def inserir_cliente(self, cliente):
        self.cursor.execute('''
            INSERT INTO Clientes (ID_cliente, CPF, Nome_cliente, Endereco, Email, Numero_telefone)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (cliente.id, cliente.cpf, cliente.nome, cliente.endereco, cliente.eMail, cliente.telefone))
        self.conn.commit() 

    def fechar_conexao(self):
        self.conn.close()


if __name__ == "__main__":
    supermercado_db = supermercadoDB()
    
    supermercado_db.fechar_conexao()
