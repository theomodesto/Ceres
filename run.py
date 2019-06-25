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

@app.route('Plantas/<lat>/<lon>',methods=['GET','POST'])
def previsao(lat,lon):
    previsoes = []
    ano = ((datetime.now().year)-1)
    Dados = GetDadosAPI(lat, lon, ano)
    for key in Dados:
        previsao = Previsao(Dados[key])
        for prev in previsao:
            planta = retornaPlantasPorId(prev['IdPlanta'])
            previsoes.append([planta, prev['Probabilidade'], key])
    return render_template('listaPlantas.html', previsoes=previsoes)

@app.route('/Plante/<id>',methods=['GET'])
def Plante(id):
    planta = retornaPlantasPorId(id)
    return render_template('passos.html'
                           , passos=planta["Passos"]
                           )

app.run()