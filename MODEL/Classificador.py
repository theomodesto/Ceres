from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from DAO.PlantasDAO import  DadosPlantas
from tensorflow.feature_column import numeric_column
from tensorflow.feature_column import categorical_column_with_hash_bucket
from tensorflow.feature_column import embedding_column
import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import LabelEncoder

X_Treinamento, y_Treinamento = DadosPlantas("Plantas")
labEnco = LabelEncoder()
y_Treinamento = pd.DataFrame(data=labEnco.fit_transform(y_Treinamento) )
print(y_Treinamento)

def TreinamentoSklearn():
    NumPlantas = len(y_Treinamento)
    classificador = KNeighborsClassifier(n_neighbors=NumPlantas)
    classificador.fit(X_Treinamento, y_Treinamento)
    return classificador

def TreinamentoTensorFlow():

    TemMin = numeric_column(key='TemMin')
    TemMax = numeric_column(key='TemMax')
    UmMin = numeric_column(key='Umidaderelativamax')
    UmMax = numeric_column(key='Umidaderelativamin')
    colunas = [TemMax,TemMin,UmMax,UmMin]

    funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x=X_Treinamento, y=y_Treinamento, batch_size=1,
                                                             num_epochs=None, shuffle=False)

    classificador = tf.estimator.DNNClassifier(hidden_units=[8, 8, 8], feature_columns=colunas)
    classificador.train(input_fn=funcao_treinamento, steps=20000)

    return classificador




