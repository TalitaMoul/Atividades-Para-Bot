"""Exercício 7.1: Crie uma função assíncrona simular_demora() que imprime "Iniciando
simulação...", espera 3 segundos usando await asyncio.sleep() , e depois imprime
"Simulação concluída!". Use asyncio.run() para executar esta corrotina."""

import asyncio

async def simular_demora():
    print("Iniciando simulação...")
    await asyncio.sleep(3)
    print("Simulação concluída.")

asyncio.run(simular_demora())

    

