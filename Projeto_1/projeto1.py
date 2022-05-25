import json
import os.path
import re
import sys
from turtle import st

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados: list[dict]) -> list[str]:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    lista_categorias = []
    for produto in dados:
        if produto["categoria"] not in lista_categorias:
            lista_categorias.append(produto["categoria"])
    lista_categorias = sorted(lista_categorias)
    return lista_categorias

def listar_por_categoria(dados: list[dict], categoria: str) -> list[dict | str]:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    lista_categorias = listar_categorias(dados)
    if categoria not in lista_categorias:
        return ["Categoria inexistente!\n"]
    else:
        lista_produtos_por_categoria = []
        for produto in dados:
            if produto["categoria"] == categoria:
                lista_produtos_por_categoria.append(produto)
        return lista_produtos_por_categoria
   
def encontrar_produto_mais_caro(dados: list[dict], categoria: str) -> list[dict | str]:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    lista_produtos_por_categoria = listar_por_categoria(dados, categoria)
    if lista_produtos_por_categoria == ["Categoria inexistente!\n"]:
        return ["Categoria inexistente!\n"]
    else:
        produto_mais_caro = sorted(lista_produtos_por_categoria, key = lambda x: float(x["preco"]), reverse = True)
        produto_mais_caro = produto_mais_caro[:1]
        return produto_mais_caro

def encontrar_produto_mais_barato(dados: list[dict], categoria: str) -> list[dict | str]:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais barato da categoria dada.
    '''
    lista_produtos_por_categoria = listar_por_categoria(dados, categoria)
    if lista_produtos_por_categoria == ["Categoria inexistente!\n"]:
        return ["Categoria inexistente!\n"]
    else:
        produto_mais_barato = sorted(lista_produtos_por_categoria, key = lambda x: float(x["preco"]))
        produto_mais_barato = produto_mais_barato[:1]
        return produto_mais_barato

def top_10_caros(dados: list[dict]) -> list[dict]:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    lista_top_10_caros = sorted(dados, key = lambda x: [float(x["preco"])], reverse = True)
    lista_top_10_caros = lista_top_10_caros[:10]
    return lista_top_10_caros

def top_10_baratos(dados:list[dict]) -> list[dict]:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    lista_top_10_baratos = sorted(dados, key = lambda x: [float(x["preco"])])
    lista_top_10_baratos = lista_top_10_baratos[:10]
    return lista_top_10_baratos

def printer_de_produto(produto: dict) -> None:
    print(f'ID: {produto["id"]}')
    print(f'Preço: {produto["preco"]}')
    print(f'Categoria: {produto["categoria"]}\n')

def printer_de_lista(lista: list) -> None:
    print()
    for i in lista:
        if type(i) == dict:
            printer_de_produto(i)
        else:
            print(i)

def menu(dados: list[dict]) -> None:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    opcao_usuario = ""
    opcoes_validas = list("0123456")
    opcao_saida = "0"

    bem_vindo = "Olá, estas são as funções do programa:"
    opcao_1 = "1. Listar categorias"
    opcao_2 = "2. Listar produtos de uma categoria"
    opcao_3 = "3. Produto mais caro por categoria"
    opcao_4 = "4. Produto mais barato por categoria"
    opcao_5 = "5. Top 10 produtos mais caros"
    opcao_6 = "6. Top 10 produtos mais baratos"
    opcao_0 = "0. Sair"
    entrada = "Digite a opção desejada: "
    
    while opcao_usuario != opcao_saida: 
        opcao_usuario = input(f'{bem_vindo}\n{opcao_1}\n{opcao_2}\n{opcao_3}\n{opcao_4}\n{opcao_5}\n{opcao_6}\n{opcao_0}\n{entrada}')

        if opcao_usuario not in opcoes_validas:
            print("\nOpção inválida, tente novamente!\n")

        if opcao_usuario == "1":
            print("\nLista de categorias:")
            printer_de_lista(listar_categorias(dados))
            print()

        if opcao_usuario == "2":
            print("\nProdutos de uma categoria:")
            categoria = input("Digite a categoria desejada: ")
            printer_de_lista(listar_por_categoria(dados, categoria))

        if opcao_usuario == "3":
            print("\nProduto mais caro de uma categoria:")
            categoria = input("Digite a categoria desejada: ")
            printer_de_lista(encontrar_produto_mais_caro(dados, categoria))

        if opcao_usuario == "4":
            print("\nProduto mais barato de uma categoria:")
            categoria = input("Digite a categoria desejada: ")
            printer_de_lista(encontrar_produto_mais_barato(dados, categoria))

        if opcao_usuario == "5":
            print(f"\nLista de top 10 produtos mais caros:")
            printer_de_lista(top_10_caros(dados))

        if opcao_usuario == "6":
            print(f"\nLista de top 10 produtos mais baratos:")
            printer_de_lista(top_10_baratos(dados))

    else:
        print("Você saiu do programa!")

# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)
