from api.produtos import buscar_produto
from services.produtos import carregar_produtos


def main():

    produtos = carregar_produtos()

    for produto in produtos:

        dados = buscar_produto(produto["nome"])

        print(f"\nPesquisa: {produto['nome']}")

        print(dados)


if __name__ == "__main__":
    main()