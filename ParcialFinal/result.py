
# importamos lo necesario
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from flask import Flask, render_template, request

# Instancia de Flask. Aplicación
app = Flask(__name__)

# Creamos nuestro primer route. '/login'
@app.route('/')
def template():
 # Renderizamos la plantilla. Formulario HTML.
 # templates/form.html
 return render_template("primeraPagina.html")

# Definimos el route con el método GET
@app.route('/',methods=['POST'])
def usuario():
 # Obtenemos la información del parametro "nombreUser"
 # Esto lo hacemos con "request.args.get"
 valorx=request.form.get('primeraColumna')
 valory=request.form.get('segundaColumna')
 doc = request.files['doc']
 # create the folders when setting up your app
 os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)

 # when saving the file
 doc.save(os.path.join(app.instance_path, 'htmlfi', doc.filename))

 csv = pd.read_csv("D:\\Luis Fer\\U\\2019\\Infografia\\ParcialFinal\\instance\\htmlfi\\"+doc.filename)

 print ("aaaaaaaaaa")
 scatter = request.form.get('scatter')
 print (scatter)
 if scatter == 'on':
     csv.plot.scatter(x=valorx, y=valory)
     print ("bbbbbbb")
     plt.savefig("scatter.png")

 lineal = request.form.get('lineal')
 if lineal  == 'on' :
     csv.plot(y=valory, x=valorx)
     plt.savefig("lineal.png")

 barras = request.form.get('barras')
 if barras  == 'on' :
     csv.plot.bar(y=valory, x=valorx)
     plt.savefig("barras.png")

 barrasY = request.form.get('barrasY')
 if barrasY  == 'on' :
     csv.plot.bar(y=[valory,'county'], x=valorx)
     plt.savefig("barrasy.png")

 pie = request.form.get('pie')

 if pie == 'on' :
     csv.plot.pie(subplots=True)
     plt.savefig("pie.png")

 return "<h1>Graficando" + doc.filename +"</h1>"


if __name__ == '__main__':
 # Iniciamos la apicación en modo debug
 app.run(debug=True)
