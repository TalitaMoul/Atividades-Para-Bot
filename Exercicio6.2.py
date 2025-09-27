"""Exercício 6.2: Simule uma situação onde seu bot tenta acessar uma configuração que pode
não existir em um dicionário. Crie um dicionário config = {"token": "abc", "prefixo": "!"} . Tente
acessar a chave "canal_logs" usando try-except para capturar um KeyError e imprima "A
chave 'canal_logs' não foi encontrada nas configurações."""

# Crie um dicionário config
config = {"token":"abc", "prefixo":"!"}

# Tente acessar a chave "canal_logs" usando try-except para capturar um KeyError

def comandos_bot(msg_bot): # type: ignore

    try:
        config[msg_bot]

# imprima "A chave 'canal_logs' não foi encontrada nas configurações."

    except KeyError:
        print(f"A chave {msg_bot} não foi encontrada nas configurações")


comandos_bot("canal_logs")
            