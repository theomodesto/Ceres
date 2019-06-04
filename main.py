from flask import  Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World! "


@app.route('/geoloc/<lat>/<log>')
def show_user_profile(lat,log):
    # show the user profile for that user
    return  lat + log


app.run()