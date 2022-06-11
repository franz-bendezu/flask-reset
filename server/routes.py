
from flask import Flask, jsonify, request
import data_controller

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

@app.route('/data', methods=["GET"])
def get_data():
    data = data_controller.get_data()
    return jsonify(data)


@app.route("/data", methods=["POST"])
def insert_data():
    payload = request.get_json()
    result = data_controller.insert_data(payload)
    return jsonify(result)


@app.route("/data/<id>", methods=["GET"])
def get_data_by_id(id):
    game = data_controller.get_by_id(id)
    return jsonify(game)