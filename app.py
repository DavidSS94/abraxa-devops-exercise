from multiprocessing import Value
from flask import Flask, request

COUNTER = Value('i', 0)

APP = Flask(__name__)


@APP.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        message = "Hello World!!!"
    if request.method == 'POST':
        COUNTER.value += 1
        message = "Hello World!!!"
    return message


@APP.route("/count")
def count():
    message = "Conteo de invocaciones: " + str(COUNTER.value)
    return message


if __name__ == "__main__":
    APP.run(debug=True, host='0.0.0.0', port=5000)
