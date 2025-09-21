from time import sleep

favoritos = []  # Lista global para armazenar favoritos

def adicionar_aos_favoritos(avaliacoes):
    print("\nEscolha um item para adicionar aos seus favoritos:")
    for i, midia in enumerate(avaliacoes, 1):
        print(f"{i} - {midia.titulo} ({midia.__class__.__name__})")
    try:
        escolha = int(input("\nDigite o número correspondente ao item: "))
        if 1 <= escolha <= len(avaliacoes):
            midia_selecionada = avaliacoes[escolha - 1]
            if not midia_selecionada.favorito:
                midia_selecionada.favorito = True
                favoritos.append(midia_selecionada)
                print(f"{midia_selecionada.titulo} foi adicionado aos seus favoritos!")
            else:
                print(f"{midia_selecionada.titulo} já está nos seus favoritos.")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Erro: Digite um número válido.")

def listar_favoritos():
    if not favoritos:
        print("\nNenhum favorito adicionado.")
        return
    print("\n--- Mídias Favoritas ---")
    for fav in favoritos:
        fav.exibir_detalhes()
        sleep(2)