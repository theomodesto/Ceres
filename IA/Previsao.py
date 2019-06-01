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

    TemMin = numeric_column(key='TemMin')
    TemMax = numeric_column(key='TemMax')
    UmMin = numeric_column(key='Umidaderelativamax')
    UmMax = numeric_column(key='Umidaderelativamin')

    colunas = [TemMax, TemMin, UmMax, UmMin]

    classificador = tf.estimator.DNNClassifier(hidden_units=[8, 8, 8],
                                               feature_columns=colunas,
                                               model_dir='IA/modelTrained')

    for p in classificador.predict(input_fn=funTeste):
        print(p )
