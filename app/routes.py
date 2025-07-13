
import os
from flask import Blueprint, render_template, request
import pickle
import numpy as np

TEMPLATES_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
main = Blueprint("main", __name__, template_folder=TEMPLATES_PATH)

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(model_path, "rb") as f:
    model = pickle.load(f)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        age = int(request.form["age"])
        weight = int(request.form["weight"])
        condition = int(request.form["condition"])

        input_data = np.array([[age, weight, condition]])
        dosage = model.predict(input_data)[0]

        return render_template("result.html", dosage=round(dosage, 2))
    return render_template("index.html")
