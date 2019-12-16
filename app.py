from flask import request
from flask import Flask, jsonify
from multiprocessing import Value

counter = Value('i', 0)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return "Hello World!!!"
    if request.method == 'POST':
        counter.value += 1
        return "Hello World!!!"

@app.route("/count")
def count():
    return "Conteo de invocaciones: " + str(counter.value)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
