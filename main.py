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



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/datos_SiMEM", methods=["GET", "POST"])
def datos_SiMEM():
    # Configuración de entrada
    x_axis = "-"
    y_axis = "-"
    data_norm = pd.DataFrame()
    data_columns = data_norm.columns
    data_norm = data_norm.to_dict(orient='list')
    
    data_example = [
        ("01-01-2020", 1597),
        ("02-01-2020", 1456),
        ("03-01-2020", 1908),
    ]
    labels = [row[0] for row in data_example]
    values = [row[1] for row in data_example]

    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        dataset_id_SiMEM= request.form['dataset_id_SiMEM'] #"2bff14" #id aportes hídricos 

        # Conexión a la información de SiMEM
        url = "https://www.simem.co/backend-files/api/PublicData?startdate=" + start_date + "&enddate=" + end_date + "&datasetId=" + dataset_id_SiMEM
        response = requests.get(url)

        # Organización de información en una tabla Pandas
        data = pd.read_json(response.text)
        data_norm = pd.json_normalize(data.loc['records']['result'])
        data_columns = data_norm.columns
        data_norm = data_norm.to_dict(orient='list')
        # data_norm = json.dumps(data_norm)
        # data_norm = data_norm.to_dict(orient='list')
        # print(aportes_hidr.head())

        # selección de datos para la grafica basado en los dropdown menus
        x_axis = request.values.get('x_axis')
        y_axis = request.values.get('y_axis')

        if x_axis in data_columns and y_axis in data_columns:
            # Extract selected columns from the DataFrame
            selected_data = data_norm[[x_axis, y_axis]]

            labels = selected_data[x_axis].tolist()
            values = selected_data[y_axis].tolist()

            return render_template("datos_SiMEM.html", 
                                data_columns=data_columns,
                                data_norm=data_norm,
                                labels = labels,
                                values = values
                                )
        return render_template("datos_SiMEM.html", 
                                data_columns=data_columns,
                                data_norm=data_norm,
                                labels = labels,
                                values = values
                                )
    else:
        return render_template("datos_SiMEM.html", 
                                data_columns=data_columns,
                                data_norm=data_norm,
                                labels = labels,
                                values = values
                                )







@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('x_axis')
    return(str(select)) # just to see what select is

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