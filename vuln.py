from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/ssrf", methods=['GET'])
def consume_event():

    url = request.args.get('url')

    requests.get(url)

    return jsonify({}), 200
