from Util.SingletonConnection import Connection
import pandas as pd

def DadosPlantas():
    plantas = Connection("DadosTreinamento").find()
    dfPlantas = pd.DataFrame(data=list(plantas))
    y = dfPlantas.idPlanta
    X = dfPlantas.drop(['Nome', '_id','idPlanta'],axis=1)
    return X,y

def DadosPlantasAumentados():
    dfPlantas = pd.DataFrame(data=list(Connection("DadosTreinamento").find()))
    DadosAumentados = AumentoRepresentatividade(dfPlantas)
    y = DadosAumentados.idPlanta
    X = DadosAumentados.drop(['idPlanta'],axis=1)

    return X,y

def AumentoRepresentatividade(dados):
    arrayDados = []
    for line in dados.values:
        for tem in range(line[2],line[1]):
            for umi in range(line[4],line[3]):
                arrayDados.append({'idPlanta':line[6], 'Tem':tem, 'Umi':umi})
    dadosAum = pd.DataFrame(data=arrayDados)
    return dadosAum


