"""Exercício 7.2: Imagine que seu bot tem um comando !contar . Crie uma função assíncrona
comando_contar(ctx, numero) que recebe um número. Dentro dela, use um loop for para
contar de 1 até o numero , e a cada contagem, use await asyncio.sleep(1) para simular um
atraso. Imprima o número atual a cada segundo. (Não precisa rodar um bot completo,
apenas a função)."""
import asyncio

async def comando_contar(numero): # type: ignore
    for n in range(numero): # type: ignore
        await asyncio.sleep(1)
        print(n + 1)

asyncio.run(comando_contar(16))

    
