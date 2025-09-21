from datetime import datetime
import time
from trabalhopython.meubanco import db, session
from cliente import Cliente, cadastrar_cliente  # Importa a classe e a função do módulo cliente
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import declarative_base
from trabalhopython.midia import Livro, Filme
from trabalhopython.favoritos import adicionar_aos_favoritos, listar_favoritos  # Importa as funções de favoritos
from trabalhopython.menu import exibir_menu

Base = declarative_base()

#

# Listas globais
avaliacoes = [
    Livro("O Senhor dos Anéis", "Fantasia", "Um hobbit embarca em uma jornada para destruir um anel maligno.", "J.R.R. Tolkien", 12, 5, "Obra-prima da literatura fantástica!", False),
    Livro("1984", "Distopia", "Um mundo totalitário onde o governo controla tudo.", "George Orwell", 16, 5, "Assustadoramente atual.", False),
    Livro("Dom Casmurro", "Romance", "A possível traição de Capitu contada por Bentinho.", "Machado de Assis", 12, 4, "Clássico da literatura brasileira.", False),
    Livro("Harry Potter e a Pedra Filosofal", "Fantasia", "O jovem bruxo Harry Potter começa sua jornada na Escola de Magia e Bruxaria de Hogwarts.", "J.K. Rowling", 12, 3, "Uma das histórias mais adoradas do mundo, cheia de magia e aventuras!", False),
    Livro("O Hobbit", "Fantasia", "A jornada de Bilbo Bolseiro para recuperar um tesouro roubado do dragão Smaug.", "J.R.R. Tolkien", 10, 4, "Uma obra-prima da literatura fantástica que encanta todas as idades.", False),
    Livro("O Grande Gatsby", "Romance", "A decadência da sociedade americana através da vida de Jay Gatsby e seu amor não correspondido por Daisy.", "F. Scott Fitzgerald", 16, 5, "Um retrato perfeito da superficialidade dos anos 20 e do sonho americano.", False),
    Livro("A Guerra dos Tronos", "Fantasia", "Intrigas e batalhas pelo trono de ferro nos Sete Reinos.", "George R.R. Martin", 18, 5, "Uma história épica, com reviravoltas emocionantes e personagens complexos.", False),
    Livro("Orgulho e Preconceito", "Romance","A história de Elizabeth Bennet e sua luta contra o orgulho e o preconceito em sua sociedade.", "Jane Austen", 12, 5, "Um clássico do romance inglês, cheio de inteligência e charme.", False),
    Livro("Frankenstein", "Terror", "O cientista Victor Frankenstein cria um monstro, mas acaba se arrependendo de sua criação.", "Mary Shelley",16, 5, "Uma história que explora os limites da ciência e da humanidade.", False),
    Livro("Cem Anos de Solidão","Realismo Mágico","A saga da família Buendía, marcada por mistério, amor e tragédia em uma cidade fictícia da América Latina.", "Gabriel García Márquez", 16, 5, "Uma das obras mais impactantes da literatura mundial, cheia de magia e poesia.", False),
    Filme("Vingadores: Ultimato", "Ação", "Os Vingadores tentam reverter o estalo de Thanos.", "Marvel Studios", 12, 5, "Épico e emocionante!", False),
    Filme("Titanic", "Romance", "Uma história de amor trágica a bordo do navio Titanic.", "James Cameron", 14, 4, "Clássico que emociona até hoje.", False),
    Filme("O Poderoso Chefão", "Drama", "A história de uma família mafiosa nos EUA.", "Francis Ford Coppola", 16, 5, "Um dos maiores filmes da história do cinema.", False),
    Filme("Forrest Gump", "Drama", "A vida extraordinária de um homem simples com um coração puro.", "Robert Zemeckis", 12, 5, "Inspirador e comovente.", False),
    Filme("Duna", "Ficção Científica", "Após a visita de uma mulher misteriosa, ele é obrigado a deixar seu planeta natal para sobreviver ao ambiente árido e severo de Arrakis.", "Denis Villeneuve", 14, 4, "O Filme está repleto de cenas épicas e muito chocantes, a direção de Denis Villeneuve junto com os roteiristas fizeram um filme excelente.", False),
]
favoritos = []

# Funções para cadastrar

# Função para procurar pelo genero especifico pelo usuario
def procura_por_genero():
    genero = input("\nDigite o gênero que deseja procurar: ").strip().lower()
    encontrados = [m for m in avaliacoes if m.genero.lower() == genero]

    if not encontrados:
        print(f"\nNenhuma mídia encontrada no gênero '{genero}'.")
    else:
        print(f"\n--- Mídias do gênero '{genero}' ---")
        for m in encontrados:
            m.exibir_detalhes()

# Função para procurar pelo titulo especifico pelo usuario
def procura_por_titulo():
    titulo = input("\nDigite o título da mídia: ").strip().lower()
    encontrados = [m for m in avaliacoes if m.titulo.lower() == titulo]

    if not encontrados:
        print(f"\nNenhuma mídia com o título '{titulo}' foi encontrada.")
    else:
        print(f"\n--- Resultado para '{titulo}' ---")
        for m in encontrados:
            m.exibir_detalhes()

# Função para procurar pela idade especifico pelo usuario
def procura_por_idade():
    try:
        idade = int(input("\nDigite sua idade: "))
        encontrados = [m for m in avaliacoes if m.idade_classificada <= idade]

        if not encontrados:
            print(f"\nNenhuma mídia disponível para a idade {idade}.")
        else:
            print(f"\n--- Mídias para maiores de {idade} ---")
            for m in encontrados:
                m.exibir_detalhes()
    except ValueError:
        print("Erro: Digite um número inteiro válido para a idade.")

