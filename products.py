import json
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

    # Recebe os produtos já cadastrados
    productbase = read_products(assets_path)

    search_description = input('Qual produto deseja pesquisar? ')

    # Lista auxiliar para verificar se o produto já existe
    # Executará um laço para inserir as ocorrências deste produto
    # Caso o produto não tenha ocorrência, pergunta se deve realizar o registro
    products_list = []

    for idx in range(len(productbase)):
        products_list.append(productbase[idx].get('DESCRIPTION'))

    # Busca por ocorrências com a substring da descrição na base de produtos
    found = [ idx for idx in products_list if search_description.capitalize() in idx ]

    if len(found) == 0:
        print('\nNenhum produto encontrado com esta descrição')
    else:
        print('\nProdutos encontrados: ')
        
        for idx in range(len(found)):
            print(f'     {idx + 1}. {found[idx]}')
        
        selected = int(input('\nQual produto deseja atualizar? ')) -1

        product_index = products_list.index(found[selected])

        new_description = input('\nNova descrição (deixe em branco para não alterar): ')
        new_brand = input('Nova marca (deixe em branco para não alterar): ')
        new_restriction = input('Adicionar restrição (deixe em branco para não alterar): ')
        new_stars = input('Nova avaliação de estrelas (deixe em branco para não alterar): ')
        new_review = input('Nova avaliação (deixe em branco para não alterar): ')

        if new_description:
            productbase[product_index]['DESCRIPTION'] = new_description
        if new_brand:
            productbase[product_index]['BRAND'] = new_brand
        if new_restriction:
            list_restrictions = []

            if len(productbase[product_index].get('RESTRICTION')) == 0:
                list_restrictions.append(new_restriction)
            else:
                for restriction in productbase[product_index].get('RESTRICTION'):
                    list_restrictions.append(restriction)
                
                list_restrictions.append(new_restriction)
            
            productbase[product_index]['RESTRICTION'] = list_restrictions
        if new_stars:
            productbase[product_index]['STARS'] = new_stars
        if new_review:
            list_reviews = []

            if len(productbase[product_index].get('REVIEWS')) == 0:
                list_reviews.append(new_review)
            else:
                for reviews in productbase[product_index].get('REVIEWS'):
                    list_reviews.append(reviews)
                
                list_reviews.append(new_review)
            
            productbase[product_index]['REVIEWS'] = list_reviews

        print('DADOS ATUALIZADOS')

        print(f'\nDescrição: {productbase[product_index].get('DESCRIPTION')}')
        print(f'Marca: {productbase[product_index].get('BRAND')}')
        print(f'Estrelas: {productbase[product_index].get('STARS')}')

        print('\nIndicado para as restrições:')
        for idx, restriction in enumerate(productbase[product_index].get('RESTRICTION')):
            print(f'>> {idx + 1}: {restriction}')

        print('\nAvaliações:')
        for idx, review in enumerate(productbase[product_index].get('REVIEWS')):
            print(f'>> {idx + 1}: {review}')
    
    # Salva a lista no arquivo de produtos
    with open(f'{assets_path}/products.json', 'w', encoding='utf-8') as file:
        json.dump(productbase, file, indent=4, ensure_ascii=False)

    print('\n>> Produto atualizado com sucesso! <<')    
    press_continue()

# Função para cadastrar produtos
def register_product(assets_path):
    screen_clear()
    print('>> Cadastro de produtos <<\n')

    # Recebe os usuários já cadastrados
    productbase = read_products(assets_path)

    # Recebe o id do último usuárko cadastrado e soma 1
    # O resultado desta soma será o id do novo usuário
    new_id = int(productbase[-1].get('ID')) + 1

    new_description = input('Descrição do produto: ')
    new_brand = input('Marca do produto: ')

    add_restriction = 's'
    list_restriction = []

    while add_restriction == 's':
        new_restriction = input('Qual restrição o produto atende? ')

        list_restriction.append(new_restriction)

        selected = input('Adicionar nova restrição (S/N)? ').lower()

        if len(selected) > 1 and selected[0] == 's':
            add_restriction = 's'
        else:
            add_restriction = 'n'
    
    new_stars = int(input('Com quantas estrelas você avalia o produto? '))

    list_review = []
    new_review = input('Escreva uma avaliação do produto: ')
    list_review.append(new_review)

    # Cria o dicionário a ser adicionado na lista
    new_product = {'ID': new_id,
                    'DESCRIPTION': new_description,
                    'BRAND': new_brand,
                    'RESTRICTION': list_restriction,
                    'STARS': new_stars,
                    'REVIEWS': list_review
                }
    
    productbase.append(new_product)

    # Salva a lista no arquivo de produtos
    with open(f'{assets_path}/products.json', 'w', encoding='utf-8') as file:
        json.dump(productbase, file, indent=4, ensure_ascii=False)
    
    print('\n>> Produto cadastrado com sucesso! <<')
    press_continue()

