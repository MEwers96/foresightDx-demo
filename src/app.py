import logging

import os
from json import loads, dumps
from flask import Flask, redirect, render_template, request, session, url_for

import httpx
from dotenv import load_dotenv
from os.path import join, dirname

from service.DNA_Analysis import get_molecular_masses, get_shipping_label, get_units_and_links


dotenv_path = join(dirname(__file__), './local.env')
load_dotenv(dotenv_path)
app = Flask(__name__, template_folder="../templates/pages", static_folder="../templates/static")
app.config["DEBUG"] = True
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["GET", "POST"])
def analyze():
    print("HERE")
    print(request.get_data())
    request_data = loads(request.get_data())

    dna_sequence =request_data["dna_sequence"]

    shipping_label = get_shipping_label(dna_sequence)
    parts_info = get_units_and_links(dna_sequence)
    mass_info = get_molecular_masses(dna_sequence)

    print(shipping_label, parts_info, mass_info)
    return render_template("analyze.html", shipping_label=shipping_label, parts_info=parts_info, mass_info=mass_info)





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001,  debug=True)