import json
import os
from pathlib import Path
from main import screen_clear, press_continue

def print_menu(assets_path):
    while True:
        screen_clear()

        menu_opts = ({'id':1, 'info': 'Alterar produto'},
                     {'id':2, 'info': 'Cadastrar produto'},
                     {'id':3, 'info': 'Comparar produtos'},
                     {'id':4, 'info': 'Pesquisar produto'},
                     {'id':5, 'info': 'Remover produto'},
                     {'id':0, 'info': 'Voltar ao menu inicial'})
    
        print('>> Menu: Compare e Conheça <<')
        for opt in menu_opts:
            print('     {id}. {info}'.format(**opt))
        
        try:
            selected = int(input('Escolha uma opção: '))
        except ValueError as error:
            selected = None

        while selected == None or not selected.is_integer or selected < 0 or selected > 5:
            print("\n>>>> ATENÇÃO: Escolha uma opção válida!")

            try:
                selected = int(input('Escolha uma opção: '))
            except ValueError as error:
                selected = None
        
        if selected == 0:
            return 0
        elif selected == 1:
            update_product(assets_path)
        elif selected == 2:
            register_product(assets_path)
        elif selected == 3:
            compare_products(assets_path)
        elif selected == 4:
            search_products(assets_path)
        elif selected == 5:
            remove_product(assets_path)

# Função para ler os produtos cadastrados
def read_products(assets_path):
    with open(f'{assets_path}/products.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Função para atualizar produto
def update_product(assets_path):
    screen_clear()
    print('>> Atualização de produto <<\n')

# Função para cadastrar produtos
def register_product(assets_path):
    screen_clear()
    print('>> Cadastro de produtos <<\n')

    # Recebe os usuários já cadastrados
    productbase = read_products(assets_path)

    # Recebe o id do último usuárko cadastrado e soma 1
    # O resultado desta soma será o id do novo usuário
    new_id = int(productbase[-1].get('ID')) + 1

    new_description = input('Informe descrição (nome) do produto: ')
    new_brand = input('Informe a marca do produto: ')
    new_restriction = input('Qual restrição o produto atende? ')
    new_stars = int(input('Com quantas estrelas você avalia o produto? '))
    new_review = input('Escreva uma avaliação do produto: ')

    # Cria o dicionário a ser adicionado na lista
    new_product = {'ID': new_id,
                'DESCRIPTION': new_description,
                'BRAND': new_brand,
                'RESTRICTION': new_restriction,
                'STARS': new_stars,
                'REVIEWS': new_review
                }
    
    productbase.append(new_product)

    # Salva a lista no arquivo de produtos
    with open(f'{assets_path}/products.json', 'w', encoding='utf-8') as file:
        json.dump(productbase, file, indent=4, ensure_ascii=False)

# Função para comprar produtos
def compare_products(assets_path):
    screen_clear()
    print('>> Comparar produtos <<\n')

# Função para pesquisar produtos
def search_products(assets_path):
    screen_clear()
    print('>> Pesquisar produtos <<\n')

# Remove um produto
def remove_product(assets_path):
    screen_clear()
    print('>> Remover produto <<\n')

    # Recebe os usuários já cadastrados
    productbase = read_products(assets_path)

    search_description = input('Qual produto deseja remover? ')

    # Lista auxiliar para verificar se o usuário já existe
    # Executará um laço para inserir as ocorrências deste usuário
    # Caso o usuário não tenha ocorrência, pergunta se deve realizar o registro
    products_list = []

    for idx in range(len(productbase)):
        products_list.append(productbase[idx].get('DESCRIPTION'))

    # Busca por ocorrências com a substring da descrição na base de produtos
    found = [ idx for idx in products_list if search_description.capitalize() in idx ]

    if len(found) == 0:
        print('Nenhum produto encontrado com esta descrição')
    else:
        print('Produtos encontrados: ')
        
        for idx in range(len(found)):
            print(f'     {idx + 1}. {found[idx]}')
        
        print(productbase)
        selected = int(input('Qual produto deseja remover? '))

        print(products_list(found[selected - 1]))
        
        deleting = products_list(found[selected - 1])
        del productbase[deleting]
        print(productbase)

        # Salva a lista no arquivo de produtos
        #with open(f'{assets_path}/products.json', 'w', encoding='utf-8') as file:
        #    json.dump(products_list, file, indent=4, ensure_ascii=False)
    
        print('>> Produto excluído do sistema com sucesso! <<')
    
    press_continue()
