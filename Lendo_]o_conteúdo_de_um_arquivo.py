arquivo = open("dados/dados.txt", "r")

# metodo read()
""""
conteudo = arquivo.read()

print(f'tipo do conteudo {type(conteudo)}')
print(f'Conteudo retornado pelo read:')
print(repr(conteudo))
"""

# metodo Read+line()
"""
conteudo = arquivo.readline()

print(f'tipo do conteudo {type(conteudo)}')

print(f'Conteudo retornado pelo readline:')
print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print(f'Proximo Conteudo retornado pelo readline:')
print(repr(proximo_conteudo))
"""

# Metodo Read+line+s()
"""
conteudo = arquivo.readlines()

print(f'tipo do conteudo {type(conteudo)}')

print(f'Conteudo retornado pelo readlines:')
print(repr(conteudo))
"""

arquivo.close()
