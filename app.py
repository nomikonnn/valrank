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

        # 1. Пробуем через alt картинки (может не работать из-за динамики)
        img = soup.find('img', alt=re.compile(r' Rank$'))
        if img:
            alt_text = img['alt']
            rank_with_number = alt_text.replace(' Rank', '')
            return rank_with_number

        # 2. Запасной вариант: мета-тег twitter:description
        meta_tag = soup.find('meta', attrs={'name': 'twitter:description'})
        if meta_tag and meta_tag.get('content'):
            content = meta_tag['content']
            # Ищем "Currently <ранг>" или "Rank: <ранг>" и т.п.
            match = re.search(r'Currently\s+([A-Za-z]+\s*\d?)', content)
            if match:
                return match.group(1)  # например "Platinum 1"
            # Если вдруг формат изменился, пробуем найти любое слово-ранг
            rank_words = ['Radiant', 'Immortal', 'Ascendant', 'Diamond',
                          'Platinum', 'Gold', 'Silver', 'Bronze', 'Iron', 'Unranked']
            for word in rank_words:
                if word in content:
                    return word

        # 3. Если совсем ничего не нашли
        return "Rank not found"

    except Exception as e:
        return str(e)
