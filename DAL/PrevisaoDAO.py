from datetime import datetime
from Util.PowerLarcAPI import *
from IA.Previsao import *
from DAL.PlantasDAO import *

def previsaoFinal(lat,lon):
    previsoes = []
    ano = ((datetime.now().year) - 1)
    Dados = GetDadosAPI(lat, lon, ano)
    for key in Dados:
        previsao = Previsao(Dados[key])
        for prev in previsao:
            print(prev, key)
            planta = retornaPlantasPorId(prev['IdPlanta'])
            previsoes.append([planta, int(prev['Probabilidade']), key.lower()])
    return previsoes