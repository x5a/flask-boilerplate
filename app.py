from flask import Flask, jsonify
from flask_cors import CORS
from redis import Redis

app = Flask("flask-boilerplate")
CORS(app)

redis = Redis(host='redis', port=6379)

@app.route('/test')
def get_test():
    value = redis.get('key')
    if value:
    	value = value.decode("utf-8")

    return jsonify(value=value)

@app.route('/test', methods=["POST"])
def post_test():
    redis.set('key', 'value')
    return jsonify(success=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
