import re
import glob
from flask import Flask, jsonify

filename = "config_files\*.txt"

def getdatafromconfigs(filename):
    result = {}
    for filename in glob.glob(filename):
        ipinfo = []
        for line in open(filename):
            pat = "(ip address) ((?:[0-9]{1,3}[\.]){1,3}[0-9]{1,3}) ((?:[0-9]{1,3}[\.]){3}[0-9]{1,3})"
            m = re.match(pat, line.strip().lower())
            if m:
                ipaddr = m.group(2) + "/" + m.group(3)
                ipinfo.append(ipaddr)
            if re.match("(hostname)", line.strip().lower()):
                hname = line.strip().lower().split(" ")[1]
        result[hname] = list(set(ipinfo))
    return result

res = getdatafromconfigs(filename)


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return 'Go to <a href="/configs">/configs</a> to see the hostnames; ' \
           'Go to /config/[name] to see [name] config. Thanks!'

@app.route("/configs")
def configs():
    return jsonify(list(res.keys()))

@app.route("/config/<name>")
def config(name):
    try:
        return jsonify(res[name])
    except:
        return "No such page found"



if __name__ == '__main__':
    app.run(debug=True)