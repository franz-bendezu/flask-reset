from array import array
import json
from flask import jsonify
from db import get_db


def insert_data(payload):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO data(payload) VALUES (?)"
    cursor.execute(statement, [json.dumps(payload, indent=4)])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, payload, timestamp FROM data WHERE id = ?"
    cursor.execute(statement, [id])
    result = cursor.fetchone()
    data = dict()
    data['id'] = result[0]
    data['payload'] = json.loads(result[1])
    data['timestamp'] = result[2]
    return data


def get_data():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, payload,timestamp FROM data"
    cursor.execute(query)
    results = cursor.fetchall()
    result = []
    for i in range(len(results)):
        data = dict()
        data['id'] = results[i][0]
        data['payload'] = json.loads(results[i][1])
        data['timestamp'] = results[i][2]
        result.append(data)
    return result
