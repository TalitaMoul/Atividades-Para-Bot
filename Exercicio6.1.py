"""Exercício .: Escreva uma função converter_para_inteiro que recebe uma entrada como
parâmetro. Use try-except para tentar converter a entrada para um número inteiro. Se a
conversão for bem-sucedida, imprima o número. Se ocorrer um ValueError (por exemplo, se
a entrada não for um número), imprima "Erro: Entrada inválida. Por favor, digite um
número.". Teste com "123" e "abc" .
"""

def converter_para_inteiro(ent: str):
    try: #tentativa de conversão
        int_entrada = int(ent)
        print(int_entrada)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
    
# converter_para_inteiro("123")
converter_para_inteiro("abc")