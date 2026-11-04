#sempre que for migracao: alembic revision --autogenerate -m "mensagem da migracao"
# executar a migracao: alembic upgrade head
# sempre que fizer edicao no banco de dados, rodar o comando acima para atualizar o banco de dados

from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey  #resposavel pro criar conexao com o banco de dados
from sqlalchemy.orm import declarative_base #base para criar tabelas
#from sqlalchemy_utils.types import ChoiceType #para criar campos de escolha no banco de dados




db = create_engine("sqlite:///banco.db") #estabelece a conexao com o banco de dados
Base = declarative_base() #cria a classe base para criar as tabelas do banco de dados

#criar as classe/tabelas do banco de dados
class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    admin = Column("admin", Boolean, default=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)


    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

#Pedido
class Pedido(Base):
    __tablename__ = "pedidos"

    #STATUS_PEDIDOS = (
        #(chave, valor) - chave é o que vai ser armazenado no banco de dados e o valor é o que vai ser exibido para o usuário
        #("PENDENTE", "PENDENTE"),
        #("CANCELADO", "CANCELADO"),
        #("FINALIZADO", "FINALIZADO")
    #)

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) #pendente, cancelado, finalizado
    usuario = Column("usuario", ForeignKey("usuarios.id")) #chave estrangeira para a tabela de usuarios
    preco = Column("preco", Float)
    #itens =

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco

#ItensPedido
class ItemPedido(Base):
    __tablename__ = "itens_pedido"

   

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho",String) #P, M, G
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

#executa a criação dos metadados do banco de dados(criar o real banco de dados)