# Função para procurar pela nota especifico pelo usuario
def procura_por_nota():
    try:
        nota = int(input("\nDigite a nota (1 a 5 estrelas): "))
        if nota < 1 or nota > 5:
            print("A nota deve estar entre 1 e 5.")
            return

        encontrados = [m for m in avaliacoes if m.nota_final == nota]

        if not encontrados:
            print(f"\nNenhuma mídia com {nota} estrela(s) foi encontrada.")
        else:
            print(f"\n--- Mídias com {nota} estrela(s) ---")
            for m in encontrados:
                m.exibir_detalhes()
    except ValueError:
        print("Erro: Digite um número inteiro de 1 a 5.")


# Função para mostrar a quantidade cadastrada de livros
def mostrar_quantidade_de_livros():
    quantidade = sum(isinstance(m, Livro) for m in avaliacoes)
    print(f"\nQuantidade de livros avaliados: {quantidade}")

# Função para mostrar a quantidade cadastrada de filmes
def mostrar_quantidade_de_filmes():
    quantidade = sum(isinstance(m, Filme) for m in avaliacoes)
    print(f"\nQuantidade de filmes avaliados: {quantidade}")


# Função genérica para garantir nota válida
def obter_nota_valida():
    while True:
        try:
            nota = int(input("Nota (1 a 5 estrelas): "))
            if 1 <= nota <= 5:
                return nota
            else:
                print("Erro: A nota deve estar entre 1 e 5.")
        except ValueError:
            print("Erro: Digite um número inteiro entre 1 e 5.")


def cadastrar_avaliacao():
    tipo = input("\nVocê deseja avaliar um Livro ou Filme? ").strip().lower()

    if tipo not in ['livro', 'filme']:
        print("Tipo inválido.")
        return

    titulo = input("Título: ").strip()
    genero = input("Gênero: ").strip()
    sinopse = input("Sinopse: ").strip()
    autor = input("Autor/Estúdio: ").strip()
    idade = int(input("Idade Classificada: "))
    critica = input("Crítica: ").strip()
    nota = obter_nota_valida()
    favorito = input("Deseja adicionar aos favoritos? (s/n): ").strip().lower() == 's'

    if tipo == 'livro':
        midia = Livro(titulo, genero, sinopse, autor, idade, nota, critica, favorito)
    else:
        midia = Filme(titulo, genero, sinopse, autor, idade, nota, critica, favorito)

    avaliacoes.append(midia)
    if favorito:
        favoritos.append(midia)

    print("Avaliação cadastrada com sucesso!")


def listar_todas_as_avaliacoes():
    if not avaliacoes:
        print("\nNenhuma avaliação cadastrada.")
        return

    print("\n--- Todas as Avaliações ---")
    for midia in avaliacoes:
        midia.exibir_detalhes()

def mostrar_maiores_notas():
    if not avaliacoes:
        print("\nNenhuma avaliação disponível.")
        return

    maior_nota = 1  # menor possível
    for m in avaliacoes:
        if m.nota_final > maior_nota:
            maior_nota = m.nota_final

    print(f"\n--- Mídias com {maior_nota} estrelas ---")
    for m in avaliacoes:
        if m.nota_final == maior_nota:
            m.exibir_detalhes()
            time.sleep(2)


def mostrar_menores_notas():
    if not avaliacoes:
        print("\nNenhuma avaliação disponível.")
        return

    menor_nota = 5  # maior possível
    for m in avaliacoes:
        if m.nota_final < menor_nota:
            menor_nota = m.nota_final

    print(f"\n--- Mídias com {menor_nota} estrelas ---")
    for m in avaliacoes:
        if m.nota_final == menor_nota:
            m.exibir_detalhes()
            time.sleep(2)


def top_5_livros():
    livros = [m for m in avaliacoes if isinstance(m, Livro)]

    if not livros:
        print("\nNenhum livro avaliado.")
        return

    livros.sort(key=lambda l: l.nota_final, reverse=True)

    print("\n--- Top 5 Livros ---")
    for i, livro in enumerate(livros[:5], 1):
        print(f"\n#{i}")
        livro.exibir_detalhes()
        if i < len(livros[:5]):
            print("\nPróximo livro será exibido em 5 segundos...\n")
            time.sleep(5)


def top_5_filmes():
    filmes = [m for m in avaliacoes if isinstance(m, Filme)]

    if not filmes:
        print("\nNenhum filme avaliado.")
        return

    filmes.sort(key=lambda f: f.nota_final, reverse=True)

    print("\n--- Top 5 Filmes ---")
    for i, filme in enumerate(filmes[:5], 1):
        print(f"\n#{i}")
        filme.exibir_detalhes()
        if i < len(filmes[:5]):
            print("\nPróximo filme será exibido em 5 segundos...\n")
            time.sleep(5)


def recomendar_midias(cliente: Cliente):
    if not avaliacoes:
        print("\nNenhuma mídia disponível para recomendação.")
        return

    genero_desejado = input("\nQual gênero você gosta? ").strip().lower()
    idade_usuario = cliente.calcular_idade()
    
    if idade_usuario is None:
        return

    recomendadas = []
    for midia in avaliacoes:
        genero_midia = midia.genero.lower()
        idade_classificada = midia.idade_classificada

        if genero_midia == genero_desejado:
            if idade_usuario >= idade_classificada:
                recomendadas.append(midia)
            elif idade_classificada == 0:
                recomendadas.append(midia)

    if not recomendadas:
        print("\nNenhuma mídia encontrada com base nas suas preferências e idade.")
    else:
        print(f"\n--- Recomendações para {cliente.nome} ---")
        for midia in recomendadas:
            midia.exibir_detalhes()

# Função principal
if __name__ == "__main__":
    exibir_menu()


