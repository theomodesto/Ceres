from IA.Classificador import *

#TESTE
TesteCampoMagro = pd.read_csv('Input/CampoMagro.csv', delimiter=',')

TesteCampoMagro = pd.DataFrame(data=TesteCampoMagro.mean(axis=0)).transpose()

print(TesteCampoMagro)

funTeste = tf.estimator.inputs.pandas_input_fn(x=TesteCampoMagro,
                                               shuffle=False)
#TESTE

#TREINAMENTO
X_Treinamento, y_Treinamento = DadosPlantas("Plantas")

# labEnc = LabelEncoder()
# y_Treinamento = pd.DataFrame(data=labEnc.fit_transform(y_Treinamento))
# y_Treinamento = pd.DataFrame(data=y_Treinamento)
print(y_Treinamento)


funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x=X_Treinamento,
                                                         y=y_Treinamento,
                                                         batch_size=1,
                                                         num_epochs=None,
                                                         shuffle=False)

#Classificador
numPlantas = len(y_Treinamento)

TemMin = numeric_column(key='TemMin')
TemMax = numeric_column(key='TemMax')
UmMin = numeric_column(key='Umidaderelativamax')
UmMax = numeric_column(key='Umidaderelativamin')

colunas = [TemMax, TemMin, UmMax, UmMin]

classificador = tf.estimator.DNNClassifier(hidden_units=[8, 8, 8],
                                           feature_columns=colunas,
                                           model_dir='modelTrained',
                                           n_classes=numPlantas
                                           )

classificador.train(input_fn=funcao_treinamento, steps=10000)

#TREINAMENTO

for prev in classificador.predict(input_fn=funTeste):
    print(prev)
