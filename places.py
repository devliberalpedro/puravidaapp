import json
import main

def print_menu(assets_path):
    while True:
        main.screen_clear()

        menu_opts = ({'id':1, 'info': 'Alterar estabelecimento'},
                     {'id':2, 'info': 'Cadastrar estabelecimento'},
                     {'id':3, 'info': 'Pesquisar estabelecimento'},
                     {'id':4, 'info': 'Remover estabelecimento'},
                     {'id':0, 'info': 'Voltar ao menu inicial'})
    
        print('>> Menu: Estabelecimentos <<')
        for opt in menu_opts:
            print('     {id}. {info}'.format(**opt))
        
        try:
            selected = int(input('Escolha uma opção: '))
        except ValueError as error:
            selected = None

        while selected == None or not selected.is_integer or selected < 0 or selected > 4:
            print("\n>>>> ATENÇÃO: Escolha uma opção válida!")

            try:
                selected = int(input('Escolha uma opção: '))
            except ValueError as error:
                selected = None
        
        if selected == 0:
            return 0
        elif selected == 1:
            update_places(assets_path)
        elif selected == 2:
            register_places(assets_path)
        elif selected == 3:
            search_places(assets_path)
        elif selected == 4:
            remove_places(assets_path)

# Função para ler os estabelecimento cadastrados
def read_places(assets_path):
    with open(f'{assets_path}/places.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Função para atualizar estabelecimento
def update_places(assets_path):
    main.screen_clear()
    print('>> Atualização de estabelecimentos <<\n')

    # Recebe os estabelecimentos já cadastrados
    placesbase = read_places(assets_path)

    print('\nESTABELECIMENTOS CADASTRADOS')
    for idx in range(len(placesbase)):
        print(f'>> {idx + 1}: {placesbase[idx].get('NAME')}')

    search_description = input('\nQual estabelecimento deseja atualizar (digite ao menos parte da palavra de pesquisa)? ')

    # Lista auxiliar para verificar se o estabelecimento já existe
    # Executará um laço para inserir as ocorrências deste estabelecimento
    # Caso o estabelecimento não tenha ocorrência, pergunta se deve realizar o registro
    places_list = []

    for idx in range(len(placesbase)):
        places_list.append(placesbase[idx].get('NAME'))

    # Busca por ocorrências com a substring da descrição na base de produtos
    found = [ idx for idx in places_list if search_description.capitalize() in idx ]

    if len(found) == 0:
        print('\nNenhum estabelecimento encontrado com este nome')
    else:
        print('\nEstabelecimentos encontrados: ')
        
        for idx in range(len(found)):
            print(f'     {idx + 1}. {found[idx]}')
        
        selected = int(input('\nQual estabelecimento deseja atualizar? ')) -1

        place_index = places_list.index(found[selected])

        new_name = input('\nNovo nome (deixe em branco para não alterar): ')
        new_type = input('Novo tipo (deixe em branco para não alterar): ')
        new_email = input('Novo email (deixe em branco para não alterar): ')
        new_address = input('Novo endereço (deixe em branco para não alterar): ')
        new_city = input('Nova cidade (deixe em branco para não alterar): ')
        new_social = input('Nova rede social (deixe em branco para não alterar): ')
        new_bio = input('Nova biografia (deixe em branco para não alterar): ')
        new_review = input('Nova review (deixe em branco para não alterar): ')
        new_service = input('Novos serviços (deixe em branco para não alterar): ')

        if new_name:
            placesbase[place_index]['NAME'] = new_name
        if new_type:
            placesbase[place_index]['TYPE'] = new_type
        if new_email:
            placesbase[place_index]['EMAIL'] = new_email
        if new_address:
            placesbase[place_index]['ADDRESS'] = new_address
        if new_city:
            placesbase[place_index]['CITY'] = new_city
        if new_social:
            list_social = []

            if len(placesbase[place_index].get('SOCIAL')) == 0:
                list_social.append(new_social)
            else:
                for socials in placesbase[place_index].get('SOCIAL'):
                    list_social.append(socials)
                
                list_social.append(new_social)
            
            placesbase[place_index]['SOCIAL'] = list_social
        if new_bio:
            placesbase[place_index]['BIO'] = new_bio
        if new_review:
            list_reviews = []

            if len(placesbase[place_index].get('REVIEWS')) == 0:
                list_reviews.append(new_review)
            else:
                for reviews in placesbase[place_index].get('REVIEWS'):
                    list_reviews.append(reviews)
                
                list_reviews.append(new_review)
            
            placesbase[place_index]['REVIEWS'] = list_reviews
        if new_service:
            list_services = []

            if len(placesbase[place_index].get('SERVICES')) == 0:
                list_services.append(new_service)
            else:
                for services in placesbase[place_index].get('SERVICES'):
                    list_services.append(services)
                
                list_services.append(new_service)
            
            placesbase[place_index]['SERVICES'] = list_reviews

        print('DADOS ATUALIZADOS')
        print(f'\nNome: {placesbase[place_index].get('NAME')}')
        print(f'Tipo: {placesbase[place_index].get('TYPE')}')
        print(f'Telefone: {placesbase[place_index].get('PHONE')}')
        print(f'Email: {placesbase[place_index].get('EMAIL')}')
        print(f'Endereço: {placesbase[place_index].get('ADDRESS')}')
        print(f'Cidade: {placesbase[place_index].get('CITY')}')

        print('Redes socials:')
        for idx, social in enumerate(placesbase[place_index].get('SOCIAL')):
            print(f'>> {idx + 1}: {social}')
        
        print(f'Biografia: {placesbase[place_index].get('BIO')}')
        
        print('Avaliações:')
        for idx, review in enumerate(placesbase[place_index].get('REVIEWS')):
            print(f'>> {idx + 1}: {review}')
        
        print('Serviços:')
        for idx, service in enumerate(placesbase[place_index].get('SERVICES')):
            print(f'>> {idx + 1}: {service}')
    
    # Salva a lista no arquivo de produtos
    with open(f'{assets_path}/places.json', 'w', encoding='utf-8') as file:
        json.dump(placesbase, file, indent=4, ensure_ascii=False)

    print('\n>> Estabelecimento atualizado com sucesso! <<')    
    main.press_continue()

# Função para cadastrar produtos
def register_places(assets_path):
    main.screen_clear()
    print('>> Cadastro de estabelecimentos <<\n')

    # Recebe os usuários já cadastrados
    placesbase = read_places(assets_path)

    # Recebe o id do último usuárko cadastrado e soma 1
    # O resultado desta soma será o id do novo usuário
    new_id = int(placesbase[-1].get('ID')) + 1

    new_name = input('Nome do estabelecimento: ')
    new_type = input('Tipo do estabelecimento: ')
    new_phone = input('Telefone do estabelecimento: ')
    new_email = input('Email do estabelecimento: ')
    new_address = input('Endereço do estabelecimento: ')
    new_city = input('Cidade do estabelecimento: ')

    add_social = 's'
    list_social = []

    while add_social == 's':
        new_social_name = input('Qual o nome da rede social? ')
        new_social_profile = input('Qual o perfil? ')

        list_social.append(f'{new_social_name}: {new_social_profile}')

        selected = input('Adicionar nova rede (S/N)? ').lower()

        if len(selected) > 1 and selected[0] == 's':
            add_social = 's'
        else:
            add_social = 'n'
    
    new_bio = input('Biografia do estabelecimento: ')
    new_stars = float(input('Nota do estabelecimento (0-5): '))
    new_number_stars = '1'

    list_review = []
    new_review = input('Escreva uma avaliação do estabelecimento: ')
    list_review.append(new_review)

    add_service = 's'
    list_services = []

    while add_service == 's':
        new_service = input('Qual o serviço ofertado (Delivery, Consumo no local, etc)? ')

        list_services.append(new_service)

        selected = input('Adicionar novo serviço (S/N)? ').lower()

        if len(selected) > 1 and selected[0] == 's':
            add_service = 's'
        else:
            add_service = 'n'
    
    # Cria o dicionário a ser adicionado na lista
    new_place = {
                    'ID': new_id,
                    'NAME': new_name,
                    'TYPE': new_type,
                    'PHONE': new_phone,
                    'EMAIL': new_email,
                    'ADDRESS': new_address,
                    'CITY': new_city,
                    'SOCIAL': list_social,
                    'BIO': new_bio,
                    'STARS': new_stars,
                    'NUMBER_STARS': new_number_stars,
                    'REVIEWS': list_review,
                    'SERVICES': list_services
                }
    
    placesbase.append(new_place)

    # Salva a lista no arquivo de produtos
    with open(f'{assets_path}/places.json', 'w', encoding='utf-8') as file:
        json.dump(placesbase, file, indent=4, ensure_ascii=False)
    
    print('\n>> Estabelecimento cadastrado com sucesso! <<')
    main.press_continue()

# Função para pesquisar produtos
def search_places(assets_path):
    main.screen_clear()
    print('>> Pesquisa de estabelecimentos <<\n')

    # Recebe os estabelecimentos já cadastrados
    placesbase = read_places(assets_path)

    search_description = input('Qual estabelecimento deseja pesquisar? ')

    # Lista auxiliar para verificar se o estabelecimento já existe
    # Executará um laço para inserir as ocorrências deste estabelecimento
    # Caso o estabelecimento não tenha ocorrência, pergunta se deve realizar o registro
    places_list = []

    for idx in range(len(placesbase)):
        places_list.append(placesbase[idx].get('NAME'))

    # Busca por ocorrências com a substring da descrição na base de produtos
    found = [ idx for idx in places_list if search_description.capitalize() in idx ]

    if len(found) == 0:
        print('\nNenhum estabelecimento encontrado com este nome')
    else:
        print('\nEstabelecimentos encontrados: ')
        
        for idx in range(len(found)):
            print(f'     {idx + 1}. {found[idx]}')

        selected = int(input('\nQual estabelecimento deseja mais informações? ')) -1

        place_index = places_list.index(found[selected])

        print(f'\nNome: {placesbase[place_index].get('NAME')}')
        print(f'Tipo: {placesbase[place_index].get('TYPE')}')
        print(f'Telefone: {placesbase[place_index].get('PHONE')}')
        print(f'Email: {placesbase[place_index].get('EMAIL')}')
        print(f'Endereço: {placesbase[place_index].get('ADDRESS')}')
        print(f'Cidade: {placesbase[place_index].get('CITY')}')

        print('Redes socials:')
        for idx, social in enumerate(placesbase[place_index].get('SOCIAL')):
            print(f'>> {idx + 1}: {social}')
        
        print(f'Biografia: {placesbase[place_index].get('BIO')}')
        print(f'Avaliação de estrelas: {placesbase[place_index].get('STARS')}')
        print(f'Total de avaliações: {placesbase[place_index].get('NUMBER_STARS')}')

        print('Avaliações:')
        for idx, review in enumerate(placesbase[place_index].get('REVIEWS')):
            print(f'>> {idx + 1}: {review}')
        
        print('Serviços:')
        for idx, service in enumerate(placesbase[place_index].get('SERVICES')):
            print(f'>> {idx + 1}: {service}')
    
    main.press_continue()

# Remove um produto
def remove_places(assets_path):
    main.screen_clear()
    print('>> Remover estabelecimento <<\n')

    # Recebe os produtos já cadastrados
    placesbase = read_places(assets_path)

    search_description = input('Qual estabelecimento você deseja remover? ')

    # Lista auxiliar para verificar se o produto já existe
    # Executará um laço para inserir as ocorrências deste produto
    # Caso o produto não tenha ocorrência, pergunta se deve realizar o registro
    places_list = []

    for idx in range(len(placesbase)):
        places_list.append(placesbase[idx].get('NAME'))

    # Busca por ocorrências com a substring da descrição na base de produtos
    found = [ idx for idx in places_list if search_description.capitalize() in idx ]

    if len(found) == 0:
        print('\nNenhum produto encontrado com esta descrição')
    else:
        print('\Estabelecimentos encontrados: ')
        
        for idx in range(len(found)):
            print(f'     {idx + 1}. {found[idx]}')
        
        selected = int(input('\nQual produto deseja remover? ')) -1
        
        # Deletar o produto selecionado da lista de produtos
        deleting_index = places_list.index(found[selected])
        del placesbase[deleting_index]

        # Salva a lista no arquivo de produtos
        with open(f'{assets_path}/places.json', 'w', encoding='utf-8') as file:
            json.dump(placesbase, file, indent=4, ensure_ascii=False)
    
        print('\n>> Estabelecimento excluído do sistema com sucesso! <<')
    
    main.press_continue()
