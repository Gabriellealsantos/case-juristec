class Televisao:
    """Representa uma televisao com controle de canal, volume e modo mudo."""

    def __init__(self, canal_inicial: int = 1, volume_inicial: int = 10):
        """Inicializa a televisao com canal e volume padrao."""
        self.canal = canal_inicial
        self.volume = volume_inicial
        self.mudo = False
        self.volume_antes_do_mudo = volume_inicial

    def alterar_canal(self, novo_canal: int) -> None:
        """Altera o canal da TV, validando se é um canal positivo."""
        if novo_canal > 0:
            self.canal = novo_canal
            print(f"Canal alterado para: {self.canal}")
        else:
            print("Canal inválido.")

    def alterar_volume(self, variacao: int) -> None:
        """Ajusta o volume no intervalo de 0 a 100."""
        if self.mudo:
            self.alternar_mudo()

        novo_volume = self.volume + variacao

        if novo_volume < 0:
            self.volume = 0
        elif novo_volume > 100:
            self.volume = 100
        else:
            self.volume = novo_volume

        print(f"Volume atual: {self.volume}")

    def alternar_mudo(self) -> None:
        """Ativa ou desativa a função mudo."""
        if not self.mudo:
            self.volume_antes_do_mudo = self.volume
            self.volume = 0
            self.mudo = True
            print("Mudo: ATIVADO")
        else:
            self.volume = self.volume_antes_do_mudo
            self.mudo = False
            print(f"Mudo: DESATIVADO. Volume restaurado para: {self.volume}")

if __name__ == "__main__":
    tv = Televisao()

    tv.alterar_canal(5)
    tv.alterar_volume(5)
    tv.alternar_mudo()
    tv.alternar_mudo()
