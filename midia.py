from sqlalchemy import Column, String, Integer, Boolean
from trabalhopython.meubanco import Base

class Midia(Base):
    __tablename__ = 'midias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    genero = Column(String)
    sinopse = Column(String)
    autor = Column(String)
    idade_classificada = Column(Integer)
    nota_final = Column(Integer)
    critica = Column(String)
    favorito = Column(Boolean, default=False)

    def __init__(self, titulo, genero, sinopse, autor, idade_classificada, nota_final, critica, favorito=False):
        self.titulo = titulo.strip()
        self.genero = genero.strip()
        self.sinopse = sinopse.strip()
        self.autor = autor.strip()
        self.idade_classificada = idade_classificada
        self.nota_final = nota_final
        self.critica = critica.strip()
        self.favorito = favorito

    def exibir_detalhes(self):
        print(f"\nTítulo: {self.titulo}")
        print(f"Gênero: {self.genero}")
        print(f"Sinopse: {self.sinopse}")
        print(f"Autor/Estúdio: {self.autor}")
        print(f"Classificação: {self.idade_classificada}")
        print(f"Nota: {self.nota_final} estrelas")
        print(f"Crítica: {self.critica}")
        print(f"Favorito: {'Sim' if self.favorito else 'Não'}")

class Livro(Midia):
    pass

class Filme(Midia):
    pass