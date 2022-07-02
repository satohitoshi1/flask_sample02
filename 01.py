from flask import Flask


app = Flask(__name__)


@app.route("/")  # デコレーター /アクセスがあったとき ～:5000/
def hello():
    return "Hello Member"


if __name__ == "__main__":
    app.run(debug=True)
