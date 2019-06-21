from flask import  Flask, render_template,request
from DAL.PlantasDAO import *

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html',
                           result=list(retornaTodasPlantas())
                           )

@app.route('/Plante/<id>',methods=['GET'])
def Plante(id):
    # passos = []
    # for planta in list(retornaTodasPlantas()):
    #     if planta['idPlanta'] == id:
    #         passos = planta['Passos']
    planta = retornaPlantasPorId(id)[0]
    return render_template('passos.html'
                           ,passos=planta["Passos"]
                           )

@app.route('/geoloc/<lat>/<log>')
def show_user_profile(lat,log):
    return  lat + log

app.run()