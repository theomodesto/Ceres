from DAO.PlantasDAO import DadosPlantas

import tensorflow as tf
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from tensorflow._api.v1.feature_column import numeric_column

global numPlantas

def Classificador(numPlantas=4):

    TemMin = numeric_column(key='TemMin')
    TemMax = numeric_column(key='TemMax')
    UmMin = numeric_column(key='Umidaderelativamax')
    UmMax = numeric_column(key='Umidaderelativamin')

    colunas = [TemMax, TemMin, UmMax, UmMin]

    classificador = tf.estimator.DNNClassifier(hidden_units=[8, 8, 8],
                                               feature_columns=colunas,
                                               model_dir='modelTrained',
                                               n_classes=numPlantas)
    return classificador

def Treinamento(classificador):

    X_Treinamento, y_Treinamento = DadosPlantas("Plantas")

    # labEnc = LabelEncoder()
    # y_Treinamento = pd.DataFrame(data=labEnc.fit_transform(y_Treinamento))

    funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x=X_Treinamento,
                                                             y=y_Treinamento[0],
                                                             batch_size=1,
                                                             num_epochs=None,
                                                             shuffle=False)

    numPlantas = len(y_Treinamento)

    classificador = Classificador(numPlantas)

    classificador.train(input_fn=funcao_treinamento,
                        steps=10000)

    return True



"""
def TreinamentoSklearn():
    X_Treinamento, y_Treinamento = DadosPlantas("Plantas")
    NumPlantas = len(y_Treinamento)
    classificador = KNeighborsClassifier(n_neighbors=NumPlantas)
    classificador.fit(X_Treinamento, y_Treinamento)
    return True
"""





