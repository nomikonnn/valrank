from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    return "API works"

@app.route("/rank")
def rank():
    try:
        url = "https://tracker.gg/valorant/profile/riot/siiyoga%23RU1/overview"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)

        html = response.text

        # Ищем ранг в странице
        if "Ascendant" in html:
            return "Ascendant"
        elif "Diamond" in html:
            return "Diamond"
        elif "Platinum" in html:
            return "Platinum"
        elif "Gold" in html:
            return "Gold"
        elif "Silver" in html:
            return "Silver"
        elif "Bronze" in html:
            return "Bronze"
        elif "Iron" in html:
            return "Iron"
        elif "Radiant" in html:
            return "Radiant"
        elif "Immortal" in html:
            return "Immortal"

        return "Rank not found"

    except Exception as e:
        return str(e)
