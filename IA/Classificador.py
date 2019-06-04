import tensorflow as tf
from tensorflow.feature_column import numeric_column
from sklearn.neighbors import KNeighborsClassifier



def Classificador(numPlantas=20):

    TemMin = numeric_column(key='TemMin')
    TemMax = numeric_column(key='TemMax')
    UmMin = numeric_column(key='Umidaderelativamax')
    UmMax = numeric_column(key='Umidaderelativamin')

    colunas = [TemMax, TemMin, UmMax, UmMin]

    classificador = tf.estimator.DNNClassifier(hidden_units=[8, 8],
                                               feature_columns=colunas,
                                               model_dir='Model/tensorflow',
                                               n_classes=numPlantas,
                                               optimizer=tf.train.ProximalAdagradOptimizer(
                                                      learning_rate=0.1,
                                                      l1_regularization_strength=0.001
                                                ) )
    return classificador

def ClassificadorDadosAumentados(numPlantas=20):

    Tem = numeric_column(key='Tem')
    Umi = numeric_column(key='Umi')

    colunas = [Tem,Umi]

    classificador = tf.estimator.DNNClassifier(hidden_units=[8, 8, 8],
                                               feature_columns=colunas,
                                               model_dir='Model/tensorflowDadosAumentados',
                                               n_classes=numPlantas,
                                               optimizer = tf.train.ProximalAdagradOptimizer(
                                                            learning_rate=0.1,
                                                            l1_regularization_strength=0.001
                                                            )
                                               )
    return classificador

def ClassificadorSklearn(NumPlantas=20):
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.naive_bayes import GaussianNB
    classificador = KNeighborsClassifier()
    return classificador






