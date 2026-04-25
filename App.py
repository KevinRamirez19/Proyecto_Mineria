from flask import Flask, render_template
import Clustering

app = Flask(__name__)

#@app.route("/")
#def home():
#    return "Hola Mundo"
#
@app.route("/")
def Prueba():
    return render_template("index.html")