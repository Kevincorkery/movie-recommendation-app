from flask import Blueprint, jsonify

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return jsonify({"message": "Movie service running"})

@main.route("/health")
def health():
    return jsonify({"status": "ok"})