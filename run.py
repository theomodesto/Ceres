from flask import  Flask, render_template,request
from DAL.PlantasDAO import *
from IA.Previsao import *
from Util.PowerLarcAPI import *

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html',
                           result=list(retornaTodasPlantas())
                           )

@app.route('/Plante/<id>',methods=['GET'])
def Plante(id):
    planta = retornaPlantasPorId(id)
    return render_template('passos.html'
                           , passos=planta["Passos"]
                           )

@app.route('previsao/<lat>/<lon>')
def previsao(lat,lon):
    previsoes = []
    ano = datetime.year()
    Dados = GetDadosAPI(lat, lon, ano)
    for key in Dados:
        previsao = Previsao(Dados[key])
        planta = retornaPlantasPorId(previsao['IdPlanta'])
        previsoes.append([planta, previsao['Probabilidade'],key])
    print(previsoes)
    return render_template('plantas.html', previsoes)



app.run()