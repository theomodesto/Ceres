from UTIL.SingletonConnection import Connection
import pandas as pd

# def DadosPlantas():
#     plantas = Connection("DadosTreinamento").find()
#     dfPlantas = pd.DataFrame(data=list(plantas))
#     print(teste.head(200))
#     y = dfPlantas.idPlanta
#     # y = dfPlantas.Nome
#     X = dfPlantas.drop(['Nome', '_id','idPlanta'],axis=1)
#
#     return X,y

def DadosPlantas():
    plantas = Connection("DadosTreinamento").find()
    dfPlantas = pd.DataFrame(data=list(plantas))
    DadosAumentados = AumentoRepresentatividade(dfPlantas)
    y = DadosAumentados.idPlanta
    X = DadosAumentados.drop(['idPlanta'],axis=1)

    return X,y

def AumentoRepresentatividade(dados):
    arrayDados = []
    # print(dados.info())
    for line in dados.values:
        for tem in range(line[2],line[1]):
            for umi in range(line[4],line[3]):
                arrayDados.append({'idPlanta':line[6],'Tem':tem,'Umi':umi})
    dadosAum = pd.DataFrame(data=arrayDados)
    return dadosAum
