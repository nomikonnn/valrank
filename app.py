from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "API works"

@app.route("/rank")
def rank():
    try:
        url = "https://api.henrikdev.xyz/valorant/v1/mmr/eu/siiyoga/RU1"

        response = requests.get(url)

        if response.status_code != 200:
            return f"API Error: {response.status_code}"

        data = response.json()

        rank = data["data"]["currenttierpatched"]
        rr = data["data"]["ranking_in_tier"]

        return f"{rank} ({rr} RR)"

    except Exception as e:
        return f"Error: {str(e)}"
