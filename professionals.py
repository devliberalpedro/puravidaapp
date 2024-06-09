#registro profissionais
def registrar_profissional():
    nome = input("Nome completo: ")
    especialidade = input("Especialidade médica: ")
    cidade = input("Cidade onde atende: ")
    restricoes = input("Restrições que atende (separadas por vírgula): ")
    
    profissional = {
        'nome': nome,
        'especialidade': especialidade,
        'cidade': cidade,
        'restricoes': [r.strip().lower() for r in restricoes.split(',')]
    }
    
    return profissional

#buscar profissionais
def buscar_profissionais(profissionais, especialidade=None, cidade=None, restricoes=None):
    resultados = profissionais
    
    if especialidade:
        resultados = [p for p in resultados if p['especialidade'].lower() == especialidade.lower()]
    
    if cidade:
        resultados = [p for p in resultados if p['cidade'].lower() == cidade.lower()]
    
    if restricoes:
        restricoes = [r.lower() for r in restricoes]
        resultados = [p for p in resultados if all(r in p['restricoes'] for r in restricoes)]
    
    return resultados

#Usuario buscando profissionais
print("\nBuscar profissionais:")
especialidade_filtro = input("Qual a especialidade você procura: ")
cidade_filtro = input("Qual cidade que predente marcar a consulta: ")
restricoes_filtro = input("Qual sua restrição alimentar: ").split

resultados_busca = buscar_profissionais(profissionais, especialidade=especialidade_filtro, cidade=cidade_filtro, restricoes=restricoes_filtro)

# Exibir resultados da busca
if resultados_busca:
    print("\nProfissionais encontrados:")
    for profissional in resultados_busca:
        print(f"Nome: {profissional['nome']}")
        print(f"Especialidade: {profissional['especialidade']}")
        print(f"Cidade: {profissional['cidade']}")
        print(f"Restrições: {', '.join(profissional['restricoes'])}")
else:
    print("Nenhum profissional encontrado com os filtros especificados.")
