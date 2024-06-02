import json
from pathlib import Path

# PuraVida App
#

# Cria op arquivo json com os usuários padrões (caso não exista)
def criar_usuario_base(assets_path):
    if not assets_path.exists():
        assets_path.mkdir()

    if not assets_path.is_file():
        usuario_base = [{
                            "id":"1",
                            "nome":"Pura Vida App",
                            "login":"puravidaapp",
                            "bio":"Usuário padrão",
                            "restricao":False,
                            "restricao_id":[],
                            "ultimo_login":""
                        },
                        {
                            "id":"2",
                            "nome":"Pedro Henrique Guimarães Liberal",
                            "login":"phgl",
                            "bio":"Programador, fotógrafo e eterno aprendiz",
                            "restricao":False,
                            "restricao_id":[],
                            "ultimo_login":""}]
        
        with open(f"{assets_path}/usuarios.json", "w", encoding="utf-8") as arquivo:
            json.dump(usuario_base, arquivo, indent=4, ensure_ascii=False)

def login(assets_path):
    print("PURAVIDA APP - CRUD")
    print("Senha para login na versão CRUD: puravidaapp")

    with open(f"{assets_path}/usuarios.json", "r", encoding="utf-8") as arquivo:
        lista_usuarios = json.load(arquivo)
    
    print(lista_usuarios)
    print("")
    print(lista_usuarios[0])
    print("")
    print(lista_usuarios[1])
    print("")
    print("")
    print("")
    print(lista_usuarios[1].get("nome"))

if __name__ == "__main__":
    assets_path = Path("./assets/")

    criar_usuario_base(assets_path)
    login(assets_path)
