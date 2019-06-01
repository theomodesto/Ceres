from DAO.PlantasDAO import DadosPlantas

import tensorflow as tf
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from tensorflow._api.v1.feature_column import numeric_column


"""
Treinamento usado para criar novo modelo para classificação das plantas
rodar toda vez que alguma planta for adicionada ao modelo  
:param 
"""
def Treinamento():

    X_Treinamento, y_Treinamento = DadosPlantas("Plantas")
    NumPlantas = len(y_Treinamento)

    # LabelEncode categorica para numerica
    labEnco = LabelEncoder()
    # y_Treinamento_enc = pd.DataFrame(data=labEnco.fit_transform(y_Treinamento))

    y_Treinamento = y_Treinamento.idPlanta



    TemMin = numeric_column(key='TemMin')
    TemMax = numeric_column(key='TemMax')
    UmMin = numeric_column(key='Umidaderelativamax')
    UmMax = numeric_column(key='Umidaderelativamin')

    colunas = [TemMax, TemMin, UmMax, UmMin]

    funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x=X_Treinamento,
                                                             y=y_Treinamento,
                                                             batch_size=1,
                                                             num_epochs=None,
                                                             shuffle=False)

    classificador = tf.estimator.DNNClassifier(hidden_units=[8, 8, 8],
                                               feature_columns=colunas,
                                               model_dir='modelTrained',
                                               n_classes=NumPlantas)

    classificador.train(input_fn=funcao_treinamento, steps=10000)

    return True


"""
def TreinamentoSklearn():
    X_Treinamento, y_Treinamento = DadosPlantas("Plantas")
    NumPlantas = len(y_Treinamento)
    classificador = KNeighborsClassifier(n_neighbors=NumPlantas)
    classificador.fit(X_Treinamento, y_Treinamento)
    return True
"""



