from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import re

app = Flask(__name__)

headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36"}
galleries = [("디제이맥스","djmaxrespect"),("사이터스","rayarkcytus"),("지브리","ghibli"),("하프라이프","halflife3"),("보이즈","voezvalkyrie"),("디모","deemo"),("동방","touhou")]
regex = [("(노|놐|누|눜)(.?)","냐\g<2>"),("(노|놐|누|눜|이기)([.,!?;ㄱ-ㅎ]*)$","냐\g<2>"),("되노","되냐"),("무친","미친"),("무쳤","미쳤"),("노무","너무"),("운지","좆망")]
@app.route('/')
def index():
    return render_template("gallery.html", galleries=galleries)

@app.route('/<id>')
def gall(id):
    params = "&".join([f"{i[0]}={i[1]}" for i in request.args.items()])
    response = requests.get(f"https://m.dcinside.com/board/{id}?{params}", headers=headers)
    content = response.content.decode("utf-8")
    for reg in regex:
        content = re.compile(reg[0]).sub(reg[1],content)
    soup = BeautifulSoup(content, "html.parser")
    for s in soup.select("script"): s.decompose()
    for a in soup.select("a"):
        a["href"] = a["href"].replace("https://m.dcinside.com/board","")
    return str(soup)

@app.route('/<id>/<no>')
def doc(id, no):
    response = requests.get(f"https://m.dcinside.com/board/{id}/{no}", headers=headers)
    content = response.content.decode("utf-8")
    for reg in regex:
        content = re.compile(reg[0]).sub(reg[1],content)
    soup = BeautifulSoup(content, "html.parser")
    for s in soup.select("script"): s.decompose()
    for a in soup.select("a"):
        a["href"] = a["href"].replace("https://m.dcinside.com/board","")
    return str(soup)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)