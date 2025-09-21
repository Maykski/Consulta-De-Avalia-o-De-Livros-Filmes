from trabalhopython.meubanco import Base
from sqlalchemy import Column, String, Integer
from datetime import datetime

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    data_de_nascimento = Column(String)
    genero = Column(String)
    cpf = Column(String)
    email = Column(String)

    def calcular_idade(self):
        try:
            data_nascimento = datetime.strptime(self.data_de_nascimento, "%d/%m/%Y")
            hoje = datetime.now()
            idade = hoje.year - data_nascimento.year
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