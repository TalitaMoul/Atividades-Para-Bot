"""Exercício 4.3: Crie uma função enviar_mensagem_privada que recebe usuario e mensagem
como parâmetros. Esta função deve imprimir "Enviando mensagem privada para [usuario]:
[mensagem]". Adicione um parâmetro opcional remetente com valor padrão "Bot". Teste a
função sem e com o remetente ."""

def enviar_mensagem_privada(user: str, msg: str, remetente: str = "Bot"):
    print(f"Enviando mensagem privada para {user}: {msg}")
    print(f"O remetente da mensagem é {remetente}")

enviar_mensagem_privada("Talita", "A Talita adora doces.", "Marcello")
enviar_mensagem_privada("Marcello", "O Marcello vai sair com o Bigode e o Bento.")
    

