from flask import  Flask , render_template
from DAL.PlantasDAO import *
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/Index/")
def chamarHTML():
    '''for planta in retornaPlantasPorId(int(id)):
        name = planta["Nome"]
        Categoria = planta["Categoria"]'''
    #print(list(retornaPlantasPorId(int(id))))
    return render_template('Index.html',result = retornaTodasAsPlantas())

@app.route('/geoloc/<lat>/<log>')
def show_user_profile(lat,log):
    # show the user profile for that user
    return  lat + log


app.run()