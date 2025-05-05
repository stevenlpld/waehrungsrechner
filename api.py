from flask import Flask, jsonify
import json
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Willkommen bei der SAP REST API!"

@app.route("/frage")
def frage():
    return jsonify({
        "frage": "Was ist SAP BTP?",
        "antwort": "Eine Cloud-Plattform für Daten, KI, Integration und Entwicklung."

    })
    return Response(
        json.dumps(daten, ensure_ascii=False),
        content_type="application/json; charset=utf-8"
    )

@app.route("/frage2")
def frage2():
    return jsonify({
        "frage2": "Wie heißt der beste Entwickler?",
        "antwort2": "Steven Leipold"
    })
    return Response(
        json.dumps(daten, ensure_ascii=False),
        content_type="application/json; charset=utf-8"
    )

@app.route("/weisheiten")
def weisheiten():
    return jsonify({
        "weisheit": "Lerne coden und schaffe es weg von deinem jetzigen Arbeitgeber",
        "weisheit2": "Verdiene mehr Geld, um dir vielleicht doch noch was leisten zu können"
    })
    return Response(
        json.dumps(daten, ensure_ascii=False),
        content_type="application/json; charset=utf-8"
    )

if __name__ == "__main__":
    app.run(debug=True)