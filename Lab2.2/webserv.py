import re
import glob
from flask import Flask, jsonify

filename = "config_files\*.txt" # где лежат конфиги

def getdatafromconfigs(filename): # создаем функцию
    result = {}
    for filename in glob.glob(filename): # цикл на чтение из файла
        ipinfo = []
        for line in open(filename): # цикл для построчного считывания из файла
            pat = "(ip address) ((?:[0-9]{1,3}[\.]){1,3}[0-9]{1,3}) ((?:[0-9]{1,3}[\.]){3}[0-9]{1,3})" # регулярное выражение для определения IP адресов
            m = re.match(pat, line.strip().lower())
            if m:
                ipaddr = m.group(2) + "/" + m.group(3) # айпи и маска выводится через слеш
            if re.match("(hostname)", line.strip().lower()):
                ipinfo.append(ipaddr)
                hname = line.strip().lower().split(" ")[1]
        result[hname] = list(set(ipinfo))
    return result

res = getdatafromconfigs(filename)


app = Flask(__name__) # запуск вебсервера

@app.route("/") # главная
@app.route("/index")
def index():
    return 'Go to <a href="/configs">/configs</a> to see the hostnames; <br><br>' \ # Красиво с HTML
           'Go to /config/[name] to see [name] config. Thanks!'

@app.route("/configs") # список хостов с конфигами
def configs():
    return jsonify(list(res.keys()))

@app.route("/config/<name>") # отобразить IP / MASK по хостнейму
def config(name):
    try:
        return jsonify(res[name])
    except:
        return "404 - No such page found"



if __name__ == '__main__':
    app.run(debug=True)