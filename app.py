from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "API works"

@app.route("/rank")
def rank():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            "https://api.henrikdev.xyz/valorant/v1/mmr/eu/siiyoga/RU1",
            headers=headers,
            timeout=10
        )

        print(response.text)

        data = response.json()

        if "data" not in data:
            return f"API Response: {data}"

        rank = data["data"]["currenttierpatched"]
        rr = data["data"]["ranking_in_tier"]

        return f"{rank} ({rr} RR)"

    except Exception as e:
        return f"Error: {str(e)}"
