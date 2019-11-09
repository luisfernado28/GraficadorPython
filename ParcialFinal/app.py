
# importamos lo necesario
from flask import Flask , render_template, request
# Instancia de Flask. Aplicación
app = Flask(__name__)

@app.route('/')
def home_page():
    #return "Hello World!"
    return render_template('primeraPagina.html');




if __name__ == '__main__':
    app.run(debug=True)
