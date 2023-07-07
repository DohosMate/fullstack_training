import requests
import json
from flask import Flask

""" response = requests.get("https://api.stackexchange.com/2.3/answers?order=desc&sort=activity&site=stackoverflow")

for data in response.json()['items']:
    print(data['owner']['account_id']) """

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello!'