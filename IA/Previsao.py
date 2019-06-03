from IA.Classificador import *

'''
:return IdPlanta que está no banco
'''
def Previsao(DadosAPI):

    # DadosAPI = pd.DataFrame(data=DadosAPI.mean(axis=0)).transpose()

    funTeste = tf.estimator.inputs.pandas_input_fn(x=DadosAPI,
                                                   shuffle=False)
    # if TreinamentoTensorFlow() == True:
    #     print("Rodou")

    classificador = Classificador()

    for p in classificador.predict(input_fn=funTeste):
        print(p['class_ids'][0])
        return p['class_ids'][0]
