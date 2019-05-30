from Util.SingletonConnection import Connection
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def DadosPlantas(Collection):
    plantas = Connection(Collection).find()
    dfPlantas = pd.DataFrame(data=list(plantas))
    y = dfPlantas.Nome
    X = dfPlantas.drop(['Nome','_id'],axis=1)
    return X,y
