import json
import main

def print_menu(assets_path):
    while True:
        main.screen_clear()

        menu_opts = ({'id':1, 'info': 'Atualizar profissional'},
                     {'id':2, 'info': 'Pesquisar por cidade'},
                     {'id':3, 'info': 'Pesquisar por especialidade'},
                     {'id':0, 'info': 'Voltar ao menu inicial'})
    
        print('>> Menu: Profissionais <<')
        for opt in menu_opts:
            print('     {id}. {info}'.format(**opt))
        
        try:
            selected = int(input('Escolha uma opção: '))
        except ValueError as error:
            selected = None

        while selected == None or not selected.is_integer or selected < 0 or selected > 3:
            print("\n>>>> ATENÇÃO: Escolha uma opção válida!")

            try:
                selected = int(input('Escolha uma opção: '))
            except ValueError as error:
                selected = None
        
        if selected == 0:
            return 0
        elif selected == 1:
            update_professional(assets_path)
        elif selected == 2:
            search_by_city(assets_path)
        elif selected == 3:
            search_by_expertise(assets_path)

# Função para ler os profissionais cadastrados
def read_professionals(assets_path):
    with open(f'{assets_path}/professionals.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Função para atualizar um profissional
def update_professional(assets_path):
    main.screen_clear()
    print('>> Atualização de profissional <<\n')

    # Recebe os estabelecimentos já cadastrados
    professionalsbase = read_professionals(assets_path)

    search_description = input('Qual estabelecimento deseja pesquisar? ')

    # Lista auxiliar para verificar se o estabelecimento já existe
    # Executará um laço para inserir as ocorrências deste estabelecimento
    # Caso o estabelecimento não tenha ocorrência, pergunta se deve realizar o registro
    professionals_list = []

    for idx in range(len(professionalsbase)):
        professionals_list.append(professionalsbase[idx].get('NAME'))

    # Busca por ocorrências com a substring da descrição na base de produtos
    found = [ idx for idx in professionals_list if search_description.capitalize() in idx ]

    if len(found) == 0:
        print('\nNenhum profissional encontrado com este nome')
    else:
        print('\nProfissionais encontrados: ')
        
        for idx in range(len(found)):
            print(f'     {idx + 1}. {found[idx]}')
        
        selected = int(input('\nQual profissional deseja atualizar? ')) -1

        professional_index = professionals_list.index(found[selected])

        new_name = input('\nNovo nome (deixe em branco para não alterar): ')
        new_expertise = input('Nova especialização (deixe em branco para não alterar): ')
        new_phone = input('Novo telefone (deixe em branco para não alterar): ')
        new_email = input('Novo email (deixe em branco para não alterar): ')
        new_social = input('Nova rede social (deixe em branco para não alterar): ')
        new_address = input('Novo endereço (deixe em branco para não alterar): ')
        new_city = input('Nova cidade (deixe em branco para não alterar): ')
        new_site = input('Novo site (deixe em branco para não alterar): ')
        new_bio = input('Nova biografia (deixe em branco para não alterar): ')

        if new_name:
            professionalsbase[professional_index]['NAME'] = new_name
        if new_expertise:
            professionalsbase[professional_index]['TYPE'] = new_expertise
        if new_phone:
            professionalsbase[professional_index]['PHONE'] = new_phone
        if new_email:
            professionalsbase[professional_index]['EMAIL'] = new_email
        if new_social:
            list_social = []

            if len(professionalsbase[professional_index].get('SOCIAL')) == 0:
                list_social.append(new_social)
            else:
                for socials in professionalsbase[professional_index].get('SOCIAL'):
                    list_social.append(socials)
                
                list_social.append(new_social)
            
            professionalsbase[professional_index]['SOCIAL'] = list_social
        if new_address:
            professionalsbase[professional_index]['ADDRESS'] = new_address
        if new_city:
            professionalsbase[professional_index]['CITY'] = new_city
        if new_site:
            professionalsbase[professional_index]['SITE'] = new_site
        if new_bio:
            professionalsbase[professional_index]['BIO'] = new_bio

        print('DADOS ATUALIZADOS')
        print(f'\nNome: {professionalsbase[professional_index].get('NAME')}')
        print(f'Especialização: {professionalsbase[professional_index].get('EXPERTISE')}')
        print(f'Telefone: {professionalsbase[professional_index].get('PHONE')}')
        print(f'Email: {professionalsbase[professional_index].get('EMAIL')}')

        print('Redes socials:')
        for idx, social in enumerate(professionalsbase[professional_index].get('SOCIAL')):
            print(f'>> {idx + 1}: {social}')

        print(f'Endereço: {professionalsbase[professional_index].get('ADDRESS')}')
        print(f'Cidade: {professionalsbase[professional_index].get('CITY')}')

        print(f'Site: {professionalsbase[professional_index].get('SITE')}')
        print(f'Biografia: {professionalsbase[professional_index].get('BIO')}')
    
    # Salva a lista no arquivo de produtos
    with open(f'{assets_path}/professionals.json', 'w', encoding='utf-8') as file:
        json.dump(professionalsbase, file, indent=4, ensure_ascii=False)

    print('\n>> Profissional atualizado com sucesso! <<')    
    main.press_continue()

# Função para pesquisar por cidade
def search_by_city(assets_path):
    main.screen_clear()
    print('>> Pesquisa de profissionais (por cidade) <<\n')

    # Recebe os profissionais já cadastrados
    professionalsbase = read_professionals(assets_path)

    search_description = input('Qual a cidade do profissional? ')

    # Executará um laço para inserir as ocorrências
    places_list = []

    for idx in range(len(professionalsbase)):
        if professionalsbase[idx].get('CITY') == search_description:
            places_list.append(professionalsbase[idx].get('NAME'))

    # Busca por ocorrências com a substring da descrição na base de produtos
    found = [ idx for idx in places_list if search_description.capitalize() in idx ]

    if len(found) == 0:
        print('\nNenhum profissional encontrado nesta cidade')
    else:
        print('\nProfissionais encontrados: ')
        
        for idx in range(len(found)):
            print(f'     {idx + 1}. {found[idx]}')

        selected = int(input('\nQual profissional deseja mais informações? ')) -1

        professional_index = places_list.index(found[selected])

        print(f'\nNome: {professionalsbase[professional_index].get('NAME')}')
        print(f'Especialização: {professionalsbase[professional_index].get('EXPERTISE')}')
        print(f'Telefone: {professionalsbase[professional_index].get('PHONE')}')
        print(f'Email: {professionalsbase[professional_index].get('EMAIL')}')

        print('Redes socials:')
        for idx, social in enumerate(professionalsbase[professional_index].get('SOCIAL')):
            print(f'>> {idx + 1}: {social}')

        print(f'Endereço: {professionalsbase[professional_index].get('ADDRESS')}')
        print(f'Cidade: {professionalsbase[professional_index].get('CITY')}')

        print(f'Site: {professionalsbase[professional_index].get('SITE')}')
        print(f'Biografia: {professionalsbase[professional_index].get('BIO')}')
    
    main.press_continue()

# Função para pesquisar por especialidade
def search_by_expertise(assets_path):
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
        print(f'Total de avaliações: {placesbase[place_index].get('NUMBER STARS')}')

        print('Avaliações:')
        for idx, review in enumerate(placesbase[place_index].get('REVIEWS')):
            print(f'>> {idx + 1}: {review}')
        
        print('Serviços:')
        for idx, service in enumerate(placesbase[place_index].get('SERVICES')):
            print(f'>> {idx + 1}: {service}')
    
    main.press_continue()
