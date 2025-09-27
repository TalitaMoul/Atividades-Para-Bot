"""Exercício2.3: Crie um dicionário chamado configuracoes_servidor com as seguintes chaves e
valores:
- "prefixo" : "!"
- "canal_padrao" : "geral"
- "log_erros" : True

Adicione uma nova chave "idioma" com o valor "pt-br" a este dicionário. Imprima o
dicionário completo."""


configuracoes_servidor = { # type: ignore
    "prefixo": "!",
    "canal_padrao": "geral",
    "log_erros": True
}

configuracoes_servidor["idioma"] = "pt-BR"
print(configuracoes_servidor) # type: ignore