"""Exercício 2.4: Acesse e imprima o valor associado à chave "prefixo" no dicionário
configuracoes_servidor ."""

configuracoes_servidor = { # type: ignore
    "prefixo": "!",
    "canal_padrao": "geral",
    "log_erros": True
}

print(f"O valor associado à chave Prefixo é: '{configuracoes_servidor["prefixo"]}'") # type: ignore