from urllib import request

from flask import  Flask , render_template
from DAL.PlantasDAO import *
app = Flask(__name__)


@app.route('/')
def testHome():

    plantas = list(retornaTodasPlantas())
    return render_template('home.html',result = plantas)


@app.route('/Plante/<id>', methods=['POST','GET'])
def Plante(id):

    passosPlantio = ''
    for planta in list(retornaPlantasPorId(1)):
        for passo in planta['Passos']:
            passosPlantio = planta['Passos']
    return render_template('passos.html', passos = passosPlantio)


@app.route('/geoloc/<lat>/<log>')
def show_user_profile(lat,log):
    # show the user profile for that user
    return  lat + log


app.run()
