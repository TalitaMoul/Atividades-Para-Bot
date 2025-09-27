"""Exercicio 2.1: Crie uma lista chamada comandos_disponiveis com os seguintes comandos:
"ping", "info", "kick", "ban". Adicione o comando "clear" a essa lista. Em seguida, remova o
comando "kick". Imprima a lista final."""

comandos_possiveis = ["ping", "info", "kick", "ban"]
print(comandos_possiveis)

comandos_possiveis.append("clear")
print(comandos_possiveis)

comandos_possiveis.remove("kick")
print(comandos_possiveis)

