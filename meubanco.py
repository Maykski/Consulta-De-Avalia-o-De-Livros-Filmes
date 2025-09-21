from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuração do banco de dados
db = create_engine("sqlite:///meubanco.db")  
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

from datetime import datetime

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    data_de_nascimento = Column(String)
    genero = Column(String)
    cpf = Column(String)
    email = Column(String)

    def __init__(self, nome, data_de_nascimento, genero, cpf, email):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.genero = genero
        self.cpf = cpf
        self.email = email

    def calcular_idade(self):
        try:
            # Converte a data de nascimento para um objeto datetime
            data_nascimento = datetime.strptime(self.data_de_nascimento, "%d/%m/%Y")
            hoje = datetime.now()
            idade = hoje.year - data_nascimento.year

            # Ajusta a idade se o aniversário ainda não ocorreu neste ano
            if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
                idade -= 1

            return idade
        except ValueError:
            print("Erro: Data de nascimento inválida.")
            return None

    def dados_clientes(self):
        print(f"\nID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.data_de_nascimento}")
        print(f"Gênero: {self.genero}")
        print(f"CPF: {self.cpf}")
        print(f"E-mail: {self.email}")

Base.metadata.create_all(bind=db)

# CRUD

cliente = Cliente(nome= "Marlo", data_de_nascimento= "01/05/2003", genero= "Masculino",cpf= "041 416 200 15", email= "marlon.gg14@gmail.com")
session.add(cliente)
session.commit()
cliente = Cliente(nome= "Michael", data_de_nascimento= "10/09/2013", genero= "Masculino",cpf= "040 486 230 18", email= "michael.g15@gmail.com")
session.add(cliente)
session.commit()
cliente = Cliente(nome= "Maria", data_de_nascimento= "04/12/2012", genero= "feminino",cpf= "040 466 200 12", email= "maria.g11@gmail.com")
session.add(cliente)
session.commit()
cliente = Cliente(nome= "Ana", data_de_nascimento= "20/010/2006", genero= "feminino",cpf= "039 416 230 41", email= "ana.g1@gmail.com")
session.add(cliente)
session.commit()
cliente = Cliente(nome= "Paula", data_de_nascimento= "29/07/2011", genero= "feminino",cpf= "040 446 240 40", email= "paula.gg12@gmail.com")
session.add(cliente)
session.commit()
cliente = Cliente(nome= "João", data_de_nascimento= "31/09/2001", genero= "Masculino",cpf= "040 456 230 10", email= "joao.g1@gmail.com")
session.add(cliente)
session.commit()
cliente = Cliente(nome= "Jorge", data_de_nascimento= "08/09/2000", genero= "Masculino",cpf= "040 436 240 02", email= "jorge.gg122@gmail.com")
session.add(cliente)
session.commit()
cliente = Cliente(nome= "Márcia", data_de_nascimento= "15/03/2003", genero= "feminino",cpf= "028 456 230 00", email= "marcia.g100@gmail.com")
session.add(cliente)
session.commit()
cliente = Cliente(nome= "Salete", data_de_nascimento= "12/02/2007", genero= "feminino",cpf= "041 476 240 05", email= "salete.gg133@gmail.com")
session.add(cliente)
session.commit()
cliente = Cliente(nome= "Eduardo", data_de_nascimento= "19/08/2002", genero= "Masculino",cpf= "042 496 230 41", email= "eduardo.g132@gmail.com")
session.add(cliente)
session.commit()