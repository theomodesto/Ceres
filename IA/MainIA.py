from IA.Treinamento import *
from IA.Teste import *
from IA.Previsao import *
from Util.PowerLarcAPI import *
from DAL.PlantasDAO import *
from datetime import datetime


if __name__ == '__main__':
    # Treinamento()
    # TreinamentoSklearn()

    # Teste()
    # TesteSklearn()

    previsoes = []

    ano = ((datetime.now().year)-1)

    Dados = GetDadosAPI(-25.288230, -49.463606, ano)
    print(Dados)
    for key in Dados:
        previsao = Previsao(Dados[key])
        for prev in previsao:
            planta = retornaPlantasPorId(prev['IdPlanta'])
            previsoes.append([planta, prev['Probabilidade'],key.lower()])

    for planta,probabilidade,estacao in previsoes:
        print(planta)
        print(probabilidade)
        print(estacao)
