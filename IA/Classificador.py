import tensorflow as tf
from tensorflow.feature_column import numeric_column

def Classificador(numPlantas=4):

    TemMin = numeric_column(key='TemMin')
    TemMax = numeric_column(key='TemMax')
    UmMin = numeric_column(key='Umidaderelativamax')
    UmMax = numeric_column(key='Umidaderelativamin')

    colunas = [TemMax, TemMin, UmMax, UmMin]

    classificador = tf.estimator.DNNClassifier(hidden_units=[8, 8, 8],
                                               feature_columns=colunas,
                                               model_dir='MODEL',
                                               n_classes=numPlantas)
    return classificador





"""
def TreinamentoSklearn():
    X_Treinamento, y_Treinamento = DadosPlantas("Plantas")
    NumPlantas = len(y_Treinamento)
    classificador = KNeighborsClassifier(n_neighbors=NumPlantas)
    classificador.fit(X_Treinamento, y_Treinamento)
    return True
"""





