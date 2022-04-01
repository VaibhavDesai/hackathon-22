from flask import Flask

app = Flask(__name__)

@app.route("/rest/applinks/1.0/manifest")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/oauth")
def hello_world1():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5002)