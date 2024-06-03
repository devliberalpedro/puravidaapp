import os
import getpass
import usuarios
from pathlib import Path

# Função para controlar o login de usuário
# Permite a criação de um novo usuário
def login(assets_path):
    print('PURAVIDA APP - CRUD')
    print('Senha para login na versão CRUD: puravidaapp')

    # Cria uma lista de dicionários com as informações dos usuários
    lista_usuarios = usuarios.ler_usuarios(assets_path)
    
    # Solicita o input do usuário que se está tentando fazer login
    usuario = input('Usuário: ')

    # Lista auxiliar para verificar se o usuário já existe
    # Executará um laço para inserir as ocorrências deste usuário
    # Caso o usuário não tenha ocorrência, pergunta se deve realizar o registro
    lista_usernames = []

    for idx in range(len(lista_usuarios)):
        lista_usernames.append(lista_usuarios[idx].get('username'))

    if lista_usernames.count(usuario) == 0:
        escolha = input("Usuário não encontrado. Deseja se registrar (S/N)? ")

        if escolha.upper() == "S":
            usuarios.registar_usuario(assets_path)
    else:
        # O método getpass permite que a senha seja inserida sem exibição no terminal
        # Caso a senha seja compatível com a padrão do CRUD, a função retorna True
        senha = getpass.getpass("Senha: ")

        # Sistema CRUD com senha padrão, caso seja diferente da informada, o sistema
        # retorna False
        if senha != "puravidaapp":
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
    usuarios.criar_usuario_base(assets_path)

    # Gerencia o login no sistema
    # Caso a função retorne falso (1), termina a execução do app
    if not login(assets_path):
        print("Senha inválida! Você foi desconectado!")
