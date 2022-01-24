from flask import Flask
import json, re

app = Flask(__name__)

@app.route("/<cpf>")
def check_cpf(cpf):
    blacklist = open("./blacklist.txt")
    status = "FREE"
    for bcpf in blacklist:
        if (cpf.strip() == re.sub("\D", "", bcpf)):
            status = "BLOCK"
            break
    blacklist.close()
    return json.dumps({ "status": status })