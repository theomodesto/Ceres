from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def EscalonamentoDados(dados):
    scaler = MinMaxScaler()
    Dados = pd.DataFrame(data=scaler.fit_transform(dados), columns=dados.columns )
    return Dados