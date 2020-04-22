import os
from flask import Flask, render_template
from markupsafe import escape
import json, random, requests

kd_api_key = os.getenv('koodous_key')

def query_koodous(input):
    headers = {
        'Authorization': 'Token ' + kd_api_key,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Content-type': 'application/json'
        }
    params = {'search':input}
    r = requests.get(url="https://api.koodous.com/apks", headers=headers,params=params)
    first_result = r.json()['results'][0]
    return first_result

app = Flask(__name__)

@app.route('/appid/<input_appid>')
def resolve_appid(input_appid):
    # show the user profile for that user
    # return 'appid %s' % escape(input_appid)
    resp = query_koodous(escape(input_appid))
    return resp

@app.route('/sha256/<input_sha256>')
def resolve_sha256appid(input_sha256):
    # show the user profile for that user
    #return 'sha256 %s' % escape(input_sha256)
    resp = query_koodous(escape(input_sha256))
    return resp

@app.route("/")
def hello():
  return "OK"

if __name__ == "__main__":
  app.run()
