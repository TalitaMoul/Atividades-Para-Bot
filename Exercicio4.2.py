"""Exercício 4.2: Crie uma função chamada calcular_media que recebe três números como
parâmetros e retorna a média deles. Chame a função com 7, 8, 9 e imprima o resultado."""

def calcular_media(n1: int, n2: int, n3: int):
    media = (n1 + n2 + n3) / 3
    return media

print(f"A média é: {calcular_media(4, 2, 6)}")


