from flask import Flask
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "API works"

@app.route("/rank")
def rank():
    try:
        url = "https://tracker.gg/valorant/profile/riot/siiyoga%23RU1/overview"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем тег img, у которого в alt есть слово "Rank"
        img = soup.find('img', alt=re.compile(r' Rank$'))
        if img:
            alt_text = img['alt']  # например "Platinum 1 Rank"
            rank_with_number = alt_text.replace(' Rank', '')  # "Platinum 1"
            return rank_with_number
        else:
            # Если картинка не найдена – попробуем запасной вариант, ищем "Unranked"
            if soup.find(string=re.compile('Unranked')):
                return "Unranked"
            return "Rank not found"

    except Exception as e:
        return str(e)
