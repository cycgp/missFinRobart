from flask import Flask, send_file, send_from_directory, request, jsonify, render_template
from getData.weather import getWeather
from getData.stock import getStock
from getData.petroleum import getPageSource
import re

app = Flask(__name__, static_url_path='', template_folder='templates')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/en")
def index_eng():
    return send_file('templates\\index_eng.html')

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/statics/<path:path>')
def send_statics(path):
    return send_from_directory('statics', path)

@app.route('/_add_numbers')
def add_numbers():
    query = request.args.get('query')
    reply = 'QQ 偶不知道你在說什麼RRRRRR'
    try:
        if '天氣如何' in query:
            reply = '瑞芳的氣溫是' + getWeather()
        elif '我美嗎' in query:
            reply = '你好美'
        elif '你好' in query:
            reply = '你好RRR'
        elif '股票' in query:
            query = re.split('股票|的',query)
            code =  query[1]
            query = query[2]
            reply = getStock(code, query)
        elif '油價' in query:
            reply = getPageSource()
    except Exception as e:
        print(e)
        pass
    return jsonify(result=reply)

if __name__ == "__main__":
    app.run()
