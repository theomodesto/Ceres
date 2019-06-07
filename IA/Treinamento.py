from IA.DadosTreinamento import *
from IA.Classificador import *
import pickle
from sklearn.preprocessing import StandardScaler, MinMaxScaler

from Util.EscalonamentoDados import *

steps = 10000

def Treinamento():

    X_Treinamento, y_Treinamento = DadosPlantas()

    X_Treinamento = EscalonamentoDados(X_Treinamento)

    funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x=X_Treinamento,
                                                             y=y_Treinamento,
                                                             batch_size=4,
                                                             num_epochs=None,
                                                             shuffle=False)

    # numPlantas = len(y_Treinamento)

    classificador = Classificador()

    print("Treinando a IA !!!")

    classificador.train(input_fn=funcao_treinamento,
                        steps=steps)

    eval = classificador.evaluate(input_fn=funcao_treinamento,steps=steps)

    print("Treinamento concluido !!!\nScore:",eval)

    return True

def TreinamentoDadosAumentados():

    X_Treinamento, y_Treinamento = DadosPlantasAumentados()

    X_Treinamento = EscalonamentoDados(X_Treinamento)

    print(X_Treinamento)

    # labEnc = LabelEncoder()
    # y_Treinamento = pd.DataFrame(data=labEnc.fit_transform(y_Treinamento))

    funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x=X_Treinamento,
                                                             y=y_Treinamento,
                                                             batch_size=4,
                                                             num_epochs=None,
                                                             shuffle=False)

    # numPlantas = len(y_Treinamento)

    classificador = ClassificadorDadosAumentados()

    print("Treinando a IA !!!")

    classificador.train(input_fn=funcao_treinamento,
                        steps=steps)

    eval = classificador.evaluate(input_fn=funcao_treinamento, steps=steps)

    print("Treinamento concluido !!!\nScore:",eval)

    return True

def TreinamentoSklearn():
    X_Treinamento, y_Treinamento = DadosPlantasAumentados()

    scaler = MinMaxScaler(feature_range=(0, 1))

    # X_Treinamento = pd.DataFrame(data=scaler.fit_transform(X_Treinamento),
    #                              columns=X_Treinamento.columns)

    X_Treinamento = EscalonamentoDados(X_Treinamento)

    numPlantas = len(y_Treinamento)

    classificador = ClassificadorSklearn()

    print("Treinando a IA !!!")

    classificador.fit(X_Treinamento, y_Treinamento)

    print("Treinamento concluido !!!\n"
          "Score: ",
          classificador.score(X_Treinamento,y_Treinamento))

    filename = 'Model/sklearn/digits_classifier.joblib.pkl'
    f = open(filename,'wb')
    pickle.dump(classificador, f)

    return classificador


Treinamento()
TreinamentoDadosAumentados()
TreinamentoSklearn()