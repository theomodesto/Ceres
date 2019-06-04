import tensorflow as tf
from tensorflow.feature_column import numeric_column
from sklearn.neighbors import KNeighborsClassifier

def Classificador_Min_Max(numPlantas=20):

    TemMin = numeric_column(key='TemMin')
    TemMax = numeric_column(key='TemMax')
    UmMin = numeric_column(key='Umidaderelativamax')
    UmMax = numeric_column(key='Umidaderelativamin')

    colunas = [TemMax, TemMin, UmMax, UmMin]

    classificador = tf.estimator.DNNClassifier(hidden_units=[8, 8, 8],
                                               feature_columns=colunas,
                                               model_dir='Model',
                                               n_classes=numPlantas)
    return classificador

def Classificador(numPlantas=20):

    Tem = numeric_column(key='Tem')
    Umi = numeric_column(key='Umi')

    colunas = [Tem,Umi]

    classificador = tf.estimator.DNNClassifier(hidden_units=[8, 8, 8],
                                               feature_columns=colunas,
                                               model_dir='Model',
                                               n_classes=numPlantas)
    return classificador

def ClassificadorSklearn(NumPlantas=20):
    classificador = KNeighborsClassifier(n_neighbors=NumPlantas)
    return classificador






