import json
import random
import string

# Função que carrega dados de um arquivo JSON
def load_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        return json.load(file)

# Carrega os dados dos membros do núcleo
membros_data = load_arquivo('./data/membros.json')

# Carrega os dados dos candidatos a Lobo
candidatos_data = load_arquivo('./data/candidatos.json')

# Função para espalhar candidatos entre as duplas
def espalhar_candidatos(duplas, candidatos):
    duplas_com_candidatos = {}
    candidatos_disponiveis = candidatos.copy()  # Faz uma cópia da lista de candidatos disponíveis
    for dupla in duplas:
        num_candidatos = random.randint(3, 4)
        # Se houver menos candidatos disponíveis do que o número desejado, apenas use todos os candidatos disponíveis
        num_candidatos = min(num_candidatos, len(candidatos_disponiveis))
        candidatos_da_dupla = random.sample(candidatos_disponiveis, num_candidatos)
        duplas_com_candidatos[dupla] = candidatos_da_dupla
        for candidato in candidatos_da_dupla:
            candidatos_disponiveis.remove(candidato)
    return duplas_com_candidatos

# Lista de nomes de membros do NATI
nomes_membros = [item['name'] for item in membros_data]

# Embaralha a lista de nomes de membros
random.shuffle(nomes_membros)

# Cria duplas
duplas = [(nomes_membros[i], nomes_membros[i+1]) for i in range(0, len(nomes_membros), 2)]

# Lista de letras do alfabeto de A a G
letras = list(string.ascii_uppercase)[:7]

# Associa cada dupla a uma letra do alfabeto
duplas_nomeadas = list(zip(letras, duplas))

# Distribui candidatos entre as duplas
duplas_com_candidatos = espalhar_candidatos(duplas_nomeadas, candidatos_data)

# Imprime as duplas com seus respectivos candidatos
print("\t\t\tDuplas & Candidatos:\n\n")
for letra, dupla in duplas_com_candidatos.items():
    print(f"Dupla {letra}:")
    if dupla:
        for candidato in dupla:
            print(f"- {candidato['name']}")
    else:
        print("Não há candidatos para esta dupla.")
