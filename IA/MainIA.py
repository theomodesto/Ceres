from IA.Treinamento import *
from IA.Teste import *
from IA.Previsao import *
from Util.PowerLarcAPI import *


if __name__ == '__main__':
    # Treinamento()
    # TreinamentoSklearn()

    # Teste()
    # TesteSklearn()

    dadosClima = GetDadosAPI(32.658317, 3.544376, 2018)

    for key in dadosClima:
        print(key)
        Previsao(dadosClima[key])
        # print(dadosClima[key])