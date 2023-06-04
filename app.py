import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from corrector.spell_handler import SpellHandler


app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
@cross_origin()
def api_home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
@cross_origin()
def spell_corrector_route():
    input_text = request.json["data"]
    handler = SpellHandler()
    result = handler.text_corrector(input_text)
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8070, debug=True)