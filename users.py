import json
from pathlib import Path

# Função para ler os usuários cadastrados
def read_users(assets_path):
    with open(f'{assets_path}/users.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Função para cadastrar novo usuário
def user_signup(assets_path):
    print('>> Cadastro de usuário <<\n')

    # Recebe os usuários já cadastrados
    usersbase = read_users(assets_path)

    # Recebe o id do último usuárko cadastrado e soma 1
    # O resultado desta soma será o id do novo usuário
    new_id = int(usersbase[-1].get('ID')) + 1

    new_name = input('Informe o seu nome: ')
    new_username = input('Informe o username: ')
    new_bio = input('Descreva sua bio (entre para em branco): ')
    
    has_restriction = input('Possui restrição alimentar (S/N)? ')
    new_restriction = True if has_restriction.upper() == 'S' else False

    # Cria o dicionário a ser adicionado na lista
    new_user = {'ID': new_id,
                'NAME': new_name,
                'USERNAME': new_username,
                'BIO': new_bio,
                'RESTRICTION': new_restriction,
                'RESTRICTION_ID': [],
                'LAST_LOGIN': ''
                }
    
    usersbase.append(new_user)

    # Salva a lista no arquivo de usuários
    with open(f'{assets_path}/users.json', 'w', encoding='utf-8') as file:
        json.dump(usersbase, file, indent=4, ensure_ascii=False)

# Cria op arquivo json com os usuários padrões (caso não exista)
def create_usersbase(assets_path):
    if not assets_path.exists():
        assets_path.mkdir()

    file_path = Path('./' + str(assets_path) + '/users.json')

    if not file_path.exists():
        basic_users = [{
                            'ID':'1',
                            'NAME':'Pura Vida App',
                            'USERNAME':'puravidaapp',
                            'BIO':'Usuário padrão',
                            'RESTRICTION':False,
                            'RESTRICTION_ID':[],
                            'LAST_LOGIN':''
                        },
                        {
                            'ID':'2',
                            'NAME':'Pedro Henrique Guimarães Liberal',
                            'USERNAME':'phgl',
                            'BIO':'Programador, fotógrafo e eterno aprendiz',
                            'RESTRICTION':False,
                            'RESTRICTION_ID':[],
                            'LAST_LOGIN':''}]
        
        with open(f'{assets_path}/users.json', 'w', encoding='utf-8') as file:
            json.dump(basic_users, file, indent=4, ensure_ascii=False)
