from os import path

# para o arquivo dados1.txt

arquivo1 = open("dados/dados1.txt")
arquivo2 = open("C:/Users/Rodri/programação/Aulas estacio/Materia- Desenvolvimento Rápido de Aplicações em "
                "Python/Manipulação de Dados em Arquivos/dados/dados1.txt")

# para o arquivo dados2.txt

arquivo3 = open("dados/dados2.txt")
arquivo4 = open("C:/Users/Rodri/programação/Aulas estacio/Materia- Desenvolvimento Rápido de Aplicações em "
                "Python/Manipulação de Dados em Arquivos/dados/dados2.txt")

print('Arquivo aberto com sucesso!')

print(path.relpath(arquivo1.name))
print(path.abspath(arquivo1.name))

print(arquivo1)
