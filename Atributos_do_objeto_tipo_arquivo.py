arquivo = open("dados/dados.txt")

print(f'nome do arquivo: {arquivo.name}')
print(f'modo do arquivo: {arquivo.mode}')
print(f'arquivo fechado?: {arquivo.closed}')

arquivo.close()

print(f'arquivo fechado?: {arquivo.closed}')
