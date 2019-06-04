from Ia.DadosTreinamento import *
from Ia.Classificador import *
import pickle

def Treinamento():

    X_Treinamento, y_Treinamento = DadosPlantas()

    print(X_Treinamento.head())
    print(y_Treinamento.head())

    # labEnc = LabelEncoder()
    # y_Treinamento = pd.DataFrame(data=labEnc.fit_transform(y_Treinamento))

    funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x=X_Treinamento,
                                                             y=y_Treinamento,
                                                             batch_size=1,
                                                             num_epochs=None,
                                                             shuffle=False)

    numPlantas = len(y_Treinamento)

    classificador = Classificador_Min_Max()

    print("Treinando a IA!!!")

    classificador.train(input_fn=funcao_treinamento,
                        steps=10000)

    eval = classificador.evaluate(input_fn=funcao_treinamento,steps=10000)

    print("Treinamento concluido!!!\nScore:",eval)

    return True

def TreinamentoSklearn():
    X_Treinamento, y_Treinamento = DadosPlantas()

    # numPlantas = len(y_Treinamento)

    classificador = ClassificadorSklearn()

    print("Treinando a IA!!!")

    classificador.fit(X_Treinamento,y_Treinamento)

    print("Treinamento concluido!!!\nScore: ",classificador.score(X_Treinamento,y_Treinamento))

    filename = 'Model/digits_classifier.joblib.pkl'
    f = open(filename,'wb')
    pickle.dump(classificador, f)

    return classificador

Treinamento()
# TreinamentoSklearn()