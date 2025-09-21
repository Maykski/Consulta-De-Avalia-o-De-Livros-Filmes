import time
from cliente import cadastrar_cliente
from trabalhopython.favoritos import adicionar_aos_favoritos, listar_favoritos
from trabalhopython.midia import Livro, Filme
from trabalhopython.meubanco import session
from ProjetoPythonComBD import (
    carregar_avaliacoes_do_banco,
    salvar_avaliacoes_no_banco,
    cadastrar_avaliacao,
    listar_todas_as_avaliacoes,
    mostrar_maiores_notas,
    mostrar_menores_notas,
    top_5_livros,
    top_5_filmes,
    recomendar_midias,
    procura_por_genero,
    procura_por_idade,
    procura_por_nota,
    procura_por_titulo,
)

avaliacoes = []  # Lista global de avaliações

def exibir_menu():
    cliente = None

    # Carregar avaliações do banco de dados ao iniciar o programa
    carregar_avaliacoes_do_banco()

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Cadastrar Cliente")
        print("2. Mostrar dados do cliente")
        print("3. Cadastrar Avaliação")
        print("4. Listar todas as Avaliações")
        print("5. Adicionar aos Favoritos")
        print("6. Listar Favoritos")
        print("7. Mostrar Mídias com Maiores Notas")
        print("8. Mostrar Mídias com Menores Notas")
        print("9. Top 5 Livros")
        print("10. Top 5 Filmes")
        print("11. Procurar por gênero")
        print("12. Procurar por idade")
        print("13. Procurar por nota")
        print("14. Procurar por título")
        print("15. Recomendar Mídias ao Cliente")
        print("16. Salvar Avaliações no Banco de Dados")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            cliente = cadastrar_cliente()
            print("\nCliente cadastrado com sucesso!")

        elif opcao == '2':
            if cliente:
                cliente.dados_clientes()
                print(f"Idade: {cliente.calcular_idade()} anos")
            else:
                print("\nNenhum cliente cadastrado.")

        elif opcao == '3':
            cadastrar_avaliacao()

        elif opcao == '4':
            listar_todas_as_avaliacoes()

        elif opcao == '5':
            adicionar_aos_favoritos(avaliacoes)

        elif opcao == '6':
            listar_favoritos()

        elif opcao == '7':
            mostrar_maiores_notas()

        elif opcao == '8':
            mostrar_menores_notas()

        elif opcao == '9':
            top_5_livros()

        elif opcao == '10':
            top_5_filmes()

        elif opcao == '11':
            procura_por_genero()

        elif opcao == '12':
            procura_por_idade()

        elif opcao == '13':
            procura_por_nota()

        elif opcao == '14':
            procura_por_titulo()

        elif opcao == '15':
            if cliente:
                recomendar_midias(cliente)
            else:
                print("\nCadastre um cliente primeiro!")

        elif opcao == '16':
            salvar_avaliacoes_no_banco()

        elif opcao == '0':
            print("\nEncerrando o programa. Até logo!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

        # Aguarda 5 segundos antes de exibir o menu novamente
        time.sleep(5)