from flask import Flask, jsonify
from datetime import datetime
from my_app import app

@app.route("/")
def notify_func():
    return f"<p>Laboratory work is done</p><a href='/healthcheck'>Healthcheck</a>"


@app.route("/healthcheck")
def healthcheck():
    response = jsonify(date=datetime.now(), status="OK")
    response.status_code = 200
    return response
