from IA.Classificador import *
import pandas as pd

def Teste():
    TesteCampoMagro = pd.read_csv('INPUT_TESTE/CampoMagro.csv', delimiter=',')

    TesteCampoMagro = pd.DataFrame(data=TesteCampoMagro.mean(axis=0)).transpose()

    print(TesteCampoMagro)

    funTeste = tf.estimator.inputs.pandas_input_fn(x=TesteCampoMagro,
                                                   shuffle=False)

    classificador = Classificador()

    for prev in classificador.predict(input_fn=funTeste):
        print(prev)

Teste()

