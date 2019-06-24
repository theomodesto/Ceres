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

    Dados = GetDadosAPI(32.658317, 3.544376, 2018)
    for key in Dados:
        previsao = Previsao(Dados[key])
        planta = retornaPlantasPorId(previsao['IdPlanta'])
        previsoes.append([planta, previsao['Probabilidade']])
    print(previsoes)