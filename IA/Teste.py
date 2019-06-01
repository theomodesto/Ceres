from IA.Classificador import *

TesteCampoMagro = pd.read_csv('Input/CampoMagro.csv', delimiter=',')

TesteCampoMagro = pd.DataFrame(data=TesteCampoMagro.mean(axis=0)).transpose()

print(TesteCampoMagro)

funTeste = tf.estimator.inputs.pandas_input_fn(x=TesteCampoMagro,
                                               shuffle=False)
# if TreinamentoTensorFlow() == True:
#     print("Rodou")

# classificador = tf.estimator.DNNClassifier

TemMin = numeric_column(key='TemMin')
TemMax = numeric_column(key='TemMax')
UmMin = numeric_column(key='Umidaderelativamax')
UmMax = numeric_column(key='Umidaderelativamin')

colunas = [TemMax, TemMin, UmMax, UmMin]

classificador = tf.estimator.DNNClassifier(hidden_units=[8, 8, 8],
                                           feature_columns=colunas,
                                           model_dir='IA/modelTrained')


for p in classificador.predict(input_fn=funTeste):
    print(p)