# Função para comprar produtos
def compare_products(assets_path):
    screen_clear()
    print('>> Comparar produtos <<\n')

    # Recebe os produtos já cadastrados
    productbase = read_products(assets_path)

    search_description = input('Qual produto deseja pesquisar? ')

    # Lista auxiliar para verificar se o produto já existe
    # Executará um laço para inserir as ocorrências deste produto
    # Caso o produto não tenha ocorrência, pergunta se deve realizar o registro
    products_list = []

    for idx in range(len(productbase)):
        products_list.append(productbase[idx].get('DESCRIPTION'))

    # Busca por ocorrências com a substring da descrição na base de produtos
    found = [ idx for idx in products_list if search_description.capitalize() in idx ]

    if len(found) == 0:
        print('\nNenhum produto encontrado com esta descrição')
    else:
        print('\nProdutos encontrados: ')
        
        for idx in range(len(found)):
            print(f'     {idx + 1}. {found[idx]}')
        
        print('\nQual produtos deseja comparar? ')
        selected = input('Informe todos separados por vírgulas: ')
        selected_list = selected.split(',')
        selected_list = [item.strip() for item in selected_list]

        for idx, position in enumerate(selected_list):
            print(f'\nProduto {idx + 1}:')
            product_index = products_list.index(found[int(position) - 1])

            print(f'Descrição: {productbase[product_index].get('DESCRIPTION')}')
            print(f'Marca: {productbase[product_index].get('BRAND')}')
            print(f'Estrelas: {productbase[product_index].get('STARS')}')

            print('\nIndicado para as restrições:')
            for idx, restriction in enumerate(productbase[product_index].get('RESTRICTION')):
                print(f'>> {idx + 1}: {restriction}')

            print('\nAvaliações:')
            for idx, review in enumerate(productbase[product_index].get('REVIEWS')):
                print(f'>> {idx + 1}: {review}')
    
    press_continue()

# Função para pesquisar produtos
def search_products(assets_path):
    screen_clear()
    print('>> Pesquisar produtos <<\n')

    # Recebe os produtos já cadastrados
    productbase = read_products(assets_path)

    search_description = input('Qual produto deseja pesquisar? ')

    # Lista auxiliar para verificar se o produto já existe
    # Executará um laço para inserir as ocorrências deste produto
    # Caso o produto não tenha ocorrência, pergunta se deve realizar o registro
    products_list = []

    for idx in range(len(productbase)):
        products_list.append(productbase[idx].get('DESCRIPTION'))

    # Busca por ocorrências com a substring da descrição na base de produtos
    found = [ idx for idx in products_list if search_description.capitalize() in idx ]

    if len(found) == 0:
        print('\nNenhum produto encontrado com esta descrição')
    else:
        print('\nProdutos encontrados: ')
        
        for idx in range(len(found)):
            print(f'     {idx + 1}. {found[idx]}')
        
        selected = int(input('\nQual produto deseja mais informações? ')) -1

        product_index = products_list.index(found[selected])

        print(f'\nDescrição: {productbase[product_index].get('DESCRIPTION')}')
        print(f'Marca: {productbase[product_index].get('BRAND')}')
        print(f'Estrelas: {productbase[product_index].get('STARS')}')

        print('\nIndicado para as restrições:')
        for idx, restriction in enumerate(productbase[product_index].get('RESTRICTION')):
            print(f'>> {idx + 1}: {restriction}')

        print('\nAvaliações:')
        for idx, review in enumerate(productbase[product_index].get('REVIEWS')):
            print(f'>> {idx + 1}: {review}')
    
    press_continue()

# Remove um produto
def remove_product(assets_path):
    screen_clear()
    print('>> Remover produto <<\n')

    # Recebe os produtos já cadastrados
    productbase = read_products(assets_path)

    search_description = input('Qual produto deseja remover? ')

    # Lista auxiliar para verificar se o produto já existe
    # Executará um laço para inserir as ocorrências deste produto
    # Caso o produto não tenha ocorrência, pergunta se deve realizar o registro
    products_list = []

    for idx in range(len(productbase)):
        products_list.append(productbase[idx].get('DESCRIPTION'))

    # Busca por ocorrências com a substring da descrição na base de produtos
    found = [ idx for idx in products_list if search_description.capitalize() in idx ]

    if len(found) == 0:
        print('\nNenhum produto encontrado com esta descrição')
    else:
        print('\nProdutos encontrados: ')
        
        for idx in range(len(found)):
            print(f'     {idx + 1}. {found[idx]}')
        
        selected = int(input('\nQual produto deseja remover? ')) -1
        
        # Deletar o produto selecionado da lista de produtos
        deleting_index = products_list.index(found[selected])
        del productbase[deleting_index]

        # Salva a lista no arquivo de produtos
        with open(f'{assets_path}/products.json', 'w', encoding='utf-8') as file:
            json.dump(productbase, file, indent=4, ensure_ascii=False)
    
        print('\n>> Produto excluído do sistema com sucesso! <<')
    
    press_continue()
