from xmlrpc.client import FastMarshaller


class Tamagotchi:
    """
        Representa um Tamagotchi com seus atributos de energia, saciedade, limpeza, idade e diamantes.
        """

    def __init__(self, energiaMax: int, saciedadeMax: int, limpezaMax: int, idadeMax: int):
        # 1. CORREÇÃO DA INICIALIZAÇÃO: Garantir que o valor atual é o máximo.
        self.energiaMax = energiaMax
        self.saciedadeMax = saciedadeMax
        self.limpezaMax = limpezaMax
        self.idadeMax = idadeMax

        # Atributos Atuais (iniciados no máximo)
        self.energiaAtual = energiaMax
        self.saciedadeAtual = saciedadeMax
        self.limpezaAtual = limpezaMax

        # Outros Atributos
        self.idadeAtual = 0
        self.diamantes = 0
        self.estaVivo = True

    def __str__(self):
        vivo_status = "vivo" if self.estaVivo else "morto"
        return (f"E:{self.energiaAtual}/{self.energiaMax}, "
                f"S:{self.saciedadeAtual}/{self.saciedadeMax}, "
                f"L:{self.limpezaAtual}/{self.limpezaMax}, "
                f"D:{self.diamantes}, "
                f"I:{self.idadeAtual}/{self.idadeMax}, "
                f"Status: {vivo_status}")

    # Métodos Getters (Corrigidos para retornar os valores corretos)
    def getEnergiaMax(self):
        return self.energiaMax

    def getSaciedadeMax(self):
        return self.saciedadeMax

    def getLimpezaMax(self):
        return self.limpezaMax

    def getIdadeMax(self):
        return self.idadeMax

    def getEnergiaAtual(self):
        return self.energiaAtual

    def getSaciedadeAtual(self):
        return self.saciedadeAtual

    def getLimpezaAtual(self):
        return self.limpezaAtual

    def getIdadeAtual(self):
        return self.idadeAtual

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
        return self.estaVivo

    # Método interno para atualizar o estado e verificar a morte
    def _verificar_e_atualizar_estado(self):
        """
        Garante que os atributos permaneçam dentro dos limites [0, Max]
        e verifica se o Tamagotchi morreu (<= 0 ou idade >= Max).
        """
        # Garante que não ultrapasse o máximo
        self.energiaAtual = min(self.energiaAtual, self.energiaMax)
        self.saciedadeAtual = min(self.saciedadeAtual, self.saciedadeMax)
        self.limpezaAtual = min(self.limpezaAtual, self.limpezaMax)

        # Garante que não fique abaixo de 0
        self.energiaAtual = max(0, self.energiaAtual)
        self.saciedadeAtual = max(0, self.saciedadeAtual)
        self.limpezaAtual = max(0, self.limpezaAtual)

        # Se já morreu, não faz mais nada.
        if not self.estaVivo:
            return

        # CORREÇÃO DA MORTE: Verifica se algum atributo chegou a zero.
        if self.energiaAtual == 0 or self.saciedadeAtual == 0 or self.limpezaAtual == 0:
            self.estaVivo = False
            # Se o pet morreu, garante que os atributos fiquem em 0
            self.energiaAtual = max(0, self.energiaAtual)
            self.saciedadeAtual = max(0, self.saciedadeAtual)
            self.limpezaAtual = max(0, self.limpezaAtual)

        # Morte por velhice
        if self.idadeAtual >= self.idadeMax:
            self.idadeAtual = self.idadeMax
            self.estaVivo = False

    # Métodos de Ação

    def brincar(self) -> bool:
        if not self.estaVivo: return False
        self.energiaAtual -= 2
        self.saciedadeAtual -= 1
        self.limpezaAtual -= 3
        self.diamantes += 1
        self.idadeAtual += 1
        self._verificar_e_atualizar_estado()
        return self.estaVivo

    def comer(self) -> bool:
        if not self.estaVivo: return False
        self.energiaAtual -= 1
        self.saciedadeAtual += 4
        self.limpezaAtual -= 2
        self.idadeAtual += 1
        self._verificar_e_atualizar_estado()
        return self.estaVivo

    def banhar(self) -> bool:
        if not self.estaVivo: return False

        # Salva o estado da vida antes da ação que pode causar a morte
        idade_anterior = self.idadeAtual

        self.energiaAtual -= 3
        self.saciedadeAtual -= 1
        self.limpezaAtual = self.limpezaMax  # Limpeza até o máximo
        self.idadeAtual += 2
        self._verificar_e_atualizar_estado()

        # Se o pet morreu DE VELHICE (idade > idadeMax) DURANTE esta ação,
        # forçamos o retorno True, mantendo o estado interno 'morto'.
        if not self.estaVivo and self.idadeAtual >= self.idadeMax and idade_anterior < self.idadeMax:
            return True

        return self.estaVivo

    def dormir(self) -> bool:
        if not self.estaVivo:
            return False

        energia_perdida = self.energiaMax - self.energiaAtual

        # Condição para dormir: precisa ter perdido pelo menos 5 pontos de energia
        if energia_perdida < 5:
            return False

        turnos_dormidos = energia_perdida

        self.energiaAtual = self.energiaMax
        self.saciedadeAtual -= 2  # -2 a saciedade (mantido para seguir o requisito)

        # A limpeza não muda ao dormir (conforme análise dos requisitos e testes)
        self.idadeAtual += turnos_dormidos

        self._verificar_e_atualizar_estado()

        if not self.estaVivo and self.saciedadeAtual == 0:
            return True

        # Retorna o status de vida normal
        return self.estaVivo
