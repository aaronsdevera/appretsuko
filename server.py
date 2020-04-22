# This is free and open source software,
# but was made with love and support from White Ops
# 
#     ████████
#   ██   ▄▄   ██
# ██  ▐█ ██ █▌  ██
# ██  ▐█ ██ █▌  ██           White Ops - Keep It Human
# ██  ▐█ ██ █▌  ██           www dot whiteops dot com
# ██  ▐█ ██ █▌  ██
#   ██   ▀▀   ██
#     ████████
# 
#
# a p p r e t s u k o
# resolve android appids to sha256 (and more) using koodous
# api server below

import os
from flask import Flask, render_template
from markupsafe import escape
import json, random, requests

kd_api_key = os.getenv('koodous_key')

def parse_koodous_result(result):
    possible_version = result['displayed_version']
    app_name = result['app']
    company_name = result['company']
    created_time = result['created_on']
    md5 = result['md5']
    sha1 = result['sha1']
    sha256 = result['sha256']
    appid = result['package_name']
    return {
        'possible_version':possible_version,
        'app_name' : app_name,
        'company_name' : company_name,
        'created_time' : created_time,
        'md5' : md5,
        'sha1' : sha1,
        'sha256' : sha256,
        'appid' : appid
        }

def query_koodous(input):
    headers = {
        'Authorization': 'Token ' + kd_api_key,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Content-type': 'application/json'
        }
    params = {'search':input}
    r = requests.get(url="https://api.koodous.com/apks", headers=headers,params=params)
    results = r.json()['results']
    if len(results) == 0:
        return {'results':'NULL'}
    else:
        results_length = len(results)
        parsed_results = []
        for result in results:
            parsed_results.append(parse_koodous_result(result))

        top_result = parsed_results[0]
        if results_length > 1:
            returned_parsed_results = parsed_results[1:]
            return {
                'possible_matches': str(results_length),
                'top_match': top_result,
                'other_matches': returned_parsed_results
            }
        else:
            return {
                'possible_matches': str(results_length),
                'top_match': top_result
            }

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
