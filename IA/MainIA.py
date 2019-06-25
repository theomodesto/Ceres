from IA.Treinamento import *
from IA.Teste import *
from IA.Previsao import *
from Util.PowerLarcAPI import *
from DAL.PlantasDAO import *

if __name__ == '__main__':
    # Treinamento()
    # TreinamentoSklearn()

    # Teste()
    # TesteSklearn()

    previsoes = []

    Dados = GetDadosAPI(-25.288230, -49.463606, 2018)
    for key in Dados:
        previsao = Previsao(Dados[key],key)
        for prev in previsao:
            planta = retornaPlantasPorId(prev['IdPlanta'])
            print(prev['IdPlanta'], prev['Probabilidade'],key)
            previsoes.append([planta, prev['Probabilidade'],key])
    print(previsoes)