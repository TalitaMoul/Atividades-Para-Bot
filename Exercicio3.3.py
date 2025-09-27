"""Exercício 3.3: Use um loop while para simular um contador regressivo de 5 até 1. A cada
iteração, imprima o número atual. Após o loop, imprima "Lançar!"."""

contador = 5
while contador > 0:
    print(contador)
    if contador == 1:
        print("Lançar!")
    contador -= 1
    
