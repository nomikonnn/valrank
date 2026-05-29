from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "API works"

@app.route("/rank")
def rank():
    url = "https://api.henrikdev.xyz/valorant/v1/mmr/eu/siiyoga/RU1"

    r = requests.get(url).json()

    rank = r["data"]["currenttierpatched"]
    rr = r["data"]["ranking_in_tier"]

    return f"{rank} ({rr} RR)"
