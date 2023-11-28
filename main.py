"""
@author: gregoriovelasquezgomez, StevenJG
"""
# librerias
from flask import Flask, render_template, request
import random 
import json
from time import time
import requests
import pandas as pd
import numpy as np
import matplotlib.cm as cm
from matplotlib import rcParams



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/datos_SiMEM", methods=["GET", "POST"])
def datos_SiMEM():
    # Configuración de entrada
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        dataset_id_SiMEM= request.form['dataset_id_SiMEM'] #"2bff14" #id aportes hídricos 

        # Conexión a la información de SiMEM
        url = "https://www.simem.co/backend-files/api/PublicData?startdate=" + start_date + "&enddate=" + end_date + "&datasetId=" + dataset_id_SiMEM
        response = requests.get(url)

        # Organización de información en una tabla Pandas
        data = pd.read_json(response.text)
        aportes_hidr = pd.json_normalize(data.loc['records']['result'])
        # print(aportes_hidr.head())
        return render_template("datos_SiMEM.html", aportes_hidr=aportes_hidr.columns)
    else:
        return render_template("datos_SiMEM.html")

@app.route('/Example_Data', methods=["GET", "POST"])
def Example_Data():
    size_data = 10
    Example_Data = []
    for i in range(1,size_data+1):
        Example_Data.append(random.randint(0,100))

    y_data = {
        "YData":Example_Data
    }

    lineal_x_axis = []
    for i in range(0,size_data):
        lineal_x_axis.append(i)

    x_data = {
        "XData":lineal_x_axis
    }
    return y_data

if __name__ == "__main__":
    app.run(debug=True)