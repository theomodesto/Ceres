import pickle

from IA.Classificador import *

import pandas as pd

from sklearn.externals import joblib

def Teste():
    TesteCampoMagro = pd.read_csv('INPUT_TESTE/CampoMagro.csv', delimiter=',')

    # TesteCampoMagro = pd.DataFrame(data=TesteCampoMagro.mean(axis=0)).transpose()

    print(TesteCampoMagro)

    funTeste = tf.estimator.inputs.pandas_input_fn(x=TesteCampoMagro,
                                                   shuffle=False)

    classificador = Classificador(2946)

    for prev in classificador.predict(input_fn=funTeste):
        print(prev['class_ids'][0])

def TesteSklearn():
    TesteCampoMagro = pd.read_csv('INPUT_TESTE/CampoMagro.csv', delimiter=',')

    print(TesteCampoMagro)

    filename = 'MODEL/digits_classifier.joblib.pkl'
    with open(filename, 'rb') as f:
        classificador = pickle.load(f)

        for prev in classificador.predict(TesteCampoMagro):
            print("IdPlanta:",prev)

# Teste()
TesteSklearn()


