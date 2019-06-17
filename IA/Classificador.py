import tensorflow as tf
from tensorflow.feature_column import numeric_column

def Classificador(numPlantas=36):

    TemMin = numeric_column(key='TemMin')
    TemMax = numeric_column(key='TemMax')
    UmMin = numeric_column(key='UmidadeRelativaMin')
    UmMax = numeric_column(key='UmidadeRelativaMax')
    PrecMin = numeric_column(key='PrecipicacaoMin')
    PrecMax = numeric_column(key='PrecipicacaoMax')

    colunas = [TemMax, TemMin, UmMax, UmMin, PrecMin, PrecMax]

    classificador = tf.estimator.DNNClassifier(hidden_units=[8, 8],
                                               feature_columns=colunas,
                                               model_dir='Model/tensorflow',
                                               n_classes=36,
                                               optimizer=tf.train.ProximalAdagradOptimizer(
                                                      learning_rate=0.1,
                                                      l1_regularization_strength=0.001
                                               ))
    return classificador

def ClassificadorDadosAumentados(numPlantas=1163654):

    Tem = numeric_column(key='Tem')
    Umi = numeric_column(key='Umi')
    Prec = numeric_column(key='Prec')

    colunas = [Tem, Umi, Prec]

    classificador = tf.estimator.DNNClassifier(hidden_units=[8, 8, 8],
                                               feature_columns=colunas,
                                               model_dir='Model/tensorflowDadosAumentados',
                                               n_classes=numPlantas,
                                               optimizer=lambda: tf.train.AdamOptimizer(
                                                   learning_rate=tf.train.exponential_decay(
                                                       learning_rate=0.01,
                                                       global_step=tf.train.get_global_step(),
                                                       decay_steps=10000,
                                                       decay_rate=0.96)
                                                   )
                                               )

    # classificador = tf.estimator.LinearClassifier(
    #                                               feature_columns=colunas,
    #                                               model_dir='Model/tensorflowLinear',
    #                                               n_classes=numPlantas
    #                                               )

    return classificador

def ClassificadorSklearn(NumPlantas=36):
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.naive_bayes import GaussianNB # 0.84 Precisão #
    # classificador = KNeighborsClassifier(n_neighbors=NumPlantas, weights='distance')
    classificador = GaussianNB()

    return classificador






