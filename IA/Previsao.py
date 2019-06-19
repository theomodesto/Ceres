from IA.Classificador import *
import pandas as pd

def Previsao(DadosAPI):

    DadosAPI = pd.DataFrame(data=DadosAPI)

    funTeste = tf.estimator.inputs.pandas_input_fn(x=DadosAPI,
                                                   shuffle=False)

    classificador = Classificador()

    for prev in classificador.predict(input_fn=funTeste):
        classes = int(prev['classes'][0])
        print(classes)
        print(prev['probabilities'][classes])
