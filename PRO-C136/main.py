from flask import Flask, request, jsonify
from data import data

app = Flask(__name__)

@app.route("/")

def index():
    return jsonify({
        "data": data,
        "message" : "success"
    }), 200


@app.route("/star-info")

def star_info():
    name = request.args.get("name")
    star_data = next(i for i in data if i["name"] == name)
    
    return jsonify({
        "data": star_data,
        "message" : "success"
    }), 200


if __name__ == '__main__':
    app.run(debug = True) 