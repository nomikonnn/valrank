from flask import Flask
import requests

app = Flask(__name__)

@app.route("/rank")
def rank():
    r = requests.get("https://api.henrikdev.xyz/valorant/v1/mmr/eu/siiyoga/RU1").json()
    return f"{r['data']['currenttierpatched']} ({r['data']['ranking_in_tier']} RR)"
