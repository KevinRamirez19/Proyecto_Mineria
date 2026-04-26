from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Datos simulados de los 5 municipios de Cundinamarca
municipios_data = {
    "Soacha": {
        "poblacion": 700000,
        "vulnerables": 285000,
        "pobreza": 42.3,
        "sin_salud": 18.7,
        "sin_educacion": 22.1,
        "desempleo": 19.4,
        "color": "#E74C3C"
    },
    "Facatativá": {
        "poblacion": 160000,
        "vulnerables": 52000,
        "pobreza": 31.2,
        "sin_salud": 14.3,
        "sin_educacion": 16.8,
        "desempleo": 14.2,
        "color": "#E67E22"
    },
    "Zipaquirá": {
        "poblacion": 130000,
        "vulnerables": 41000,
        "pobreza": 28.9,
        "sin_salud": 12.1,
        "sin_educacion": 15.3,
        "desempleo": 13.1,
        "color": "#F39C12"
    },
    "Chía": {
        "poblacion": 140000,
        "vulnerables": 35000,
        "pobreza": 24.5,
        "sin_salud": 10.2,
        "sin_educacion": 12.7,
        "desempleo": 11.8,
        "color": "#27AE60"
    },
    "Fusagasugá": {
        "poblacion": 145000,
        "vulnerables": 58000,
        "pobreza": 38.6,
        "sin_salud": 16.9,
        "sin_educacion": 20.4,
        "desempleo": 17.3,
        "color": "#8E44AD"
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/municipios')
def api_municipios():
    return jsonify(municipios_data)

@app.route('/api/resumen')
def api_resumen():
    total_poblacion = sum(m["poblacion"] for m in municipios_data.values())
    total_vulnerables = sum(m["vulnerables"] for m in municipios_data.values())
    promedio_pobreza = sum(m["pobreza"] for m in municipios_data.values()) / len(municipios_data)
    return jsonify({
        "total_poblacion": total_poblacion,
        "total_vulnerables": total_vulnerables,
        "promedio_pobreza": round(promedio_pobreza, 1),
        "municipios_analizados": len(municipios_data),
        "registros_dataset": 4000000
    })

if __name__ == '__main__':
    app.run(debug=True)
