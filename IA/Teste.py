import pickle

from IA.Classificador import *
from Util.EscalonamentoDados import *

import pandas as pd

def Teste():
    TesteCampoMagro = pd.read_csv('Input_Teste/CampoMagroMedio.csv', delimiter=',')

    # TesteCampoMagro = pd.DataFrame(data=TesteCampoMagro.mean(axis=0)).transpose()
    scaler = MinMaxScaler(feature_range=(0,1))

    TesteCampoMagro = pd.DataFrame(data=scaler.fit_transform(TesteCampoMagro), columns=TesteCampoMagro.columns)

    print(TesteCampoMagro)

    funTeste = tf.estimator.inputs.pandas_input_fn(x=TesteCampoMagro,
                                                   shuffle=False)

    classificador = Classificador()

    for prev in classificador.predict(input_fn=funTeste):
        print(prev['class_ids'][0])

def TesteDadosAumentados():
    TesteCampoMagro = pd.read_csv('Input_Teste/CampoMagroMedia.csv', delimiter=',')

    TesteCampoMagro = EscalonamentoDados(TesteCampoMagro)

    funTeste = tf.estimator.inputs.pandas_input_fn(x=TesteCampoMagro,
                                                   shuffle=False)

    classificador = ClassificadorDadosAumentados()

    for prev in classificador.predict(input_fn=funTeste):
        print(prev)


def TesteSklearn():
    TesteCampoMagro = pd.read_csv('Input_Teste/CampoMagroMedia.csv', delimiter=',')

    TesteCampoMagro = EscalonamentoDados(TesteCampoMagro)

    print(TesteCampoMagro.head())

    filename = 'Model/sklearn/digits_classifier.joblib.pkl'
    with open(filename, 'rb') as f:
        classificador = pickle.load(f)

        for prev in classificador.predict(TesteCampoMagro):
            print("IdPlanta:",prev)


