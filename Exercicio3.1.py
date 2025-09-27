"""Exercício 3.1: Escreva um código que simule a verificação de um comando. Se a variável
comando_digitado for "!status", imprima "Bot online e funcionando!". Se for "!ajuda",
imprima "Use !ping para testar a conexão.". Caso contrário, imprima "Comando
desconhecido.". Teste com comando_digitado = "!status" , comando_digitado = "!ajuda" e
comando_digitado = "!qualquercoisa" ."""


comando_digitado = "!status"  
comando_digitado = "!ajuda" 
comando_digitado = "!ping"

if comando_digitado == "!status": # type: ignore
    print("Bot online e funcionando!")
elif comando_digitado == "!ajuda": # type: ignore
    print("Use '!ping' para testar a conexão.")
elif comando_digitado == "!ping":
    print("A conexão está ativa!")
else:
    print("Comando desconhecido.")
