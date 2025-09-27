"""Exercício 8.1: Crie um decorador simples chamado log_execucao que imprime "Função
[nome_da_funcao] foi chamada." antes de executar a função decorada e "Função
[nome_da_funcao] finalizada." depois. Aplique este decorador a uma função minha_tarefa()
que apenas imprime "Executando minha tarefa..."""

def log_execucao(funcao_original): # type: ignore
    # A função interna 'wrapper' é o que "embrulha" a original.
    def wrapper():
        print("A função 'minha_tarefa' foi chamada.")
        # Aqui chamamos a função que foi "embrulhada"
        funcao_original()
        print("A função 'minha_tarefa' foi finalizada.")
    # O decorador retorna a função 'wrapper'
    return wrapper

@log_execucao
def minha_tarefa():
    print("Executando minha tarefa...")

minha_tarefa()

