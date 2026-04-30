from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Datos simulados de los 5 municipios de Cundinamarca


@app.route('/')
def index():
    return render_template('index.html')




