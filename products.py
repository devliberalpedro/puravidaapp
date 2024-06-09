import json
import os
from pathlib import Path

def print_menu(assets_path):
    while True:
        menu_opts = ({'id':1, 'info': 'Alterar produto'},
                     {'id':2, 'info': 'Cadastrar produto'},
                     {'id':3, 'info': 'Comparar produtos'},
                     {'id':4, 'info': 'Pesquisar produto'},
                     {'id':5, 'info': 'Remover produto'},
                     {'id':0, 'info': 'Voltar ao menu inicial'})
    
        print('\n>> Menu: Compare e Conheça <<')
        for opt in menu_opts:
            print('     {id}. {info}'.format(**opt))
        
        try:
            selected = int(input('Escolha uma opção: '))
        except ValueError as error:
            selected = None

        while selected == None or not selected.is_integer or selected < 0 or selected > 5:
            print(">>>> ATENÇÃO: Escolha uma opção válida!")

            try:
                selected = int(input('Escolha uma opção: '))
            except ValueError as error:
                selected = None
        
        if selected == 0:
            # Executa a limpeza do console para qualquer sistema operacional
            # windows: cls linux/apple: clear
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

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
    print('>> Atualização de produto <<\n')

# Função para cadastrar produtos
def register_product(assets_path):
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
    new_user = {'ID': new_id,
                'DESCRIPTION': new_description,
                'BRAND': new_brand,
                'RESTRICTION': new_restriction,
                'STARS': new_stars,
                'REVIEWS': new_restriction
                }
    
    productbase.append(new_user)

    # Salva a lista no arquivo de usuários
    with open(f'{assets_path}/products.json', 'w', encoding='utf-8') as file:
        json.dump(productbase, file, indent=4, ensure_ascii=False)

# Função para comprar produtos
def compare_products(assets_path):
    print('>> Comparar produtos <<\n')

# Função para pesquisar produtos
def search_products(assets_path):
    print('>> Pesquisar produtos <<\n')

# Remove um produto
def remove_product(assets_path):
    print('>> Remover produto <<\n')

    # Recebe os usuários já cadastrados
    productbase = read_products(assets_path)