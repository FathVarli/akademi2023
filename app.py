from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def bc4m():
    return jsonify(msg="BC4M")




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
