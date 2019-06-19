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

    # TesteCampoMagro = EscalonamentoDados(TesteCampoMagro)

    funTeste = tf.estimator.inputs.pandas_input_fn(x=TesteCampoMagro,
                                                   shuffle=False)

    classificador = ClassificadorDadosAumentados()

    for prev in classificador.predict(input_fn=funTeste):
        classes = int(prev['classes'][0])
        print(classes)
        print(prev['probabilities'][classes])
        MaioresValoes(prev['probabilities'])
        # print("IdPlanta: "+classes + " Probabilidade: "+prev['probabilities'][0][classes])

def MaioresValoes(Probabilidade):
    Maiores = []
    valores = 0.1
    idPlanta = 0
    for a in Probabilidade:
        if a > valores:
            Maiores.append({"IdPlanta":idPlanta,'Probabilidade':a})
        idPlanta = idPlanta + 1

    print(Maiores)


def TesteSklearn():
    TesteCampoMagro = pd.read_csv('Input_Teste/CampoMagroMedia.csv', delimiter=',')

    TesteCampoMagro = EscalonamentoDados(TesteCampoMagro)

    filename = 'Model/sklearn/digits_classifier.joblib.pkl'
    with open(filename, 'rb') as f:
        classificador = pickle.load(f)

        matrix = classificador.kneighbors(TesteCampoMagro, return_distance=True)
        print(matrix)


        for prev in classificador.predict(TesteCampoMagro):
            print("IdPlanta:",prev)
            print(matrix[0][0][prev])


