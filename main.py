"""
@author: gregoriovelasquezgomez
"""
# librerias
from flask import Flask, render_template
import random 
import json
from time import time
import requests
import pandas as pd
import numpy as np
import matplotlib.cm as cm
from matplotlib import rcParams

# Configuración de entrada
start_date = "2023-11-01"
end_date = "2023-11-17"
dataset_id_SiMEM= "2bff14"

# Conexión a la información de SiMEM
url = "https://www.simem.co/backend-files/api/PublicData?startdate=" + start_date + "&enddate=" + end_date + "&datasetId=" + dataset_id_SiMEM
response = requests.get(url)

# Organización de información en una tabla Pandas
data = pd.read_json(response.text)
aportes_hidr = pd.json_normalize(data.loc['records']['result'])


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route('/Random_Data', methods=["GET", "POST"])
def Random_Data():
    Random_Data = []
    for i in range(1,10):
        Random_Data.append(random.randint(0,100))
    my_data = {
        "YData":Random_Data
    }
    return my_data

if __name__ == "__main__":
    app.run(debug=True)