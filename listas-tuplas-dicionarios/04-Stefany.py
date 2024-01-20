'''4. Crie um dicionário representando contatos (nome, telefone). Permita ao usuário procurar por um contato pelo nome.'''

# Inicialização do dicionário de contatos
contatos = {"João": "123456789", "Maria": "987654321", "Carlos": "555555555"}

# Busca por um contato pelo nome
nome_busca = input("Digite o nome do contato que deseja buscar: ")
telefone = contatos.get(nome_busca, "Contato não encontrado")

# Impressão do resultado
print(f"Telefone de {nome_busca}: {telefone}")