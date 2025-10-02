#Importamos las librerias necesarias
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("index2.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


# Examen practico - Automatización en Infraestructura Digital II - Froylan Alonso Pérez Alanis - José Manuel Pérez Gutiérrez

