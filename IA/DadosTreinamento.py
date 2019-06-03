from UTIL.SingletonConnection import Connection
import pandas as pd

def DadosPlantas(Collection):
    plantas = Connection(Collection).find()
    dfPlantas = pd.DataFrame(data=list(plantas))
    y = dfPlantas.idPlanta
    # y = dfPlantas.Nome
    X = dfPlantas.drop(['Nome', '_id','idPlanta'],axis=1)
    return X,y
