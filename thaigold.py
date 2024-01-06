from flask import Flask, jsonify
from flask_caching import Cache
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
# Configure cache - Simple cache with a timeout of 300 seconds (5 minutes)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 300})

def scrape_gold_price():
    url = "https://xn--42cah7d0cxcvbbb9x.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', class_='flip pdtable bdo')
    row = table.find('tbody').find('tr')

    return {
        "date_time": row.find('td', {'data-column': 'วันที่/เวลา'}).text,
        "bar_buy": row.find('td', {'data-column': 'ทองคำแท่งรับซื้อ'}).text,
        "bar_sell": row.find('td', {'data-column': 'ทองคำแท่งขายออก'}).text,
        "jewelry_buy": row.find('td', {'data-column': 'ฐานภาษี'}).text,
        "jewelry_sell": row.find('td', {'data-column': 'ทองรูปพรรณขายออก'}).text
    }

@app.route('/thaigold', methods=['GET'])
@cache.cached(timeout=300)  # Cache this view for 5 minutes
def get_thai_gold():
    gold_data = scrape_gold_price()
    return jsonify(gold_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
