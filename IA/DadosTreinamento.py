from Util.SingletonConnection import Connection
import pandas as pd

def DadosPlantas():
    plantas = Connection("PlantasTreinamento").find()
    dfPlantas = pd.DataFrame(data=list(plantas))
    y = dfPlantas.idPlanta
    X = dfPlantas.drop(['Nome', '_id','idPlanta'],axis=1)
    return X,y

def DadosPlantasAumentados():
    dfPlantas = pd.DataFrame(data=list(Connection("PlantasTreinamento").find()))
    DadosAumentados = AumentoRepresentatividade(dfPlantas)
    y = DadosAumentados.idPlanta
    X = DadosAumentados.drop(['idPlanta'],axis=1)

    return X,y

def AumentoRepresentatividade(dados):
    arrayDados = []
    print("Aumentando os dados")
    for line in dados.values:
        for prec in range(int(line[2]),int(line[1])):
            for tem in range(int(line[4]),int(line[3])):
                for umi in range(int(line[6]),int(line[5])):
                    arrayDados.append({'idPlanta':line[8], 'Tem':tem, 'Umi':umi,'Prec':prec})
    print("Dados aumentados")
    dadosAum = pd.DataFrame(data=arrayDados)
    return dadosAum

