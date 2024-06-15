from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "deployment on azure using github actions"

if __name__ == '__main__':
    app.run()