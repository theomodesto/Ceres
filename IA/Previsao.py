from IA.Classificador import *
import pandas as pd

def Previsao(Dados):
    '''
    :param Dados tem que ser dict
    '''

    Dados = pd.DataFrame.from_dict(data=[Dados])

    funTeste = tf.estimator.inputs.pandas_input_fn(x=Dados,
                                                   shuffle=False)

    classificador = Classificador()

    previsoesDict = {}

    for prev in classificador.predict(input_fn=funTeste):
        # classes = int(prev['classes'][0])
        previsoesDict = MaioresValoes(prev['probabilities'])
    return previsoesDict

def MaioresValoes(Probabilidade):
    MaioreProbabilidade = {}
    valores = 0.1
    idPlanta = 0
    for a in Probabilidade:
        if a > valores and a < 1:
            MaioreProbabilidade = {"IdPlanta":idPlanta,'Probabilidade':a}
        idPlanta = idPlanta + 1
    return MaioreProbabilidade