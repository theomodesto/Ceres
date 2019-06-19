from urllib import request

from flask import  Flask , render_template
from DAL.PlantasDAO import *
app = Flask(__name__)


@app.route('/')
def testHome():

    plantas = list(retornaTodasPlantas())
    return render_template('home.html',result = plantas)


@app.route('/Plante/<id>', methods=['POST'])
def Plante(id):
    passos = ['']
    for planta in list(retornaTodasPlantas()):
        print(planta['idPlanta'])
        if planta['idPlanta'] == id:
            print(planta['Passos'])
            passos = planta['Passos']

    print(passos)
    return render_template('passos.html', passos = passos)


@app.route('/geoloc/<lat>/<log>')
def show_user_profile(lat,log):
    # show the user profile for that user
    return  lat + log


app.run()