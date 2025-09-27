"""Exercício 5.2: Crie uma classe ModeradorDiscord que herda de UsuarioDiscord . A classe
ModeradorDiscord deve ter um atributo adicional permissoes_moderacao (uma lista de
strings, ex: ["kick", "mute"] ). Adicione um método aplicar_mute que recebe um usuario_alvo
e imprime "[NomeDoModerador] aplicou mute em [NomeDoUsuarioAlvo]". Crie um objeto
ModeradorDiscord e teste o método."""

class UsuarioDiscord:
    def __init__(self, nome_usuario): # type: ignore
        self.nome = nome_usuario

    def enviar_mensagem(self, msg: str):
        print(f"{self.nome} disse a mensagem: {msg}")

class ModeradorDiscord(UsuarioDiscord):
    def __init__(self, nome_usuario, permissoes_moderacao = ["kick", "mute"]): # type: ignore
        super().__init__(nome_usuario) # type: ignore
        self.permissoes = permissoes_moderacao # type: ignore

    def aplicar_mute(self, usuario_alvo): # type: ignore
        print(f"{self.nome} aplicou mute em {usuario_alvo.nome}") # type: ignore

usuario_discord = UsuarioDiscord("Talita")
moderador_discord = ModeradorDiscord("Marcello")
usuario_discord2 = UsuarioDiscord("Grilhonildo")


moderador_discord.aplicar_mute(usuario_discord2) # type: ignore
usuario_discord2.enviar_mensagem("O Pedrinho não sabe ser Paquita.")
moderador_discord.enviar_mensagem("Feed tático.")
usuario_discord.enviar_mensagem("Mamado")


