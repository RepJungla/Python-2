from flask import Flask, render_template_string
import json

app = Flask(__name__)

with open("data.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

@app.route("/")
def index():
    with open("index.html", "r", encoding="utf-8") as f:
        plantilla = f.read()
    return render_template_string(plantilla, datos=datos)

app.run(debug=True)
