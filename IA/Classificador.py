import tensorflow as tf
from tensorflow.feature_column import numeric_column

def Classificador(numPlantas=28):

    Tem = numeric_column(key='Tem')
    Umi = numeric_column(key='Umi')
    Prec = numeric_column(key='Prec')

    colunas = [Tem, Umi, Prec]

    classificador = tf.estimator.DNNClassifier(hidden_units=[32, 32, 32],
                                               feature_columns=colunas,
                                               model_dir='Model/tensorflow',
                                               n_classes=numPlantas,
                                               )

    # classificador = tf.estimator.LinearClassifier(
    #                                               feature_columns=colunas,
    #                                               model_dir='Model/tensorflowLinear',
    #                                               n_classes=numPlantas
    #                                               )

    return classificador

def ClassificadorSklearn(NumPlantas=37):
    from sklearn.neighbors import KNeighborsClassifier
    # from sklearn.naive_bayes import GaussianNB # 0.84 Precisão #
    classificador = KNeighborsClassifier(n_neighbors=NumPlantas, weights='distance')
    # classificador = GaussianNB()

    return classificador






