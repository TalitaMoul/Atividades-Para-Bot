"""Exercício 5.1: Baseado na classe UsuarioDiscord do documento, crie uma nova classe
CanalDiscord que tenha atributos nome_canal e id_canal . Adicione um método
enviar_mensagem_canal que recebe mensagem e imprime "[nome_canal]: [mensagem]". Crie
um objeto CanalDiscord e use o método."""

class CanalDiscord:
    def __init__(self, nome_canal: str, id_canal: int):
        self.nome = nome_canal
        self.id = id_canal
    
    def enviar_mensagem_canal(self, msg: str):
        print(f"{self.nome}: {msg}")

CanalDiscordObj = CanalDiscord("Bozo", 33244) # type: ignore
CanalDiscordObj.enviar_mensagem_canal("Pedrinho não consegue ser paquita.. ele quer ser a Xuxa!") # type: ignore

    