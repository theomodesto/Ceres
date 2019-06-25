from flask import  Flask, render_template,request
from DAL.PlantasDAO import *
from IA.Previsao import *
from Util.PowerLarcAPI import *
from DAL.PrevisaoDAO import *

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/Plantas/<lat>/<lon>', methods=['POST','GET'])
def previsao(lat,lon):
    print("As cordenadas passadas foram:" + lat,lon)
    previsoes = previsaoFinal(lat,lon)
    return render_template('plantas.html', result=previsoes)

@app.route('/Passos/<id>',methods=['POST','GET'])
def Plante(id):
    planta = retornaPlantasPorId(id)
    return render_template('passos.html',passos=planta["Passos"])

app.run()