import json
import random

# Função que carrega dados de um arquivo JSON
def load_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        return json.load(file)

# Carrega os dados dos membros do núcleo
membros_data = load_arquivo('./data/membros.json')

# Carrega os dados dos candidatos a Lobo
candidatos_data = load_arquivo('./data/candidatos.json')

# Lista de nomes de membros do NATI
nomes_membros = [item['name'] for item in membros_data]

# Lista de nomes de candidatos
nomes_candidatos = [item['name'] for item in candidatos_data]

# Embaralha a lista de membros
random.shuffle(nomes_membros)

# Espalha os candidatos entre os membros
print("Distribuição de Candidatos para Membros:")
print("---------------------------------------")
for candidato in nomes_candidatos:
    membro = random.choice(nomes_membros)
    print(f"Membro: {membro}\t- Candidato: {candidato}")
