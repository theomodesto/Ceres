from DAL.ConnectionMongoDB import *
import pandas as pd

def DadosPlantasAumentados():
    dfPlantas = pd.DataFrame(data=list(Connection("PlantasTreinamento").find().clone()))
    DadosAumentados = AumentoRepresentatividade(dfPlantas)
    y = DadosAumentados.idPlanta
    X = DadosAumentados.drop(['idPlanta'],axis=1)

    return X,y

def AumentoRepresentatividade(dados):
    arrayDados = []

    print("Aumentando os dados")

    # f = open('output\\DadosAumentadosPlantas.csv', 'w', encoding='utf8')
    # header = "idPlanta,Tem,Umi,Prec\n"
    # f.write(header)
    for line in dados.values:
        for prec in range(int(line[2]),int(line[1])):
            for tem in range(int(line[4]),int(line[3])):
                for umi in range(int(line[6]),int(line[5])):
                    # f.write(str(line[8])+','+str(tem)+','+str(umi)+','+str(prec)+'\n')
                    arrayDados.append({'idPlanta':line[8], 'Tem':tem, 'Umi':umi,'Prec':prec})
                    # f.flush()
    # f.close()
    print("Dados aumentados")
    print("Media PreciMin : 162")

    dadosAum = pd.DataFrame(data=arrayDados)
    return dadosAum
