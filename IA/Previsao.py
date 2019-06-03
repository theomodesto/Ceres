from IA.Classificador import *

"""
:param DadosAPI : DataFrame do Pandas com as colunas 
TemMax,TemMin,Umidaderelativamin,Umidaderelativamax
"""
def previsao(DadosAPI):

    # DadosAPI = pd.DataFrame(data=DadosAPI.mean(axis=0)).transpose()

    funTeste = tf.estimator.inputs.pandas_input_fn(x=DadosAPI,
                                                   shuffle=False)
    # if TreinamentoTensorFlow() == True:
    #     print("Rodou")

    classificador = Classificador()

    for p in classificador.predict(input_fn=funTeste):
        print(p )
