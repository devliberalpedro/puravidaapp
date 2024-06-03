import json
from pathlib import Path

# Cria op arquivo json com os usuários padrões (caso não exista)
def criar_usuario_base(assets_path):
    if not assets_path.exists():
        assets_path.mkdir()

    file_path = Path('./' + str(assets_path) + '/usuarios.json')

    if not file_path.exists():
        usuario_base = [{
                            'id':'1',
                            'nome':'Pura Vida App',
                            'username':'puravidaapp',
                            'bio':'Usuário padrão',
                            'restricao':False,
                            'restricao_id':[],
                            'ultimo_login':''
                        },
                        {
                            'id':'2',
                            'nome':'Pedro Henrique Guimarães Liberal',
                            'username':'phgl',
                            'bio':'Programador, fotógrafo e eterno aprendiz',
                            'restricao':False,
                            'restricao_id':[],
                            'ultimo_login':''}]
        
        with open(f'{assets_path}/usuarios.json', 'w', encoding='utf-8') as arquivo:
            json.dump(usuario_base, arquivo, indent=4, ensure_ascii=False)

# Função para ler os usuários cadastrados
def ler_usuarios(assets_path):
    with open(f'{assets_path}/usuarios.json', 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

# Função para cadastrar novo usuário
def registar_usuario(assets_path):
    print('Cadastro de novo usuário\n\n')

    # Recebe os usuários já cadastrados
    usuarios_cadastrados = ler_usuarios(assets_path)

    # Recebe o id do último usuárko cadastrado e soma 1
    # O resultado desta soma será o id do novo usuário
    novo_id = int(usuarios_cadastrados[-1].get('id')) + 1

    novo_nome = input('Informe o seu nome: ')
    novo_username = input('Informe o username: ')
    nova_bio = input('Descreva sua bio (entre para em branco): ')
    
    escolha_restricao = input('Possui restrição alimentar (S/N)? ')
    novo_restricao = True if escolha_restricao.upper() == 'S' else False

    # Cria o dicionário a ser adicionado na lista
    novo_usuario = {'id': novo_id,
                    'nome': novo_nome,
                    'username': novo_username,
                    'bio': nova_bio,
                    'restricao': novo_restricao,
                    'restricao_id': [],
                    'ultimo_login': ''
                    }
    
    usuarios_cadastrados.append(novo_usuario)

    # Salva a lista no arquivo de usuários
    with open(f'{assets_path}/usuarios.json', 'w', encoding='utf-8') as arquivo:
        json.dump(usuarios_cadastrados, arquivo, indent=4, ensure_ascii=False)