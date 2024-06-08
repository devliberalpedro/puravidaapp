import os
import getpass
import users
from pathlib import Path

# Função para controlar o login de usuário
# Permite a criação de um novo usuário
def login(assets_path):
    print('PURAVIDA APP - CRUD')
    print('Senha para login na versão CRUD: puravidaapp')

    # Cria uma lista de dicionários com as informações dos usuários
    users_list = users.read_users(assets_path)
    
    # Solicita o input do usuário que se está tentando fazer login
    user = input('Usuário: ')

    # Lista auxiliar para verificar se o usuário já existe
    # Executará um laço para inserir as ocorrências deste usuário
    # Caso o usuário não tenha ocorrência, pergunta se deve realizar o registro
    usernames_list = []

    for idx in range(len(users_list)):
        usernames_list.append(users_list[idx].get('USERNAME'))

    if usernames_list.count(user) == 0:
        option = input("Usuário não encontrado. Deseja se registrar (S/N)? ")

        if option.upper() == "S":
            users.user_signup(assets_path)
    
    # O método getpass permite que a senha seja inserida sem exibição no terminal
    # Caso a senha seja compatível com a padrão do CRUD, a função retorna True
    password = getpass.getpass("Senha: ")

    # Sistema CRUD com senha padrão, caso seja diferente da informada, o sistema
    # retorna False
    if password != "puravidaapp":
        return False
        
    return True

# Função Main do app
if __name__ == "__main__":
    # Executa a limpeza do console para qualquer sistema operacional
    # windows: cls linux/apple: clear
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    # Define o diretório para os arquivos com extenção .json
    assets_path = Path('./assets/')

    # Caso seja a primeira execução, cria a pasta e o arquivo de usuários com o padrão
    users.create_usersbase(assets_path)

    # Gerencia o login no sistema
    # Caso a função retorne falso (1), termina a execução do app
    if not login(assets_path):
        print("Senha inválida! Você foi desconectado!")
    
    menu_opts = ({'id':1, 'info': 'Menu de produtos'},
                 {'id':2, 'info': 'Menu de estabelecimentos'},
                 {'id':3, 'info': 'Menu de profissionais'})
    
    for opt in menu_opts:
        print('{id}. {info}'.format(**opt))