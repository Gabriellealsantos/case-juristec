# q2_televisao.py

class Televisao:

    def __init__(self, canal_inicial: int = 1, volume_inicial: int = 10):
        self.canal = canal_inicial
        self.volume = volume_inicial
        self.mudo = False
        self.volume_antes_do_mudo = volume_inicial # Guarda o volume para restaurar depois

    def alterar_canal(self, novo_canal: int) -> None:
        """Altera o canal da TV, validando se é um canal positivo."""
        if novo_canal > 0:
            self.canal = novo_canal
            print(f"Canal alterado para: {self.canal}")
        else:
            print("Canal inválido.")

    def alterar_volume(self, variacao: int) -> None:
        """
        Aumenta ou diminui o volume.
        Exemplo: alterar_volume(5) aumenta 5. alterar_volume(-3) diminui 3.
        """
        # Se estiver no mudo e o volume for alterado, tiramos do mudo
        if self.mudo:
            self.alternar_mudo()

        novo_volume = self.volume + variacao

        # Garantindo que o volume não fique negativo ou passe de 100
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
            # Ativando o mudo
            self.volume_antes_do_mudo = self.volume
            self.volume = 0
            self.mudo = True
            print("Mudo: ATIVADO")
        else:
            # Desativando o mudo e restaurando o volume
            self.volume = self.volume_antes_do_mudo
            self.mudo = False
            print(f"Mudo: DESATIVADO. Volume restaurado para: {self.volume}")

# ==========================================
# Exemplo de Teste Unitário Simples
# ==========================================
if __name__ == "__main__":
    tv = Televisao()

    tv.alterar_canal(5)
    tv.alterar_volume(5)   # Vai para 15
    tv.alternar_mudo()     # Ativa mudo (volume 0)
    tv.alternar_mudo()     # Desativa mudo (volta para 15)
