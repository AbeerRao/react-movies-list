from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
URL = "https://www.imdb.com/calendar/?ref_=nv_mv_cal"

@app.route('/movies')
def get_movies():
     movieNames = []
     page = requests.get(URL)
     soup = BeautifulSoup(page.content, 'html.parser')
     div = soup.find('div', id="main")
     for i in div.find_all('ul'):
          for j in i.find_all('li'):
               picURL = "imdb.com" + j.a.get('href')
               movieNames.append(picURL)
     return jsonify(url=movieNames)
     # return jsonify({
     #      "people": {
     #           "abc123": {
     #                "name": "abeer",
     #                "class": "9D"
     #           }, "def456": {
     #                "name": "addu",
     #                "class": "1C"
     #           }
     #      }
     # })