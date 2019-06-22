from IA.Classificador import *
import pandas as pd

def Previsao(Dados):
    '''
    :param Dados tem que ser dict
    '''
    for key in Dados:

        Dados = pd.DataFrame(data=[Dados[key]])

        funTeste = tf.estimator.inputs.pandas_input_fn(x=Dados,
                                                       shuffle=False)

        classificador = Classificador()

        previsoesDict = {}

        for prev in classificador.predict(input_fn=funTeste):
            # classes = int(prev['classes'][0])
            print(MaioresValoes(prev['probabilities']))

    # return previsoesDict
    pass

def MaioresValoes(Probabilidade):
    MaioreProbabilidade = {}
    valores = 0.1
    idPlanta = 0
    for a in Probabilidade:
        if a > valores and a < 1:
            MaioreProbabilidade = {"IdPlanta":idPlanta,'Probabilidade':a}
        idPlanta = idPlanta + 1
    return MaioreProbabilidade