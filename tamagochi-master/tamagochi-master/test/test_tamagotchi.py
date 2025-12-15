import unittest

from src.tamagotchi import Tamagotchi


class TestTamagotchi(unittest.TestCase):

    def testInicializacao(self):
        tamagotchi = Tamagotchi(20, 10, 15, 30)

        self.assertEqual(20, tamagotchi.getEnergiaMax(),
                         "Ao inicializar um tamagotchi, a energia maxima tem que ser igual ao informado no construtor.")
        self.assertEqual(20, tamagotchi.getEnergiaAtual(),
                         "Ao inicializar um tamagotchi, a energia atual deve ser igual a energia maxima informado no construtor.")
        self.assertEqual(10, tamagotchi.getSaciedadeMax(),
                         "Ao inicializar um tamagotchi, a saciedade maxima tem que ser igual ao informado no construtor.")
        self.assertEqual(10, tamagotchi.getSaciedadeAtual(),
                         "Ao inicializar um tamagotchi, a saciedade atual deve ser igual a saciedade maxima informado no construtor.")
        self.assertEqual(15, tamagotchi.getLimpezaMax(),
                         "Ao inicializar um tamagotchi, a limpeza maxima deve ser igual ao informado no construtor.")
        self.assertEqual(15, tamagotchi.getLimpezaAtual(),
                         "Ao inicializar um tamagotchi, a limpeza atual deve ser igual a limpeza maxima informado no construtor.")
        self.assertEqual(30, tamagotchi.getIdadeMax(),
                         "Ao inicializar um tamagotchi, a idade maxima deve ser igual ao informado no construtor.")
        self.assertEqual(0, tamagotchi.getIdadeAtual(),
                         "Ao inicializar um tamagotchi, a idade atual deve ser igual a 0.")
        self.assertEqual(0, tamagotchi.getDiamantes(),
                         "Ao inicializar um tamagotchi, a quantidade de diamantes deve ser igual a 0.")
        self.assertTrue(tamagotchi.getEstaVivo(),
                        "Ao inicializar um tamagotchi, esta Vivo deve ser igual a true.")

    def testBrincandoEAlterandoValores(self):
        tamagotchi = Tamagotchi(20, 10, 15, 30)
        self.assertTrue(tamagotchi.brincar(),
                        "Deve ser possivel o tamagotchi brinca se ele nao tiver morrido.")
        self.assertEqual(18, tamagotchi.getEnergiaAtual(),
                         "Ao brincar, o tamagotchi gastara 2 pontos de energia")
        self.assertEqual(9, tamagotchi.getSaciedadeAtual(),
                         "Ao brincar, o tamagotchi gastara 1 ponto de saciedade")
        self.assertEqual(12, tamagotchi.getLimpezaAtual(),
                         "Ao brincar, o tamagotchi gastara 3 pontos de limpeza")
        self.assertEqual(1, tamagotchi.getDiamantes(),
                         "Ao brincar, o tamagotchi ganhara 1 diamante.")
        self.assertEqual(1, tamagotchi.getIdadeAtual(),
                         "Ao brincar, o tamagotchi aumentara a idade em 1.")

    def testComerAlterandoValores(self):
        tamagotchi = Tamagotchi(20, 10, 15, 30)

        self.assertTrue(tamagotchi.brincar(),
                        "Deve ser possivel o tamagotchi brinca se ele nao tiver morrido.")
        self.assertTrue(tamagotchi.comer(),
                        "Deve ser possivel o tamagotchi comer se ele nao tiver morrido.")
        self.assertEqual(17, tamagotchi.getEnergiaAtual(),
                         "Ao comer, o tamagotchi gastara 1 ponto de energia")
        self.assertEqual(10, tamagotchi.getSaciedadeAtual(),
                         "Ao comer, o tamagotchi ganhara 4 pontos de saciedade")
        self.assertEqual(10, tamagotchi.getLimpezaAtual(),
                         "Ao comer, o tamagotchi gastara 2 pontos de limpeza")
        self.assertEqual(1, tamagotchi.getDiamantes(),
                         "Ao comer, o tamagotchi nao ganhara nenhum diamante.")
        self.assertEqual(2, tamagotchi.getIdadeAtual(),
                         "Ao comer, o tamagotchi aumentara a idade em 1.")

    def testConsegueDormirComEnergiaLimite(self):
        tamagotchi = Tamagotchi(20, 10, 15, 30)

        self.assertTrue(tamagotchi.brincar(),
                        "Deve ser possivel o tamagotchi brinca se ele nao tiver morrido.")
        self.assertTrue(tamagotchi.comer(),
                        "Deve ser possivel o tamagotchi comer se ele nao tiver morrido.")
        tamagotchi.brincar()
        self.assertTrue(tamagotchi.dormir(),
                        "Deve ser possivel o tamagotchi dormir se ele nao tiver morrido ou tiver perdido exatamente 5 pontos de energia.")

    def testNaoConsegueDormir(self):
        tamagotchi = Tamagotchi(20, 10, 15, 30)

        self.assertTrue(tamagotchi.brincar(),
                        "Deve ser possivel o tamagotchi brinca se ele nao tiver morrido.")
        self.assertTrue(tamagotchi.comer(),
                        "Deve ser possivel o tamagotchi comer se ele nao tiver morrido.")
        self.assertFalse(tamagotchi.dormir(),
                         "nao deve ser possivel o tamagotchi dormir se ele nao tiver perdido pelo menos 5 pontos de energia.")

    def testDormirAlterandoValores(self):
        tamagotchi = Tamagotchi(20, 10, 15, 30)
        self.assertTrue(tamagotchi.brincar(),
                        "Deve ser possivel o tamagotchi brinca se ele nao tiver morrido.")
        self.assertTrue(tamagotchi.comer(),
                        "Deve ser possivel o tamagotchi comer se ele nao tiver morrido.")
        tamagotchi.brincar()
        tamagotchi.brincar()

        self.assertTrue(tamagotchi.dormir(),
                        "Deve ser possivel o tamagotchi dormir se ele tiver perdido pelo menos 5 pontos de energia.")
        self.assertEqual(20, tamagotchi.getEnergiaAtual(),
                         "Ao dormir, o tamagotchi ganhara a energia maxima que ele pode ter.")
        self.assertEqual(6, tamagotchi.getSaciedadeAtual(),
                         "Ao dormir, o tamagotchi perdera 2 pontos de saciedade")
        self.assertEqual(4, tamagotchi.getLimpezaAtual(),
                         "Ao dormir, a limpeza do tamagotchi nao mudara.")
        self.assertEqual(3, tamagotchi.getDiamantes(),
                         "Ao dormir, os diamantes do tamagotchi nao mudara.")
        self.assertEqual(11, tamagotchi.getIdadeAtual(),
                         "Ao dormir, o tamagotchi aumetara sua idade equivalente ao número de turnos que ele dormiu para recuperar sua energia maxima.")

    def testBanharAlterandoValores(self):
        tamagotchi = Tamagotchi(20, 10, 15, 30)
        self.assertTrue(tamagotchi.brincar(),
                        "Deve ser possivel o tamagotchi brinca se ele nao tiver morrido.")
        tamagotchi.brincar()
        self.assertTrue(tamagotchi.comer(),
                        "Deve ser possivel o tamagotchi comer se ele nao tiver morrido.")
        tamagotchi.brincar()
        self.assertTrue(tamagotchi.banhar(),
                        "Deve ser possivel o tamagotchi banhar se ele nao tiver morrido.")
        self.assertEqual(10, tamagotchi.getEnergiaAtual(),
                         "Ao banhar, o tamagotchi perdera 3 pontos de energia.")
        self.assertEqual(8, tamagotchi.getSaciedadeAtual(),
                         "Ao banhar, o tamagotchi perdera 1 pontos de saciedade")
        self.assertEqual(15, tamagotchi.getLimpezaAtual(),
                         "Ao banhar, o tamagotchi ganhara a limpeza maxima que ele pode ter.")
        self.assertEqual(3, tamagotchi.getDiamantes(),
                         "Ao banhar, os diamantes do tamagotchi nao mudara.")
        self.assertEqual(6, tamagotchi.getIdadeAtual(),
                         "Ao banhar, o tamagotchi aumetara sua idade em 2.")

    def testTamagotchiMorreuSemEnergia(self):
        tamagotchi = Tamagotchi(5, 10, 15, 30)
        self.assertTrue(tamagotchi.brincar(),
                        "Deve ser possivel o tamagotchi brinca se ele nao tiver morrido.")
        tamagotchi.brincar()
        tamagotchi.brincar()
        self.assertFalse(tamagotchi.dormir(),
                         "nao deve ser possivel dormir se o tamagotchi morreu.")
        self.assertFalse(tamagotchi.getEstaVivo(),
                         "Quando a energia atual do tamagotchi chega em 0, ele acaba morrendo sem energia.")
        self.assertEqual(0, tamagotchi.getEnergiaAtual(),
                         "Quando o tamagotchi morre sem energia, a sua energia atual fica zerada.")

    def testTamagotchiMorreuDeFome(self):
        tamagotchi = Tamagotchi(20, 5, 15, 30)
        self.assertTrue(tamagotchi.brincar(), "Deve ser possivel o tamagotchi brinca se ele nao tiver morrido.")
        tamagotchi.brincar()
        tamagotchi.brincar()
        self.assertTrue(tamagotchi.dormir(),
                        "Deve ser possivel o tamagotchi dormir se ele tiver perdido pelo menos 5 pontos de energia.")
        self.assertFalse(tamagotchi.comer(), "nao deve ser possivel comer se o tamagotchi morreu.")
        self.assertFalse(tamagotchi.getEstaVivo(),
                         "Quando a saciedade atual do tamagotchi chega em 0, ele acaba morrendo de fome")
        self.assertEqual(0, tamagotchi.getSaciedadeAtual(),
                         "Quando o tamagotchi morre de fome, a sua fome atual fica zerada.")

    def testTamagotchiMorreuSujo(self):
        tamagotchi = Tamagotchi(20, 10, 5, 30)
        self.assertTrue(tamagotchi.brincar(),
                        "Deve ser possivel o tamagotchi brinca se ele nao tiver morrido.")
        tamagotchi.brincar()
        self.assertFalse(tamagotchi.banhar(),
                         "nao deve ser possivel banhar se o tamagotchi morreu.")
        self.assertFalse(tamagotchi.getEstaVivo(),
                         "Quando a limpeza atual do tamagotchi chega em 0, ele acaba morrendo de sujeira.")
        self.assertEqual(0, tamagotchi.getLimpezaAtual(),
                         "Quando o tamagotchi morre de sujeira, a sua limpeza atual fica zerada.")

    def testTamagotchiMorreuDeVelhice(self):
        tamagotchi = Tamagotchi(20, 10, 15, 10)
        self.assertTrue(tamagotchi.brincar(),
                        "Deve ser possivel o tamagotchi brinca se ele nao tiver morrido.")
        tamagotchi.brincar()
        tamagotchi.brincar()
        self.assertTrue(tamagotchi.dormir(),
                        "Deve ser possivel o tamagotchi dormir se ele tiver perdido pelo menos 5 pontos de energia.")
        self.assertTrue(tamagotchi.banhar(),
                        "Deve ser possivel o tamagotchi banhar se ele nao tiver morrido.")
        self.assertFalse(tamagotchi.getEstaVivo(),
                         "Quando a idade atual ultrapassa a idade maxima, ele acaba morrendo de velhice.")
        self.assertEqual(10, tamagotchi.getIdadeAtual(),
                         "Quando o tamagotchi morre de velhice, a sua idade atual fica igual a idade maxima.")

    def testTamagotchiMorreuENaoPodeFazerAcoes(self):
        tamagotchi = Tamagotchi(4, 10, 15, 10)
        self.assertTrue(tamagotchi.brincar(),
                        "Deve ser possivel o tamagotchi brinca se ele nao tiver morrido.")
        tamagotchi.brincar()
        self.assertFalse(tamagotchi.getEstaVivo(),
                         "Quando a energia atual do tamagotchi chega em 0, ele acaba morrendo sem energia.")
        self.assertFalse(tamagotchi.brincar(),
                         "nao deve ser possivel brincar se o tamagotchi  morreu.")
        self.assertFalse(tamagotchi.banhar(),
                         "nao deve ser possivel banhar se o tamagotchi morreu.")
        self.assertFalse(tamagotchi.comer(),
                         "nao deve ser possivel comer se o tamagotchi morreu.")
        self.assertFalse(tamagotchi.dormir(),
                         "nao deve ser possivel dormir se o tamagotchi morreu.")
        self.assertEqual(0, tamagotchi.getEnergiaAtual(),
                         "Como nao foi possivel fazer mais ações o tamagotchi permanece com a energia atual inalterada.")
        self.assertEqual(8, tamagotchi.getSaciedadeAtual(),
                         "Como nao foi possivel fazer mais ações o tamagotchi permanece com a saciedade atual inalterada.")
        self.assertEqual(9, tamagotchi.getLimpezaAtual(),
                         "Como nao foi possivel fazer mais ações o tamagotchi permanece com a limpeza atual inalterada.")
        self.assertEqual(2, tamagotchi.getDiamantes(),
                         "Como nao foi possivel fazer mais ações o tamagotchi permanece com os diamantes inalterados.")
        self.assertEqual(2, tamagotchi.getIdadeAtual(),
                         "Como nao foi possivel fazer mais ações o tamagotchi permanece com a idade atual inalterada.")


if __name__ == '__main__':
    unittest.main()