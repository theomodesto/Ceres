import tensorflow as tf
from tensorflow.feature_column import numeric_column
from sklearn.neighbors import KNeighborsClassifier

def Classificador(numPlantas=36):

    TemMin = numeric_column(key='TemMin')
    TemMax = numeric_column(key='TemMax')
    UmMin = numeric_column(key='UmidadeRelativaMin')
    UmMax = numeric_column(key='UmidadeRelativaMax')
    PrecMin = numeric_column(key='PrecipicacaoMin')
    PrecMax = numeric_column(key='PrecipicacaoMax')

    colunas = [TemMax, TemMin, UmMax, UmMin,PrecMin,PrecMax]

    classificador = tf.estimator.DNNClassifier(hidden_units=[8, 8 ],
                                               feature_columns=colunas,
                                               model_dir='Model/tensorflow',
                                               n_classes=numPlantas,
                                               optimizer=tf.train.ProximalAdagradOptimizer(
                                                      learning_rate=0.1,
                                                      l1_regularization_strength=0.001
                                               ))
    return classificador

def ClassificadorDadosAumentados(numPlantas=36):

    Tem = numeric_column(key='Tem')
    Umi = numeric_column(key='Umi')
    Prec = numeric_column(key='Prec')

    colunas = [Tem,Umi,Prec]

    classificador = tf.estimator.DNNClassifier(hidden_units=[8, 8, 8],
                                               feature_columns=colunas,
                                               model_dir='Model/tensorflowDadosAumentados',
                                               n_classes=numPlantas,
                                               optimizer=tf.train.ProximalAdagradOptimizer(
                                                            learning_rate=0.1,
                                                            l1_regularization_strength=0.001
                                                ))
    return classificador

def ClassificadorSklearn(NumPlantas=36):
    from sklearn.neighbors import KNeighborsClassifier
    classificador = KNeighborsClassifier(n_neighbors=NumPlantas, weights='distance')
    # classificador = KNeighborsClassifier(n_neighbors=NumPlantas)
    return classificador






